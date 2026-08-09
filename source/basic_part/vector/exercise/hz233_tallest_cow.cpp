/* 题目描述
? 有 N 头牛站成一行。两头牛能够相互看见，当且仅当它们中间的牛身高都比它们矮。现在，我们只知道其中最高的牛是第 P 头，它的身高是 H ，不知道剩余 N?1 头牛的身高。但是，我们还知道 M 对关系，每对关系都指明了某两头牛 Ai,Bi 可以相互看见。求每头牛的身高最大可能是多少。
输入
? 输入的第一行为正整数 N,P,H,M。（1≤N,M≤104,1≤H≤106）
? 接下来的 M 行每行有 2 个正整数，分别表示 Ai,Bi。
输出
? 共 N 行，每行一个数，表示第 i 头牛可能最高的身高。

样例输入
9 3 5 5
1 3
5 3
4 3
3 7
9 8
样例输出
5
4
5
3
4
4
5
5
5 */
#include <iostream>
#include <vector>
#include <unordered_set>
#include <set>
using namespace std;
typedef pair<int,int> PII;
set<PII> relation;
int main(void){
    int n,p,h,m;//p为最高的奶牛
    //h为最高的身高，n为奶牛的总数
    cin>>n>>p>>h>>m;
    vector<int> height(n+5,h);
    height[p-1] = h;
    vector<int> diff(n+5,0);
    diff[0] = h;
    for(int i=0;i<m;i++){
        int num1;
        int num2;
        cin>>num1>>num2;
        int left = min(num1,num2);
        int right = max(num1,num2);
        if(relation.find(PII(left,right)) != relation.end()) continue;
        else relation.insert(PII(left,right));
        diff[left]--;
        diff[right-1]++;
    }
    for(int i=0;i<n;i++){
        if(i==0){
            height[0] = diff[0];
        }else{
            height[i] = height[i-1]+diff[i];
        }
        cout<<height[i]<<endl;
    }
    //system("pause");
    return 0;
}