/* 注意：本题为上古 NOIP 原题，不保证存在靠谱的做法能通过该数据范围下的所有数据。本题的难度仅代表设计算法可以通过本题原始数据的难度。
本题为搜索题，本题不接受 hack 数据。关于此类题目的详细内容
NOIP2000 提高组 T3
题目描述
单词接龙是一个与我们经常玩的成语接龙相类似的游戏，现在我们已知一组单词，且给定一个开头的字母，要求出以这个字母开头的最长的“龙”（每个单词都最多在“龙”中出现两次），在两个单词相连时，其重合部分合为一部分，例如 beast 和 astonish，如果接成一条龙则变为 beastonish，另外相邻的两部分不能存在包含关系，例如 at 和 atide 间不能相连。
输入格式
输入的第一行为一个单独的整数 n 表示单词数，以下 n 行每行有一个单词，输入的最后一行为一个单个字符，表示“龙”开头的字母。你可以假定以此字母开头的“龙”一定存在。
输出格式
只需输出以此字母开头的最长的“龙”的长度。
输入输出样例
输入 #1复制
5
at
touch
cheat
choose
tact
a
输出 #1复制
23 */
#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <climits>
using namespace std;
#define  MAX_N 20
string start;
vector<int> vis(MAX_N+5,0);
vector<string> s(MAX_N+5);//记录第i个单词
vector<vector<int>> d(MAX_N+5,vector<int>(MAX_N+5,0));//第i个单词和第j个单词重叠部分的长度
int ans = 0;
int n;

int f(const string& s1, const string& s2) {
    int limit = min(s1.size(), s2.size());
    for (int len = 1; len < limit; len++) {
        if (s1.compare(s1.size() - len, len, s2, 0, len) == 0) {
            return len;
        }
    }
    return 0;
}

//当前单词的下标,当前单词的总长度
void dfs(int now_word,int l){
    ans = max(ans,l);
    for(int next_word = 0;next_word<n;next_word++){
        if(d[now_word][next_word] == 0) continue;
        if(vis[next_word]==2) continue;
        vis[next_word]++;
        dfs(next_word,l + s[next_word].size() - d[now_word][next_word]);
        vis[next_word]--;
    }
    return;
}

int main(void){
    scanf("%d",&n);
    for(int i=0;i<n;i++){
        cin>>s[i];
    }
    cin>>start;
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            d[i][j]=f(s[i],s[j]);
        }
    }
    for(int i=0;i<n;i++){
        if(s[i][0] != start[0]) continue;
        vis[i]++;
        dfs(i,s[i].size());
        vis[i]--;
    }
    cout<<ans<<endl;
    return 0;
}