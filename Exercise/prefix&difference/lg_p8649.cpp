/* 题目描述
给定一个长度为 N 的数列，A
1
?
 ,A
2
?
 ,?A
N
?
 ，如果其中一段连续的子序列 A
i
?
 ,A
i+1
?
 ,?A
j
?
 (i≤j) 之和是 K 的倍数，我们就称这个区间 [i,j] 是 K 倍区间。

你能求出数列中总共有多少个 K 倍区间吗？

输入格式
第一行包含两个整数 N 和 K (1≤N,K≤10
5
 )。

以下 N 行每行包含一个整数 A
i
?
  (1≤A
i
?
 ≤10
5
 )。

输出格式
输出一个整数，代表 K 倍区间的数目。

输入输出样例
输入 #1复制

5 2
1
2
3
4
5
输出 #1复制

6
 */
#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;
long long  f(long long  number){
    return (number*(number-1))/2;
}
int main(void){
    long long  n;
    long long  k;
    cin>>n>>k;
    vector<long long > prefix(n+1,0);
    unordered_map<long long ,long long > h;
    for(long long  i=1;i<n+1;i++){
        cin>>prefix[i];
        prefix[i] += prefix[i-1];
    }
    for(long long  i=0;i<n+1;i++){
        prefix[i] = prefix[i]%k;
        h[prefix[i]]++;
    }
    long long  ans = 0;
    for(auto x:h){
        long long  number = x.second;
        if(number>1){
            ans +=f(number);
        }
    }
    cout<<ans<<endl;

    //system("pause");
    return 0;
}