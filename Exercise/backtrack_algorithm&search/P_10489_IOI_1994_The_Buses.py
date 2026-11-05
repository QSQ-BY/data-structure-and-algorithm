""" 题目描述
一个人在 12:00 到达一个公交车站。他在 12:00 到 12:59 期间一直待在那里。这个公交车站被多条公交线路使用。这个人记录了公交车到达的时间。给出了公交车到达的时间。

同一条路线的公交车在整个小时内从 12:00 到 12:59 以固定的时间间隔到达。
时间以整分钟给出，从 0 到 59。
每条公交线路至少停靠 2 次。
测试示例中的公交线路数量将 ≤17。
不同路线的公交车可能同时到达。
几条公交线路的首次到达时间和/或时间间隔可能相同。如果两条公交线路的起始时间和间隔相同，则它们是不同的，并且都需要呈现。
找出满足输入数据的必须停靠在公交车站的公交线路数量最少的时间表。对于每条公交线路，输出起始时间和间隔。

输入格式
你的程序需要从标准输入中读取。输入包含一个数字 n（n≤300），表示已经记录的到达公交车的数量，后跟按升序排列的到达时间。

输出格式
你的程序需要写入标准输出。输出包含一个整数，即最少的公交线路数量。

翻译来自于：ChatGPT

输入输出样例
输入 #1复制

17
0 3 5 13 13 15 21 26 27 29 37 39 39 45 51 52 53
输出 #1复制

3 """
import sys
input = sys.stdin.buffer.readline
def read():
    # 读取剩余所有时刻，允许输入分成多行。
    return map(int, sys.stdin.buffer.read().split())

def solution1():
    n = int(input())
    time = list(read())
    def dfs(bus: list[list[int]], index: int, depth: int):
        if len(bus) > depth:
            return False

        if index == n:
            for b in bus:
                # 每条线路至少到站两次
                if len(b) < 2:
                    return False

                d = b[1] - b[0]

                # 下一班如果仍在这一小时内，说明线路还不完整
                if b[-1] + d < 60:
                    return False

            return True

        cur = time[index]

        # 剪枝：检查是否错过下一班，以及剩余记录是否足够补全已有线路。
        need = 0
        for b in bus:
            if len(b) == 1:
                need += 1
            else:
                d = b[1] - b[0]
                expected = b[-1] + d
                if expected < 60 and expected < cur:
                    return False
                need += (59 - b[-1]) // d

        if need > n - index:
            return False

        # 剪枝：已确定线路正好等待当前时刻时，直接分配。
        for b in bus:
            if(len(b) >= 2):
                d = b[1] - b[0]
                if(b[-1] + d == cur):
                    b.append(cur)
                    result = dfs(bus,index + 1,depth)
                    b.pop()
                    return result

        # 剪枝：起点相同的单点线路，本层只尝试一条。
        seen = set()
        for b in bus:
            if len(b) != 1:
                continue
            if b[0] in seen:
                continue
            seen.add(b[0])
            d = cur - b[0]
            if d <= 0 or b[0] >= d:
                continue
            b.append(cur)
            result = dfs(bus, index + 1, depth)
            b.pop()
            if result:
                return True
        # 剪枝：线路数达到上限，或者当前时刻已经无法作为首次到站时间。
        if len(bus) >= depth or cur >= 30:
            return False
        # 尝试新建线路，并在返回时恢复现场
        bus.append([cur])
        result = dfs(bus, index + 1, depth)
        bus.pop()
        return result

    # 同一条线路在同一分钟最多到站一次，以最大出现次数作为线路数下界。
    from collections import Counter
    depth = max(Counter(time).values(), default=0)
    while not dfs([], 0, depth):
        depth += 1
    print(depth)

def solution2():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n = data[0]
    t = [0] * 305
    for x in data[1:n + 1]:
        t[x] += 1
    def check(s, d):
        for i in range(s, 60, d):
            if t[i] == 0:
                return False
        return True
    a = []
    for s in range(60):
        for d in range(s + 1, 60 - s):
            if check(s, d):
                length = (59 - s) // d + 1
                a.append((s, d, length))
    a.sort(key=lambda node: node[2], reverse=True)
    cnt = len(a)
    dep = 0
    #参数	含义
    #x	已经选了多少条线路
    #pos	接下来只允许选择编号不小于 pos 的候选线路
    #total	已经覆盖了多少条到站记录
    def dfs(x, pos, total):
        if x == dep:
            return total == n
        if pos >= cnt:
            return False
        if total + a[pos][2] * (dep - x) < n:
            return False
        for i in range(pos, cnt):
            s, d, length = a[i]
            if not check(s, d):
                continue
            for j in range(s, 60, d):
                t[j] -= 1
            if dfs(x + 1, i, total + length):
                return True
            for j in range(s, 60, d):
                t[j] += 1
        return False
    while not dfs(0, 0, 0):
        dep += 1
    print(dep)

solution2()
