/* 题目描述
? 地图 x 轴的上方为海，下方为陆地，海中有 n 个小岛，坐标分别为 (Xi,Yi)。有一种雷达，能探测到的范围为以 d 为半径的圆。问海岸线上至少造多少雷达可以把所有的小岛都处在探测范围内。注意雷达是建在海岸线上的，也就是x轴上的。
输入
? 第一行输入两个数 n,d。（1≤n≤1000）

? 接下来 n 行，每行两个数代表小岛的坐标。（?1000≤Xi,Yi≤1000）

输出
? 输出一个数表示答案，无解时输出 ?1。

样例输入
3 2
1 2
-3 1
2 1
样例输出
2 */

#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>
#include <cmath>
using namespace std;
typedef pair<double,double> PII;
int n;
double d;
vector<PII> arr;

bool cmp(const PII &a, const PII &b) {
    return a.second < b.second;
}
int main(void){
    cin>>n>>d;
    for(int i=0;i<n;i++){
        double x;
        double y;
        cin>>x>>y;
        if(y>d){
            cout<<-1<<endl;
            return 0;
        }
        double left = x - sqrt(d*d - y*y);
        double right = x+ sqrt(d*d - y*y);
        arr.push_back(PII(left,right));
    }
    sort(arr.begin(),arr.end(),cmp);
    int ans = 1;
    double pos = arr[0].second;
    for(int i=0;i<n;i++){
        if(pos < arr[i].first){
            ans++;
            pos = arr[i].second;
        }
    }
    cout<<ans<<endl;
    //system("pause");
    return 0;
}