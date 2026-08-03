/* 题目描述
? 一些士兵站在矩阵的一些方格内，现要把他们移动到一横排，
并连续地排成一队，士兵一次可以选择四个方向中的一个方向移动一格，
求最少需要移动多少步才能完成要求。

? 即所有士兵的y坐标相同并且x坐标相邻。
输入
? 第一行输入一个正整数 n，表示士兵的数量。（1≤n≤10000）
? 接下来 n 行，每行两个数，
代表第 i 个士兵所处位置的横纵坐标 Xi,Yi。
（?10000≤Xi,Yi≤10000）
输出
? 输出最少移动步数。
样例输入
5
1 2
2 2
1 3
3 -2
3 3
样例输出
8 */

#include <iostream>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;

///求解cost x = |((xi - i) - X)|的最小值
//xi' = xi - i
//cost y = |yi - Y|
void test01(){
    int n = 0;
    cin>>n;
    vector<int> x(n),y(n);
    for(int i=0;i<n;i++){
        cin>>x[i]>>y[i];
    }
    int X = 0;
    int Y = 0;
    sort(y.begin(),y.end());
    Y = y[n/2];
    int costY = 0;
    for(int i=0;i<n;i++){
        costY += abs(y[i]-Y);
    }

    sort(x.begin(),x.end());
    vector<int> x_(n);
    for(int i=0;i<n;i++) x_[i] = x[i]-i;
    sort(x_.begin(),x_.end());
    X = x_[n/2];
    int costX = 0;
    for(int i=0;i<n;i++){
        costX += abs(x_[i]-X);
    }

    int ans = costX + costY;
    cout<<ans;
    return;
}

int main(void){
    test01();
    system("pause");
    return 0;
}