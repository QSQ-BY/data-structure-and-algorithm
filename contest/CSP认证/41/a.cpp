/* 时间限制： 1.0 秒

空间限制： 512 MiB

相关文件： 题目目录

题目描述
小 P 在学习了位运算后，定义了如下“平衡数”：

对于一个正整数 
a
a，如果其二进制表示中 1 和 0 的个数相等，则称其为平衡数。
这里的二进制表示以 1 为最高位，即不考虑更高位用于补位的 0。例如，正整数 
12
12 的二进制表示为 1100，包含两个 1 和两个 0。在实际存储中，更高位可能需要填 0 补位，如 00001100，在本题中无需考虑此种情况。

小 P 已经生成好了 
n
n 个正整数 
a
1
,
a
2
,
⋯
,
a
n
a 
1
​
 ,a 
2
​
 ,⋯,a 
n
​
 ，试编程统计里面有多少个平衡数。

输入格式
从标准输入读入数据。

输入的第一行包含一个正整数 
n
n，第二行包含空格分隔的 
n
n 个正整数 
a
1
,
a
2
,
⋯
,
a
n
a 
1
​
 ,a 
2
​
 ,⋯,a 
n
​
 。

输出格式
输出到标准输出。

输出一个整数，表示 
a
1
,
a
2
,
⋯
,
a
n
a 
1
​
 ,a 
2
​
 ,⋯,a 
n
​
  中平衡数的个数。

样例输入
3
2 5 9
样例输出
2
样例解释
2
2 的二进制表示为 10，是平衡数；

5
5 的二进制表示为 101，不是平衡数；

9
9 的二进制表示为 1001，是平衡数。

子任务
50
%
50% 的测试点满足：
0
<
a
i
≤
256
0<a 
i
​
 ≤256；

全部的测试点满足：
0
<
n
≤
100
0<n≤100 且 
0
<
a
i
≤
1
0
9
0<a 
i
​
 ≤10 
9
 。 */
#include <iostream>
using namespace std;

bool is_balanced(long long number){
  long long cnt1 = 0;
  for(long long temp = number;temp != 0;temp -= (-temp & temp)){
    cnt1 ++;
  }
  long long total = 0;
  for (long long temp = number; temp > 0; temp >>= 1) {
      total++;
  }
  return total == 2*cnt1;
}

int main(void){
  long long n;
  cin>>n;
  long long ans = 0;
  for(long long i=0;i<n;i++){
    long long number;
    cin>>number;
    if(is_balanced(number)){
      ans += 1;
    }
  }
  cout<<ans<<endl;
  //system("pause");
}