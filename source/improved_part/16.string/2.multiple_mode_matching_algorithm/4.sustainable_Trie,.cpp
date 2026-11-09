//可持续化字典树
//普通字典树只能查找第1到次的操作中是否插入了单词x
//可持久化字典树可以查找在i-j次插入的单词中是否存在单词x，
// 可持久化字典树支持区间查找，普通的字典树则只能进行全局查找
#include <iostream>
#include <cstdio>
using namespace std;
#define MAX_N 10000
#define MAX_LEN 99
#define MAX_NODE (MAX_N*(MAX_LEN+1)+5)
int rt[MAX_N+5] = {0};
int ch[MAX_NODE][26] = {0};
int ch_cnt = 0;
int val[MAX_NODE] = {0};
//插入单词，当前版本根节点，上一个版本的根节点，字符串
void insert(int o,int lst,const char* s){
    for(int i=0;s[i];i++){
        int index = s[i] - 'a';
        ch[o][index] = ++ch_cnt;
        for(int j=0;j<26;j++){
            if(ch[o][j]) continue;
            ch[o][j] = ch[lst][j];
        }
        o = ch[o][index];
        lst = ch[lst][index];
        val[o] = val[lst];
    }
    //终点节点也要继承旧版本的子树，避免插入前缀时丢失已有单词
    for(int j=0;j<26;j++){
        ch[o][j] = ch[lst][j];
    }
    val[o] += 1;
}

int find_once(int x,const char* s){
    int p =rt[x];
    for(int i=0;s[i];i++){
        int index = s[i] - 'a';
        p = ch[p][index];
    }
    return val[p];
}

int find(int a,int b,const char* s){
    //使用前缀和的思想，首先统计到b版本，a-1版本之前一共被插入了多少次最后直接相减就是从a版本到b版本之间一共被插入了多少次
    int x1 = find_once(b,s);
    int x2 = find_once(a-1,s);
    return x1 - x2;
}

int main(void){
    int n = 0;
    if(!(cin>>n) || n<0 || n>MAX_N) return 0;
    char s[MAX_LEN+1];
    for(int i=1;i<=n;i++){
        if(scanf("%99s",s) != 1) return 0;
        rt[i] = ++ch_cnt;
        insert(rt[i],rt[i-1],s);
    }
    int a;
    int b;
    while (scanf("%d%d%99s",&a,&b,s) == 3){
        //在区间[a,b]之间查找字符s，是否出现过以及其出现的次数
        printf("from %d to %d find %s:%d\n",a,b,s,find(a,b,s));
    }
    return 0;
}
