/* 题目描述
给出正整数 n，要求按如下方式构造数列：

只有一个数 n 的数列是一个合法的数列。
在一个合法的数列的末尾加入一个正整数，但是这个正整数不能超过该数列最后一项的一半，可以得到一个新的合法数列。
请你求出，一共有多少个合法的数列。两个合法数列 a,b 不同当且仅当两数列长度不同或存在一个正整数 i≤∣a∣，使得 a 
i
?
 
?
=b 
i
?
 。

输入格式
输入只有一行一个整数，表示 n。

输出格式
输出一行一个整数，表示合法的数列个数。

输入输出样例
输入 #1复制

6
输出 #1复制

6
说明/提示
样例 1 解释
满足条件的数列为：

6
6,1
6,2
6,3
6,2,1
6,3,1 */
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
#include <cmath>

using namespace std;
//f[i]代表以i作为开头的合法的数列的数量
/* 1.以i作为结尾的序列，不在拓展的序列的数量->一种
2.继续向外拓展的数量->f[i/2]+f[i/2-1]+......+f[1]
f[i] = 1+f[i/2]+f[i/2-1]+......+f[1] */
#define MAX_N 1000
vector<int> f(MAX_N+5,0);
void test01(){
    int n;
    cin>>n;
    f[0] = 0;
    f[1] = 1;
    f[2] = 2;
    for(int i=3;i<=n;i++){
        f[i] = 1;
        for(int j=1;j<=i/2;j++){
            f[i] += f[j];
        }
    }
    cout<<f[n]<<endl;
    return;
}

int main(void){
    test01();
    //system("pause");
    return 0;
}