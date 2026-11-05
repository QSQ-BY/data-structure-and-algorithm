//多模匹配算法，基于哈希的思想Rabin_Karp算法
//两个字符串哈希值不相等，那么他们就一定不相等
//两个字符串哈希值相等那么他们也不一定相等
#include <iostream>
#include <cstring>
#include <string>
#include <cstdio>
#include <vector>
#include <unordered_map>
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

//hash = s[i]*base**(n-1-i) 哈希权重与下标进行逆序对应
//hash2 = hash1*base + s[i] - s[i-n]*base**m
//利用前一个位置字符串的哈希值计算得到下一个位置的哈希值，时间复杂度只有O(1)
//先计算得到所有位置的哈希值再与模式串的哈希值进行比较，
//如果哈希值相等就直接比较

#define MOD 9973
int base= 131;
int hash_func(const char* s){
    int h = 0;
    int slen = strlen(s);
    for(int i=slen-1,kbase = 1;i>=0;i--){
        h = (h+s[i]*kbase) % MOD;
        kbase = kbase*base%MOD;
    }
    return h;
}

int hash_func2(string& s){
    int h = 0;
    int slen = s.size();
    for(int i=slen-1,kbase = 1;i>=0;i--){
        h = (h+s[i]*kbase) % MOD;
        kbase = kbase*base%MOD;
    }
    return h;
}
//Rabin_Karp算法进行单模匹配
int Rabin_Karp(const char* s,const char*t){
    if(t[0] == '\0') return 0;
    int thash = hash_func(t);
    int nbase = 1;
    int tlen = strlen(t);
    for(int i=0;t[i];i++) nbase = nbase*base%MOD;
    for(int i=0,h = 0;s[i];i++){
        h = h*base+s[i];
        h = h%MOD;
        if(i >= tlen){
            h = (h - s[i-tlen]*nbase%MOD + MOD)%MOD;
        }
        if(i+1 < tlen){
            continue;
        }
        if(h != thash){
            continue;
        }
        if(strncmp(s+i-tlen+1,t,tlen) == 0){
            return i-tlen+1;
        }
    }

    return -1;
}

//Rabin_Karp算法进行多模匹配，要求所有模式串非空且长度相同
void Rabin_Karp(string &s,vector<string> &t){
    if(t.empty()) return;
    int tlen = static_cast<int>(t[0].size());
    if(tlen == 0){
        cerr<<"多模匹配要求模式串非空。\n";
        return;
    }
    int nbase = 1;
    unordered_map<int,vector<int>> thash;
    for(int i=0;i<static_cast<int>(t.size());i++){
        if(t[i].size() != t[0].size()){
            cerr<<"多模匹配要求所有模式串长度相同。\n";
            return;
        }
        thash[hash_func2(t[i])].push_back(i);
    }
    for(int i=0;i<tlen;i++) nbase = nbase*base%MOD;
    for(int i=0,h = 0;i<static_cast<int>(s.size());i++){
        h = h*base+s[i];
        h = h%MOD;
        if(i >= tlen){
            h = (h - s[i-tlen]*nbase%MOD + MOD)%MOD;
        }
        if(i+1 < tlen){
            continue;
        }
        if(thash.find(h) == thash.end()){
            continue;
        }
        for(int j=0;j<static_cast<int>(thash[h].size());j++){
            if(strncmp(s.c_str()+i-tlen+1,t[thash[h][j]].c_str(),tlen) == 0){
                printf("pos %d:%s\n",i-tlen+1,t[thash[h][j]].c_str());
            }
        }
    }
}

//验证单模匹配算法
void test01(){
    char s[100],t[100];
    while(scanf("%99s%99s",s,t) == 2){
        TEST(Rabin_Karp,s,t);
        TEST(sunday,s,t);
        cout<<"\n";
    }
    return;
}
//多模匹配算法
void test02(){
    int n;
    string s;
    if(!(cin>>n) || n < 0) return;
    vector<string> t(n);
    for(int i=0;i<n;i++){
        if(!(cin>>t[i])) return;
    }

    while(cin>>s){
        Rabin_Karp(s,t);
    }
}
int main(void){
    //test01();
    test02();
    return 0;
}
