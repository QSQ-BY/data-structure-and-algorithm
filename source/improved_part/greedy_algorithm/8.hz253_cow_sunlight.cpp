/* 题目描述
? 有 C 头奶牛去晒太阳，每头奶牛各自能够忍受的阳光强度有一个最小值和一个最大值，太大就晒伤了，太小奶牛没感觉。而刚开始的阳光的强度非常大，奶牛都承受不住，奶牛得涂抹防晒霜，防晒霜的作用是让阳光照在身上的阳光强度固定为某个值。那么为了不让奶牛烫伤，又不会没有效果。给出了 L 种防晒霜固定的阳光强度和数量，每头奶牛只能抹一瓶防晒霜，求能够享受晒太阳的奶牛最多有几头。

输入
? 第一行输入两个数 C,L。（1≤C,L≤2500）

? 接下来 C 行，每行两个数表示每头奶牛能接受的阳光强度的最小值和最大值。（均小于 1000）

? 再接下来 L 行，每行两个数表示每种防晒霜固定的阳光强度和数量。（均小于 1000）

输出
? 输出能晒太阳的奶牛的最多数量。

样例输入
3 2
3 10
2 5
1 5
6 2
4 1 */
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
typedef pair<int,int> PII;

bool cmp(const PII& a,const PII& b ){
    return a.second < b.second;
}

int main(void){
    int c;
    int l;
    cin>>c>>l;
    vector<PII> cow(c);
    for(int i=0;i<c;i++){
        int l;
        int r;
        cin>>l>>r;
        cow[i] = PII(l,r);
    }
    sort(cow.begin(),cow.end(),cmp);

    vector<PII> sun(l);
    for(int i=0;i<l;i++){
        int num;
        int cnt;
        cin>>num>>cnt;
        sun[i] = PII(num,cnt);
    }
    sort(sun.begin(),sun.end());
    int ans = 0;
    for(int i=0;i<c;i++){
        for(int j=0;j<l;j++){
            if(sun[j].second == 0) continue;
            int num = sun[j].first;
            int l = cow[i].first;
            int r = cow[i].second;
            if(num>=l and num<=r){
                sun[j].second--;
                ans++;
                break;
            }
        }
    }
    cout<<ans<<endl;
    //system("pause");
    return 0;
}