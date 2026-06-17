/* 题目描述
? 给出一个 n?m 的矩阵，每行取一个元素，
组成一个包含 n 个元素的序列，一共有 m的n次方 种序列，
求出序列和最小的前 m 个序列的序列和。
输入
? 输入两个整数 n,m，接下来输入矩阵。
输出
? 输出最小的前 m 个序列的序列和。
每两个数之间用空格隔开。
样例输入
2 3
1 2 3
2 2 3
样例输出
3 3 4 */
//序列m小和
#include <iostream>
#include <vector>
#include <set>
#include <string>
#include <algorithm>
using namespace std;

typedef pair<int,int> PII;

int main(void){
    int n=0;
    int m=0;
    cin>>n>>m;
    int tot = 0;
    set<PII> s;
    
    s.insert(PII(0,tot++));
    for(int i=0;i<n;i++){
        vector<int> temp;
        for(auto x:s){
            temp.push_back(x.first);
        }
        s.clear();
        for(int j=0,a;j<m;j++){
            cin>>a;
            for(auto x:temp){
                if(s.size()<m or s.begin()->first < x-a){
                    s.insert(PII(x-a,tot++));
                    if(s.size()>m){
                        s.erase(s.begin());
                    }
                }
            }
        }
    }

    int flag = 0;
    for(auto iter = s.rbegin();iter != s.rend();iter++){
        if(flag == 1) cout<<" ";
        cout<<-iter->first;
        flag = 1;
    }
    system("pause");
    return 0;
}
