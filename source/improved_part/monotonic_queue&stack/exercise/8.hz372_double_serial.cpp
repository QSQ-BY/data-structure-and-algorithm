/* 题目描述
? u，v 两个序列趋势相同，当且仅当对于任意 l 和 r，
均有 RMQ(u,l,r)=RMQ(v,l,r) (1≤l≤r≤n)，
? 其中 n 是序列长度，RMQ(u,l,r) 
是 u 序列从 l 到 r 中的最小值（有可能有多个最小值）的最大下标。
? 现有两个序列 A={a1,a2,a3,…,an}，B={b1,b2,b3,…,bn} 两个序列
? 请求出最大的 p，使得A‘={a1,a2,a3,…,ap} 
与B‘={b1,b2,b3,…,bp} 趋势相同。
输入
? 第一行输入一个整数 n(1≤n≤500000)，代表 A、B 序列长度。
? 接下来两行，每行 n 个正整数，分别代表两个序列相应位置的值。
? 序列中数字大小均在 int32 范围内。
输出
? 输出一个整数，代表满足题意的最大 p 值。
样例输入
5
3 1 5 2 4
5 2 4 3 1
样例输出
4 */
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <unordered_map>
#include <unordered_set>
#include <stack>
#include <queue>
#include <deque>
#include <climits>

using namespace std;

void test01(){
    int n = 0;
    cin>>n;
    vector<int> a(n);
    vector<int> b(n);
    for(int i=0;i<n;i++){
        scanf("%d",&a[i]);
    }
    for(int i=0;i<n;i++){
        scanf("%d",&b[i]);
    }
    deque<int> qa;
    deque<int> qb;
    int p = 0;
    for(int i=0;i<n;i++){
        while(!qa.empty() and a[qa.back()] >= a[i]) qa.pop_back();
        while(!qb.empty() and b[qb.back()] >= b[i]) qb.pop_back();
        qa.push_back(i);
        qb.push_back(i);
        p=i;
        if(qa.size() != qb.size()) break;
    }
    cout<<p<<endl;
    return;
}

int main(void){
    test01();
    //system("pause");
    return 0;
}