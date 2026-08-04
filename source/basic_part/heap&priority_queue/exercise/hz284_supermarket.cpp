/* 题目描述
? 超市里有N个商品. 
第i个商品必须在保质期(第di天)之前卖掉, 
若卖掉可让超市获得pi的利润.
? 每天只能卖一个商品.
? 现在你要让超市获得最大的利润.
输入
? 每组数据第一行为一个整数N(0<N≤10000), 
即超市的商品数目
? 之后N行，每行各有两个整数, 
第i行为pi,di(1<=pi,di<=10000)
输出
? 输出当前条件下超市的最大利润.
输入样例1
7
20 1 
2 1 
10 3 
100 2 
8 2 
5 20 
50 10
输出样例1
185 */

#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
using namespace std;

typedef pair<int, int> PII;

void test01(){
    int n;

    while(cin >> n){
        vector<PII> arr; // first = d, second = p

        for(int i = 0, p, d; i < n; i++){
            cin >> p >> d;
            arr.push_back(PII(d, p));
        }

        sort(arr.begin(), arr.end());

        set<PII> s; // first = p, second = 编号，用来区分利润相同的商品
        int tot = 0;

        for(int i = 0; i < n; i++){
            int d = arr[i].first;
            int p = arr[i].second;

            if(d > s.size()){
                s.insert(PII(p, tot++));
            }else{
                if(p > s.begin()->first){
                    s.erase(s.begin());
                    s.insert(PII(p, tot++));
                }
            }
        }

        int ans = 0;
        for(auto x : s){
            ans += x.first;
        }

        cout << ans << endl;
    }
}

int main(void){
    test01();
    system("pause");
    return 0;
}