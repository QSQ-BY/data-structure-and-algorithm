/* 题目背景
本题不保证存在靠谱的多项式复杂度的做法。测试数据非常的水，各种做法都可以通过，不代表算法正确。因此本题题目和数据仅供参考。

本题为搜索题，本题不接受 hack 数据。关于此类题目的详细内容

题目描述
已知有两个字串 A,B 及一组字串变换的规则（至多 6 个规则），形如：

A 
1
?
 →B 
1
?
 。
A 
2
?
 →B 
2
?
 。
规则的含义为：在 A 中的子串 A 
1
?
  可以变换为 B 
1
?
 ，A 
2
?
  可以变换为 B 
2
?
 ?。

例如：A=abcd，B＝xyz，

变换规则为：

abc→xu，ud→y，y→yz。
则此时，A 可以经过一系列的变换变为 B，其变换的过程为：

abcd→xud→xy→xyz。
共进行了 3 次变换，使得 A 变换为 B。

输入格式
第一行有两个字符串 A,B。

接下来若干行，每行有两个字符串 A 
i
?
 ,B 
i
?
 ，表示一条变换规则。

输出格式
若在 10 步（包含 10 步）以内能将 A 变换为 B，则输出最少的变换步数；否则输出 NO ANSWER!。

输入输出样例
输入 #1复制

abcd xyz
abc xu
ud y
y yz
输出 #1复制

3
说明/提示
对于 100% 数据，保证所有字符串长度的上限为 20，且均由小写英文字母组成。

【题目来源】

NOIP 2002 提高组第二题 */
#include <iostream>
#include <vector>
#include <string>
#include <climits>
#include <map>
using namespace std;

int ans_k;
vector<string> from(10);
vector<string> to(10);
string a;
string b;
int trans_cnt = 0;
int ans = INT_MAX;
map<string,int> dp;

//当前变换为的字符串
void dfs(string& now,int step){
    dp[now] = step;
    if(step>10 or step>ans_k) return;
    if(now == b){
        ans = min(ans,step);
        return;
    }

    for(int i=0;i<trans_cnt;i++){
        int pos = -1;
        pos = now.find(from[i]);
        while(pos != -1){
            string temp = now;
            temp.erase(pos,from[i].size());
            temp.insert(pos,to[i]);
            if(dp.find(temp) == dp.end() or step+1 < dp[temp]){
                dfs(temp,step+1); 
            }
            pos = now.find(from[i],pos+1);
        }
    }
    return;
}

int main(void){
    cin>>a;
    cin>>b;
    while(cin>>from[trans_cnt]>>to[trans_cnt]) trans_cnt++;

    for(int i = 1;i<=10;i++){
        ans_k = i;
        dp.clear();
        dfs(a,0);
        if(ans != INT_MAX) break;
    }
    if (ans == INT_MAX)
        cout << "NO ANSWER!" << '\n';
    else
        cout << ans << '\n';
    return 0;
}