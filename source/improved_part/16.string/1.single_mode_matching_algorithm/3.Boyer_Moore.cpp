#include <iostream>
#include <cstring>
using namespace std;
#define TEST(func,s,t){\
    printf("%s(%s,%s) = %d\n",#func,s,t,func(s,t));\
}

//sunday算法
int sunday(const char* s,const char* t){
    int len[256] = {0};
    int n = strlen(s);
    int m = strlen(t);
    for(int i=0;i<256;i++){
        len[i] = m+1;//默认向后移动m+1，如果该字符不在模式串中的话
    }
    //字符t[i]应该向后移动m-i个位置
    for(int i=0;t[i];i++){
        len[t[i]] = m - i;
    }
    //每次移动当前母串的最后一位字符的下一位字符
    for(int i=0;i+m <= n;i += len[s[i+m]]){
        int flag = 1;
        for(int j=0;t[j];j++){
            if(s[i+j] == t[j]) continue;
            flag = 0;
            break;
        }
        if(flag == 1) return i;
    }
    return -1;
}

//delta1数组记录的是每一种字符最后出现的位置
//坏字符规则，移动的距离就是i - delta1[t[i]]
int* getDelta1(const char* t){
    int* delta1 = (int*)malloc(sizeof(int)*256);
    for(int i=0;i<256;i++) delta1[i] = -1;
    //初始化为-1，最后移动的距离就是i+1,相当于越过一整个字符串
    for(int i=0;t[i];i++){
        delta1[t[i]] = i;
    }
    return delta1;
}

//预处理suffix数组
//表示以模式串位置 q 结尾的子串，与整个模式串后缀相同的最长长度。
int* getSuffix(const char* t){
    int tlen = strlen(t);
    int* suff = (int*)malloc(sizeof(int)*tlen);
    suff[tlen - 1] = tlen;
    for(int i=0;i<tlen-1;i++){
        int j=0;
        while(j <= i and t[tlen - j - 1] == t[i-j]) j++;
        suff[i] = j;
    }
    return suff;
}

//初始化构建delta2数组
//如果模式串在位置p失配以后，好后缀规则允许右移多长
//好后缀长度= m-1-p其中p表示的是失配的位置
int* getDelta2(const char* t){
    int tlen = strlen(t);
    int last_index = tlen - 1;//最后一个下标大小
    int* suffix = getSuffix(t);
    int* delta2 = (int*)malloc(sizeof(int)*tlen);
    for(int i=0;i<tlen;i++){
        delta2[i] = tlen;
    }
    //有部分后缀与前缀匹配
    //第一种情况，能使用模式串的前缀衔接好后缀的尾部
    for(int i=0;i<tlen;i++){
        if(suffix[i] != i+1){
            continue;
        }//以i位置为结尾的模式串所有前缀能够与后缀匹配就表明长度suffix[i] = i+1
        //长度恰好为i+1说明匹配已经延伸到了整个模式串的开头
        for(int j=0;j<=last_index - suffix[i];j++){
            delta2[j] = last_index - i;
        }
    }

    //另一种情况就是在模式串的前面找到一整个好后缀都能继续宁匹配
    //完全匹配的情况
    for(int i=0;i<last_index;i++){
        delta2[last_index - suffix[i]] = last_index - i;
    }
    return delta2;
}

//BM算法：使用坏字符和好后缀两个转移规则，不太实用
int boyer_moore(const char* s,const char* t){
    int* delta1 = getDelta1(t);
    int* delta2 = getDelta2(t);
    int slen = strlen(s);
    int tlen = strlen(t);
    for(int j=0;j+tlen <= slen;){
        int i = tlen - 1;
        //母串与模式串从右往左进行逐一匹配
        while(i>=0 and t[i] == s[j+i]) i--;
        //如果说最后匹配到头了就说明匹配上了
        if( i == -1){
            return j;
        }
        //使用坏字符规则和好后缀进行向右移动
        j += max(i - delta1[s[j+i]],delta2[i]);
    }
    return -1;
}

int main(void){
    char s[100],t[100];
    while(~scanf("%s%s",s,t)){
        TEST(sunday,s,t);
        TEST(boyer_moore,s,t);
        cout<<"\n";
    }
    return 0;
}

