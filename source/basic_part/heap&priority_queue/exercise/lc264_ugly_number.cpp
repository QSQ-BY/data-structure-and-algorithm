/* 给你一个整数 n ，请你找出并返回第 n 个 丑数 。
丑数 就是质因子只包含 2、3 和 5 的正整数。
示例 1：
输入：n = 10
输出：12
解释：[1, 2, 3, 4, 5, 6, 8, 9, 10, 12] 
是由前 10 个丑数组成的序列。
示例 2：
输入：n = 1
输出：1
解释：1 通常被视为丑数 */

#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
using namespace std;
class Solution{
public:
    int nthUglyNumber(int n) {
        set<long long> s;
        s.insert(1);
        int cnt = 0;
        while(1){
            for(auto x:s){
                s.insert(x*2);
                s.insert(x*3);
                s.insert(x*5);
                cnt++;
                if(cnt == n){
                    return *s.begin();
                }
                s.erase(s.begin());
            }
        }
    }

    int nthUglyNumber2(int n){
        set<long long> s;
        s.insert(1);
        long long ans = 0;
        int flag=0;
        while(n--){
            ans = *s.begin();
            s.erase(s.begin());
            s.insert(ans*5);
            s.insert(ans*2);
            s.insert(ans*3);
        }
        return ans;
    }
};



void test01(){
    Solution s;
}

int main(void){
    test01();
    system("pause");
    return 0;
}