#include <iostream>
#include <cstring>
using namespace std;
#define TEST(func,s,t){\
    printf("%s(%s,%s) = %d\n",#func,s,t,func(s,t));\
}

//暴力匹配算法,brute_force算法，单模匹配算法
int brute_force(const char* s,const char* t){
    for(int i=0;s[i];i++){
        int flag = 1;
        for(int j=0;t[j];j++){
            if(s[i+j] == t[j]){
                continue;
            }
            flag = 0;
            break;
        }
        if(flag == 1){
            return i;
        }
    }
    return -1;//不存在，查找失败
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


int main(void){
    char s[100],t[100];
    while(~scanf("%s%s",s,t)){
        TEST(brute_force,s,t);
        TEST(sunday,s,t);
        cout<<"\n";
    }
    return 0;
}
