//shift_and/shift_or算法，模式串长度不超过32

#include <iostream>
#include <string>
#include <cstring>
#include <cstdio>
using namespace std;
#define TEST(func,s,t){\
    printf("%s(%s,%s) = %d\n",#func,s,t,func(s,t));\
}

//shift_and算法
int shift_and(const char* s,const char* t){
    int code[256] = {0};
    int n = strlen(t);
    if(n == 0) return 0;
    if(n > 32) return -1;
    for(int i=0;t[i];i++){
        code[t[i]] |= (1<<i);
    }
    int p = 0;
    for(int i=0;s[i];i++){
        p = (p<<1|1)&code[s[i]];
        if(p&(1<<(n-1))){
            return i-n+1;
        }
    }
    return -1;
}

//shift_or算法，进行了优化，少了左移之后或1的操作
//使用0表示有效位
int shift_or(const char* s,const char* t){
    int code[256];
    int n = strlen(t);
    if(n == 0) return 0;
    if(n > 32) return -1;
    for(int i=0;i<256;i++) code[i] = -1;
    for(int i=0;t[i];i++){
        code[t[i]&255] &= ~(1<<i);
    }
    int p = -1;
    for(int i=0;s[i];i++){
        //左移前清除符号位，避免对负数直接左移
        p = ((p)<<1)|code[s[i]];
        if((p&(1<<(n-1))) == 0){
            return i-n+1;
        }
    }
    return -1;
}

int main(void){
    char s[100],t[100];
    while(scanf("%99s%99s",s,t) == 2){
        TEST(shift_and,s,t);
        TEST(shift_or,s,t);
        cout<<"\n";
    }
    return 0;
}
