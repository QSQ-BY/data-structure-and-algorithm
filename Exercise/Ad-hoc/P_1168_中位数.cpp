/* 题目描述
给定一个长度为 N 的非负整数序列 A，对于前奇数项求中位数。

输入格式
第一行一个正整数 N。

第二行 N 个正整数 A 
1…N
​
 。

输出格式
共 ⌊ 
2
N+1
​
 ⌋ 行，第 i 行为 A 
1…2i−1
​
  的中位数。

输入输出样例
输入 #1复制

7
1 3 5 7 9 11 6
输出 #1复制

1
3
5
6
输入 #2复制

7
3 1 5 9 8 7 6
输出 #2复制

3
3
5
6
说明/提示
对于 20% 的数据，N≤100；

对于 40% 的数据，N≤3000；

对于 100% 的数据，1≤N≤10 
5
 ，0≤A 
i
​
 ≤10 
9
 。 */

#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    //默认大顶堆
    priority_queue<int> left;
    //创建小顶堆
    priority_queue<int, vector<int>, greater<int>> right;

    for (int i = 1; i <= n; i++) {
        int x;
        cin >> x;

        if (left.empty() || x <= left.top()) {
            left.push(x);
        } else {
            right.push(x);
        }

        // 调整两个堆的大小
        while(left.size() > right.size() + 1) {
            right.push(left.top());//.top()函数取出堆顶元素
            left.pop();
        } 
        while(right.size() > left.size()) {
            left.push(right.top());
            right.pop();
        }

        // 奇数长度前缀的中位数
        if (i % 2 == 1) {
            cout << left.top() << '\n';
        }
    }

    return 0;
}
