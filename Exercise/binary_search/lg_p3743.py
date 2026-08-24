""" 小鸟有 n 个可同时使用的设备，第 i 个设备每秒消耗 a 
i
​
  个单位能量。能量的使用是连续的，也就是说能量不是某时刻突然消耗的，而是匀速消耗。也就是说，对于任意实数，在 k 秒内消耗的能量均为 k×a 
i
​
  单位。在开始的时候第 i 个设备里存储着 b 
i
​
  个单位能量。

同时小鸟又有一个可以给任意一个设备充电的充电宝，每秒可以给接通的设备充能 p 个单位，充能也是连续的，不再赘述。你可以在任意时间给任意一个设备充能，从一个设备切换到另一个设备的时间忽略不计。

小鸟想把这些设备一起使用，直到其中有设备能量降为 0。所以小鸟想知道，在充电器的作用下，她最多能将这些设备一起使用多久。

输入格式
第一行给出两个整数 n,p。

接下来 n 行，每行表示一个设备，给出两个整数，分别是这个设备的 a 
i
​
  和 b 
i
​
 。

输出格式
如果小鸟可以无限使用这些设备，输出 −1。

否则输出小鸟在其中一个设备能量降为 0 之前最多能使用多久。

设你的答案为 a，标准答案为 b，只有当 a,b 满足  
max(1,b)
∣a−b∣
​
 ≤10 
−4
  的时候，你能得到本测试点的满分。

输入输出样例
输入 #1复制

2 1
2 2
2 1000
输出 #1复制

2.0000000000
输入 #2复制

1 100
1 1
输出 #2复制

-1 
输入 #3复制

3 5
4 3
5 2
6 1
输出 #3复制

0.5000000000  """
import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())

n,p = read()
devices = []
total_rate = 0
total_energy = 0
for i in range(n):
    ai,bi = read()
    devices.append((ai,bi))
    total_rate += ai
    total_energy += bi
#check(i)表示在充电器的作用下能不能使用这些设备i时长
def check(duration:float)->bool:
    available_energy = p*duration
    required_energy = 0.0
    for ai,bi in devices:
        deficit = ai*duration-bi
        if(deficit > 0):
            required_energy += deficit
            if(required_energy > available_energy):
                return False
    return True

if(total_rate <= p):
    print(-1)
else:
    left = 0.0
    right = total_energy/(total_rate-p)
    while(abs(left - right) >= (5e-5)):
        mid = (left+right)/2
        if(check(mid)):
            left = mid
        else:
            right = mid
    print(f"{left:.10f}")

