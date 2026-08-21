/* Problem Statement  问题描述
There is a charger with an unlimited number of charging slots. At time 
0, all slots are empty.
有一个充电器，拥有无限数量的充电插槽。在时间点 
0 时，所有插槽都是空的。

The maximum capacity of a battery is 
V. While a battery is plugged into a slot, it is charged at a rate of 
1 until its charge level reaches the maximum capacity (that is, the charge level increases by 
1 for every 
1 unit of time that passes).
电池的最大容量为 
V 。当电池插入充电接口后，它会以 
1 的速率进行充电，直到其充电水平达到最大容量为止。也就是说，每过 
1 单位时间，电池的充电水平就会增加 
1 。

Process 
Q queries in order. The 
q-th query is given in one of the following formats. Here, it is guaranteed that 
t 
1
?
 <?<t 
Q
?
 .
按顺序处理 
Q 个查询。第 
q 个查询以以下格式之一给出。此处保证有 
t 
1
?
 <?<t 
Q
?
  个查询。

Type 
1 (
1 t 
q
?
  w 
q
?
 ): At time 
t 
q
?
 , plug one battery with charge level 
w 
q
?
  into a slot.
输入 
1 ( 
1 t 
q
?
  w 
q
?
  )：在 
t 
q
?
  时刻，将电量水平为 
w 
q
?
  的电池插入相应的插槽中。
Type 
2 (
2 t 
q
?
 ): At time 
t 
q
?
 , unplug one battery with the highest charge level from its slot, and output that battery's charge level. If there is no battery plugged into any slot, output 
?1 instead.
输入 
2 ( 
2 t 
q
?
  )：在 
t 
q
?
  时刻，将电量最高的电池从插槽中取出，并输出该电池的电量值。如果所有插槽中都没有电池，则输出 
?1 。
Constraints  约束
1≤Q≤3×10 
5
 
1≤V≤10 
9
 
For type 
1 queries, 
1≤t 
q
?
 ≤10 
9
 .
对于类型为 
1 的查询，执行 
1≤t 
q
?
 ≤10 
9
  操作。
For type 
1 queries, 
0≤w 
q
?
 ≤V.
对于类型为 
1 的查询，执行 
0≤w 
q
?
 ≤V 操作。
For type 
2 queries, 
1≤t 
q
?
 ≤10 
9
 .
对于类型为 
2 的查询，执行 
1≤t 
q
?
 ≤10 
9
  操作。
t 
1
?
 <?<t 
Q
?
 
The input values are all integers.
所有输入值均为整数。
Input  输入
The input is given from Standard Input in the following format:
输入从标准输入以以下格式给出：

Q 
V
query 
1
?
 
?
query 
Q
?
 
Here, 
query 
q
?
  represents the 
q-th query, and is given in one of the following two formats:
在这里， 
query 
q
?
  表示第 
q 条查询结果，其格式有两种可能：

1 
t 
q
?
  
w 
q
?
 
2 
t 
q
?
 
Output  输出结果
Let 
x be the number of type 
2 queries. Output 
x lines.
令 
x 表示类型为 
2 的查询数量。输出 
x 行内容。

The 
k-th line (
1≤k≤x) should contain the value to be outputed for the 
k-th type 
2 query.
第 
k 行（ 
1≤k≤x ）应包含针对第 
k 种类型 
2 查询而需要输出的数值。

Sample Input 1  示例输入 1 复制
Copy  副本
7 100
1 15 60
1 25 80
2 30
1 45 0
2 60
2 70
2 80
Sample Output 1  示例输出 1 复制
Copy  副本
85
100
25
-1
The seven queries are processed in the following order.
这七个查询是按照以下顺序来处理的。

At time 
15, a battery with charge level 
60 is plugged in. At this point, the charger has a battery with charge level 
60.
在时间点 
15 时，电量水平为 
60 的电池被接入了充电设备。此时，充电设备所连接的电池的电量水平为 
60 。
At time 
25, a battery with charge level 
80 is plugged in. At this point, the charger has batteries with charge levels 
70,80.
在时间点 
25 时，一块充电水平为 
80 的电池被接入了充电设备。此时，充电设备中还有充电水平为 
70,80 的电池正在充电中。
At time 
30, the charger has batteries with charge levels 
75,85. Of these, the battery with charge level 
85 is unplugged.
在时间 
30 时，充电器所连接的电池的充电状态分别为 
75,85 。其中，充电状态为 
85 的电池此时处于未连接状态。
At time 
45, a battery with charge level 
0 is plugged in. At this point, the charger has batteries with charge levels 
0,90.
在时间点 
45 时，一块充电水平为 
0 的电池被接入了充电设备。此时，充电设备中还有充电水平为 
0,90 的电池正在充电中。
At time 
60, the charger has batteries with charge levels 
15,100. Of these, the battery with charge level 
100 is unplugged.
在时间 
60 时，充电器所连接的电池的充电状态分别为 
15,100 。其中，充电状态为 
100 的电池此时处于未连接状态。
At time 
70, the charger has a battery with charge level 
25. This battery, with charge level 
25, is unplugged.
在时间 
70 时，充电器所连接的电池的充电水平为 
25 。而另一块充电水平为 
25 的电池则处于未连接充电器的状态。
At time 
80, no battery is plugged into the charger. Thus, no battery is unplugged.
在时间 
80 时，没有电池被插入充电器。因此，也没有电池从充电器上被拔下。 */

#include <iostream>
#include <set>
#include <algorithm>

using namespace std;

void solve() {
    // 优化标准输入输出流，防止大数据量 IO 超时
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int q;
    long long vmax;
    if (!(cin >> q >> vmax)) return;

    // 使用 multiset + greater<long long> 维护降序集合
    // 容器首元素 (*s.begin()) 即为最大值
    multiset<long long, greater<long long>> s;

    for (int i = 0; i < q; ++i) {
        int scode;
        cin >> scode;
        if (scode == 1) {
            long long t, w;
            cin >> t >> w;
            // 插入电池基准值 key = w - t
            // 时间复杂度：O(log N)
            s.insert(w - t);
        } else if (scode == 2) {
            long long t;
            cin >> t;
            if (s.empty()) {
                cout << -1 << "\n";
            } else {
                // 获取当前最大 key 值（堆顶）
                long long max_key = *s.begin();
                
                // 删除堆顶元素（注意：用迭代器删除，防止删除所有重复值）
                // 时间复杂度：O(log N)
                s.erase(s.begin());

                // 计算该电池在时刻 t 的实时电量，上限为 vmax
                long long ans = min(vmax, max_key + t);
                cout << ans << "\n";
            }
        }
    }
}

int main() {
    solve();
    return 0;
}