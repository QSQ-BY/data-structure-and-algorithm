/* 题目描述
给定 A、B、C 三根足够长的细柱，在 A 柱上放有 2n 个中间有孔的圆盘，共有 n 个不同的尺寸，每个尺寸都有两个相同的圆盘，注意这两个圆盘是不加区分的（下图为 n=3 的情形）。



现要将这些圆盘移到 C 柱上，在移动过程中可放在 B 柱上暂存。要求：

每次只能移动一个圆盘；
A、B、C 三根细柱上的圆盘都要保持上小下大的顺序。
任务：设 A 
n
?
  为 2n 个圆盘完成上述任务所需的最少移动次数，对于输入的 n，输出 A 
n
?
 。

输入格式
一个正整数 n，表示在 A 柱上放有 2n 个圆盘。

输出格式
一个正整数, 为完成上述任务所需的最少移动次数 A 
n
?
 。

输入输出样例
输入 #1复制

1
输出 #1复制

2
输入 #2复制

2
输出 #2复制

6 */
#include <iostream>
#include <string>

using namespace std;

void test01(){
    int n;
    cin >> n;
    string f = "0";
    for(int i = 1; i <= n; i++){
        int carry = 2;  // 对应递推式中的 +2
        // 高精度计算：f = 2 * f + 2
        for(int j = static_cast<int>(f.size()) - 1; j >= 0; j--){
            int value = (f[j] - '0') * 2 + carry;
            f[j] = static_cast<char>('0' + value % 10);
            carry = value / 10;
        }
        if(carry > 0){
            f.insert(f.begin(), static_cast<char>('0' + carry));
        }
    }

    cout << f << endl;
}

int main(){
    test01();
    return 0;
}