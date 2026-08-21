/* 题目描述
? 给定一个矩阵，在其中找一个子矩阵，使得子矩阵中所有元素的和加在一起最大。

输入
? 第一行输入一个整数 N 表示矩阵的大小为 N?N。

? 接下来 N 行，每行 N 个数，表示矩阵中的元素的值 C。（?128≤C≤127）

输出
? 输出一个整数，表示最大子阵和。

样例输入
4
0 -2 -7 0
9 2 -6 2
-4 1 -4 1
-1 8 0 -2
样例输出
15 */

#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;
#define MAX_N 100
vector<vector<int>> arr(MAX_N+5,vector<int>(MAX_N+5,0));
int main(void){
    int n;
    cin>>n;
    for(int i=1;i<=n;i++){
        for(int j=1;j<=n;j++){
            cin>>arr[i][j];
            arr[i][j] += arr[i-1][j];
        }
    }
    int ans = INT_MIN;
    //枚举子矩阵的起始行号和终止行号
    for(int i=1;i<=n;i++){
        for(int j=i;j<=n;j++){
            int s = 0;
            for(int k=1;k<=n;k++){
                //得到这一个区间内第k列的值
                int a = arr[j][k] - arr[i-1][k];
                if(s>=0) s+=a;
                else s = a;
                ans = max(ans,s);
            }
        }
    }

    cout<<ans<<endl;
    //system("pause");
    return 0;
}