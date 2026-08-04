/* 题目描述
定义三元组（a,b, c）（a,b,c 均为正数）的距离 D=|a-b|+|b-c|+|c-a|。
给定 3 个非空整数集合 S1, S2 ,S3, 
按升序分别存储在 3 个数组中。请设计一个尽可能高效的算法，
计算并输出所有可能的三元组（a, b, c）（a∈S1,b∈S2,c∈S3）中的最小距离。
例如 S1={-1, 0, 9}, S2={-25，-10，10，11}，S3={2，9，17，30，41}，
则最小距离为 2，相应的三元组为（9，10，9）。

程序中的主要部分已经帮你写好了，你只需要将如下代码拷贝到你的环境中，
并且补充 func函数功能即可。函数功能描述如下：

输入参数
输入三个参数，分别为存储三个非空集合的队列

返回值说明
返回一个整形值，表示所有可能的三元组（a, b, c）
（a∈S1,b∈S2,c∈S3）中的最小距离 */


//2020数据结构考研第41题
/* 思路分析：
理解D=|a-b|+|b-c|+|c-a|,__a__________b________________c______

a,b,c就是数轴上的三个点，D就等于两倍的abc之间的最大差值
要使得D最小就要让a\b\c之间最小值和最大值的差值尽可能小
三个集合都是按照从小到大进行排列的，
移动数轴中间的点，D要不然就是不变要不然就是变大
移动最右边的点，D一定变大，
移动最左边的点D有可能变小，有可能变大也有可能不变，最有可能的就是变小
所以想让D变小就移动最左边的点，就是选定相应集合中的下一个数字
一句话策略：不断移动最左边的点就可以解决这道题 */

#include <iostream>
#include <cstdlib>
#include <queue>
#include <climits>
using namespace std;

int min_num(int a, int b, int c) {
    if (a > b) swap(a, b);
    if (a > c) swap(a, c);
    return a;
}

int func(queue<int> que1, queue<int> que2, queue<int> que3) {
    int ans = INT_MAX;
    int temp_ans = INT_MAX;//暂存当前循环计算的值
    int cur_min{0};//寻找当前循环中的最小值
    while(!que1.empty() and !que2.empty() and !que3.empty()){
        int a = que1.front();
        int b = que2.front();
        int c = que3.front();
        temp_ans = abs(a-b) + abs(a-c) + abs(b-c);
        if(temp_ans<=ans) ans = temp_ans;
        cur_min = min_num(a,b,c);
        if(cur_min == a) que1.pop();
        else if(cur_min == b) que2.pop();
        else if(cur_min == c) que3.pop();
    } 

    return ans;
}

int main() {
    int m, n, k, x;
    queue<int> que1, que2, que3;
    cin >> m >> n >> k;
    for (int i = 0; i < m; i++) {
        cin >> x;
        que1.push(x);
    }
    for (int i = 0; i < n; i++) {
        cin >> x;
        que2.push(x);
    }
    for (int i = 0; i < k; i++) {
        cin >> x;
        que3.push(x);
    }
    cout << func(que1, que2, que3) << endl;
    return 0;
}