/* 题目描述
小 T 是一名质量监督员，最近负责检验一批矿产的质量。这批矿产共有 n 个矿石，从 1 到 n 逐一编号，每个矿石都有自己的重量 w 
i
​
  以及价值 v 
i
​
 。检验矿产的流程是：

给定 m 个区间 [l 
i
​
 ,r 
i
​
 ]；
选出一个参数 W；
对于一个区间 [l 
i
​
 ,r 
i
​
 ]，计算矿石在这个区间上的检验值 y 
i
​
 ：
y 
i
​
 = 
j=l 
i
​
 
∑
r 
i
​
 
​
 [w 
j
​
 ≥W]× 
j=l 
i
​
 
∑
r 
i
​
 
​
 [w 
j
​
 ≥W]v 
j
​
 
其中 j 为矿石编号，[p] 是指示函数，若条件 p 为真返回 1，否则返回 0。

这批矿产的检验结果 y 为各个区间的检验值之和。即： 
i=1
∑
m
​
 y 
i
​
 。

若这批矿产的检验结果与所给标准值 s 相差太多，就需要再去检验另一批矿产。小 T 不想费时间去检验另一批矿产，所以他想通过调整参数 W 的值，让检验结果尽可能的靠近标准值 s，即使得 ∣s−y∣ 最小。请你帮忙求出这个最小值。

输入格式
第一行包含三个整数 n,m,s，分别表示矿石的个数、区间的个数和标准值。

接下来的 n 行，每行两个整数，中间用空格隔开，第 i+1 行表示 i 号矿石的重量 w 
i
​
  和价值 v 
i
​
 。

接下来的 m 行，表示区间，每行两个整数，中间用空格隔开，第 i+n+1 行表示区间 [l 
i
​
 ,r 
i
​
 ] 的两个端点 l 
i
​
  和 r 
i
​
 。注意：不同区间可能重合或相互重叠。

输出格式
一个整数，表示所求的最小值。

输入输出样例
输入 #1复制

5 3 15 
1 5 
2 5 
3 5 
4 5 
5 5 
1 5 
2 4 
3 3 
输出 #1复制

10
说明/提示
【输入输出样例说明】

当 W 选 4 的时候，三个区间上检验值分别为 20,5,0，这批矿产的检验结果为 25，此时与标准值 s 相差最小为 10。

【数据范围】

对于 10% 的数据，有 1≤n,m≤10；

对于 30% 的数据，有 1≤n,m≤500；

对于 50% 的数据，有 1≤n,m≤5,000；

对于 70% 的数据，有 1≤n,m≤10,000；

对于 100% 的数据，有 1≤n,m≤2×10 
5
 ，0<w 
i
​
 ,v 
i
​
 ≤10 
6
 ，0<s≤10 
12
 ，1≤l 
i
​
 ≤r 
i
​
 ≤n。 */
#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>
using namespace std;
#define int long long
int n,m,s;
vector<int> weight,value,l,r;
vector<int> countPrefix,valuePrefix;

__int128 calculate(int w){
    countPrefix[0] = valuePrefix[0] = 0;
    for(int i=1;i<=n;i++){
        countPrefix[i] = countPrefix[i-1] + (weight[i]>=w);
        valuePrefix[i] = valuePrefix[i-1] + (weight[i]>=w ? value[i] : 0);
    }
    // 单个区间的检验值能用 long long 保存，但所有区间的总和可能溢出。
    __int128 y = 0;
    for(int i=0;i<m;i++){
        int count = countPrefix[r[i]] - countPrefix[l[i]-1];
        int sum = valuePrefix[r[i]] - valuePrefix[l[i]-1];
        y += (__int128)count * sum;
    }
    return y;
}
signed main(void){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cin>>n>>m>>s;
    // 读入 n、m 后再分配空间；矿石下标从 1 开始，方便计算区间前缀和。
    weight.resize(n+1);
    value.resize(n+1);
    l.resize(m);
    r.resize(m);
    countPrefix.resize(n+1);
    valuePrefix.resize(n+1);
    int left = LLONG_MAX;
    int right = 0;
    for(int i=1;i<=n;i++){
        cin>>weight[i]>>value[i];
        left = min(left,weight[i]);
        right = max(right,weight[i]);
    }
    for(int i=0;i<m;i++){
        cin>>l[i]>>r[i];
    }
    right++; // W 大于最大重量时，所有矿石都不选，y=0。
    // W 越大，y 越小：寻找第一个满足 y<=s 的 W（前面为 0，后面为 1）。
    while(left<right){
        int mid = left + (right-left)/2;
        if(calculate(mid)<=s){
            right = mid;
        }else{
            left = mid+1;
        }
    }
    // 最优值在分界点两侧；若 left 已是最小重量，left-1 仍是全选。
    __int128 answer = s-calculate(left);
    __int128 difference = calculate(left-1)-s;
    if(difference<0) difference = -difference;
    answer = min(answer,difference);
    // 全不选时差值为 s，因此最终答案一定能用 long long 保存。
    cout<<(long long)answer<<'\n';
    return 0;
}   
