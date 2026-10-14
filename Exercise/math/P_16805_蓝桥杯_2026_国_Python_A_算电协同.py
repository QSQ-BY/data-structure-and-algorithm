""" 题目描述
2026 年，“算电协同”首次写入政府工作报告，与超大规模智算集群一同被列为国家级新基建工程，支撑全国一体化算力调度体系建设。在工程实施中，国家算力枢纽节点需要实时管理大量算力单元。

每个算力单元都有一个非负整数形式的能效值 v。为了优化能源调度，调度系统需要统计满足“协同条件”的单元对数量。定义两个算力单元 (i,j) 为一组协同单元对，当且仅当：

i<j;
Fib(v 
i
​
 +v 
j
​
 )=Fib(v 
i
​
 )+Fib(v 
j
​
 )。
其中 Fib(x) 表示第 x 个斐波那契数。斐波那契数列的计算规则如下：

Fib(0)=0;
Fib(1)=1;
对于 x≥2, Fib(x)=Fib(x−1)+Fib(x−2)。
现在，你需要维护一个初始为空的算力单元池，并处理 q 次操作：

1 k v: 增加 k 个能效值为 v 的算力单元。
2 k v: 减少最多 k 个能效值为 v 的算力单元。如果当前能效值为 v 的单元不足 k 个，则全部移除。
3: 查询当前共有多少组协同单元对。
对此，请你编写程序模拟该调度系统的运行，并针对每次查询给出对应结果。

输入格式
第一行包含一个正整数 q，表示操作次数。 接下来的 q 行，每行描述一个操作：

1 k v: 增加 k 个能效值为 v 的单元。
2 k v: 减少最多 k 个能效值为 v 的单元。
3: 查询当前协同单元对总数。
输出格式
对于每个 3 操作，输出一行一个整数，表示当前的协同单元对总数。

输入输出样例
输入 #1复制

5
1 2 0
1 3 1
3
2 4 0
3
输出 #1复制

7
0
说明/提示
【评测用例规模与约定】
对于 30% 的评测用例，1≤q≤10 
3
 ，1≤k≤10。

对于所有评测用例，1≤q≤2×10 
5
 ，0≤v≤10 
9
 ，1≤k≤10 
3
 。 """
import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())

t = int(input())

arr = {}
arr[0] = 0
arr[1] = 0
arr[2] = 0
arr[3] = 0
total = 0
for _ in range(t):
    data = list(read())
    scode = data[0]
    match(scode):
        case 1:
            add_cnt = data[1]
            add_number = data[2]
            total += add_cnt
            if(add_number in arr):
                arr[add_number] += add_cnt
            else:
                arr[add_number] = add_cnt
        case 2:
            remove_cnt = data[1]
            remove_number = data[2]
            if(remove_number not in arr):
                continue
            removed = min(arr[remove_number], remove_cnt)
            arr[remove_number] -= removed
            total -= removed
        case 3:
            zero = arr[0]
            ans = zero * (total - zero) + zero * (zero - 1) // 2
            ans += arr[1] * (arr[2] + arr[3])
            print(ans)
