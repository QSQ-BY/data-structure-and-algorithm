/* 题目描述
? 给定从左到右多个矩形，已知这此矩形的宽度都为 1，
长度不完全相等。这些矩形相连排成一排，
求在这些矩形包括的范围内能得到的面积最大的矩形，
打印出该面积。所求矩形可以横跨多个矩形，
但不能超出原有矩形所确定的范围。
输入
? 输入共两行，第一个数表示矩形的个数 N。
接下来 N 个数表示矩形的大小。（1≤N≤100000）
输出
? 输出最大矩形面积。
样例输入
7
2 1 4 5 1 3 3
样例输出
8 */
//矩形的高一定为某一个木板的高，
//最左边和最右边的木板一定是最近的小于当前木板的木板->单调栈
//遍历每一块木板把他当作最高的木板
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
//数据的读入
    long long n=0;
    cin>>n;
    vector<long long> height;
    height.push_back(-1);
    for(long long i=0;i<n;i++){
        long long number;
        cin>>number;
        height.push_back(number);
    }
    height.push_back(-1);

//构造单调栈
    vector<long long> l(n+2,0);//左边第一个小于第i个元素的元素下标
    vector<long long> r(n+2,0);//右边第一个小于第i个元素的元素下标
    stack<long long> s;
    for(long long i=1;i<n+2;i++){
        while(!s.empty() and height[i] < height[s.top()]){
            r[s.top()] = i;
            s.pop();
        }
        s.push(i);
    }
    while(!s.empty()) s.pop();
    for(long long i = n;i>=0;i--){
        while(!s.empty() and height[s.top()] > height[i]){
            l[s.top()] = i;
            s.pop();
        }
        s.push(i);
    }

//求解答案
    long long ans = 0;
    for(long long i=1;i<=n;i++){
        long long cur_height = height[i];
        long long cur_width = r[i] - l[i] -1;
        long long temp_ans = cur_height*cur_width;
        ans = max(ans,temp_ans);
    }
    cout<<ans<<endl;

    return;
}

int main(void){
    test01();
    //system("pause");
    return 0;
}
