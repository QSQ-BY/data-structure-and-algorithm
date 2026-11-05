#include <iostream>
#include <cstring>
#include <vector>
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

//next[j] = k表示以j位置作为结尾的这一段后缀等于以k位置作为结尾的这一段前缀
int KMP(const char* s,const char* t){
    int n = strlen(s);
    int m = strlen(t);
    if(m == 0) return 0;

    //next[i]表示t[i]组最长相同前缀的末尾下标
    vector<int> next(m,-1);
    int j = -1;
    //j指向的是模式串的前一位
    //不用考虑第一位因为只有一个字符的话，那一定是不存在的，规定next[0] = -1
    //从1位置开始求解
    for(int i=1;i<m;i++){
        //当前后缀无法扩展，尝试更短的前后缀
        while(j != -1 and t[i] != t[j+1]){
            j = next[j];
        }
        if(t[i] == t[j+1]){
            j++;
        }
        next[i] = j;
    }
    for(int i=0;i<next.size();i++){
        cout<<next[i]<<" ";
    }
    cout<<"\n";

    //在主串中搜索模式串
    j = -1;
    //j指向的是模式串的前一位
    for(int i=0;i<n;i++){
        //失配，保留较短的已匹配前缀，主串的指针保持不变,
        //只对模式串的指针进行回退操作
        while(j != -1 and s[i] != t[j+1]){
            j = next[j];
        }

        if(s[i] == t[j+1]){
            j++;
        }
        if(j == m-1){
            return i - m + 1;
        }
    }
    return -1;
}

int main(void){
    char s[100],t[100];
    while(~scanf("%s%s",s,t)){
        TEST(sunday,s,t);
        TEST(KMP,s,t);
        cout<<"\n";
    }
    return 0;
}

