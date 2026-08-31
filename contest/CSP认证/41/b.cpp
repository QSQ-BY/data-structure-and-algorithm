/* 时间限制： 1.0 秒

空间限制： 512 MiB

相关文件： 题目目录

题目描述
小 P 计划招募 
n
n 个机器人完成一个项目：每个机器人负责其中的一项任务，编号从 
1
1 到 
n
n，任务之间互不干扰。如果完成任务 
i
i 的耗时为 
t
i
t 
i
​
 ，则该项目总耗时为 
t
1
+
t
2
+
⋯
+
t
n
t 
1
​
 +t 
2
​
 +⋯+t 
n
​
 。

作为项目管理者，小 P 可以用有限的预算为机器人们购买咖啡加油。其中负责任务 
i
i 的机器人，最多可以喝 
a
i
a 
i
​
  杯咖啡，从而将该任务耗时缩短 
b
i
b 
i
​
 （最终耗时即为 
t
i
−
b
i
t 
i
​
 −b 
i
​
 ）。

根据任务的特性和机器人的偏好，
n
n 项任务可分为“灵活型”和“普通型”两类，详情参见附件资料（重要）。

附件资料
已知小 P 可以为机器人们提供最多 
m
m 杯咖啡，试计算完成整个项目的最短时间。

输入格式
从标准输入读入数据。

输入的第一行包含空格分隔的两个正整数 
n
n 和 
m
m，分别表示任务数量和咖啡数量。

接下来 
n
n 行，每行包含空格分隔的四个整数 
o
i
o 
i
​
 、
t
i
t 
i
​
 、
a
i
a 
i
​
  和 
b
i
b 
i
​
 ，表示一个任务。其中 
o
i
∈
{
0
,
1
}
o 
i
​
 ∈{0,1} 表示任务类别，
o
i
=
0
o 
i
​
 =0 表示灵活型、
o
i
=
1
o 
i
​
 =1 表示普通型；其余变量含义如上所述，输入数据保证 
t
i
>
b
i
t 
i
​
 >b 
i
​
 ，即缩短后的耗时仍大于零。

输出格式
输出到标准输出。

输出一个实数，表示完成整个项目的最短时间。

样例1输入
3 5
0 2 3 1
0 3 4 2
0 4 5 2
样例1输出
6.6
样例1解释
三个任务均为灵活型，初始总耗时为 
2
+
3
+
4
=
9
2+3+4=9。最优方案为：给任务二分配 
4
4 杯咖啡，耗时缩短 
2
2；给任务三分配 
1
1 杯咖啡，耗时相应缩短 
2
5
=
0.4
5
2
​
 =0.4。综上，完成整个项目最短时间为 
9
−
2
−
0.4
=
6.6
9−2−0.4=6.6。

样例2输入
5 62
0 10 2 1
0 10 1 1
1 500 40 360
1 600 50 500
1 400 20 150
样例2输出
1008.5
样例2解释
初始总耗时为 
1520
1520。最优方案为：给任务三分配 
40
40 杯咖啡，耗时缩短 
360
360；给任务五分配 
20
20 杯咖啡，耗时缩短 
150
150；给任务一和二各分配 
1
1 杯咖啡，耗时分别缩短 
0.5
0.5 和 
1
1。综上，完成整个项目最短时间为 
1520
−
360
−
150
−
0.5
−
1
=
1008.5
1520−360−150−0.5−1=1008.5。 */
#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip>
using namespace std;

int main(void){
    int n;
    int m;
    cin>>n>>m;//任务数量和咖啡数量
    //机器人型号（0为灵活型1为普通型），初始总耗时，能提供的总数量，咖啡能减少的时间
    vector<vector<int>> mission(n,vector<int>(4));
    long long sum = 0;
    for(int i=0;i<n;i++){
        for(int j=0;j<4;j++){
            cin>>mission[i][j];
        }
        sum += mission[i][1];
    }

    vector<double> dp(m+1,0);
    for(int i=0;i<n;i++){
        int coffee = mission[i][2];
        int saved_time = mission[i][3];
        if(mission[i][0] == 1){
            //普通型任务只能选择不分配，或者一次分配 coffee 杯咖啡
            for(int j=m;j>=coffee;j--){
                dp[j] = max(dp[j],dp[j-coffee]+saved_time);
            }
        }else{
            //灵活型任务拆成 coffee 个重量为 1 的物品
            double saved_per_coffee = static_cast<double>(saved_time)/coffee;
            for(int k=0;k<coffee;k++){
                for(int j=m;j>=1;j--){
                    dp[j] = max(dp[j],dp[j-1]+saved_per_coffee);
                }
            }
        }
    }
    cout<<fixed<<setprecision(6)<<sum-dp[m]<<'\n';
    return 0;
}
