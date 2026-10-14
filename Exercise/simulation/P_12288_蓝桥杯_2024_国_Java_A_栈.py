""" 题目描述
小蓝有一个栈，他不断地向这个栈的顶端添加数字。小蓝希望栈中不存在相同的数，当他加入了一个之前已经存在的数时，栈中之前存在的那个数会消失（其它原有元素的相对顺序不变），小蓝还想随时知道栈中所有相邻的数中和为奇数的总共有多少组，请你计算出小蓝要求的结果。

输入格式
输入的第一行包含一个整数 n。

接下来 n 行，每行包含一个整数 A 
i
​
 ，表示被添加的数。

输出格式
输出 n 行，每行包含一个整数表示每次添加数后的答案。

输入输出样例
输入 #1复制

4
1
2
3
2
输出 #1复制

0
1
2
1
说明/提示
评测用例规模与约定
对于 30% 的评测用例，1≤n≤1000，A 
i
​
 ≤300；
对于 70% 的评测用例，1≤n≤10 
5
 ，A 
i
​
 ≤1000；
对于所有评测用例，1≤n≤5×10 
5
 ，1≤A 
i
​
 ≤10 
6
 。 """
import sys
input = sys.stdin.buffer.readline

n = int(input())
size = 10**6 + 1
pre = [0] * size#记录每一个数字的前驱
nxt = [0] * size#记录每一个数字的后继
#bitearray是字节数字，每个位置的数字只能是0-255
#这里用来保存01看这个数字是不是已经出现过了
#bitearray比普通的布尔数组更省内存
present = bytearray(size)
ans = 0
out = []

for _ in range(n):
    x = int(input())

    # 删除已经存在的 x
    if present[x]:
        l, r = pre[x], nxt[x]
        if l:
            #如果奇偶性不同就是1的贡献
            #奇偶性相同就是0的贡献
            ans -= (l ^ x) & 1
        if r:
            ans -= (x ^ r) & 1
        if l and r:
            ans += (l ^ r) & 1

        nxt[l] = r
        pre[r] = l

    # 将 x 插入末尾
    tail = pre[0]

    if tail:
        ans += (tail ^ x) & 1

    pre[x] = tail
    nxt[x] = 0
    nxt[tail] = x
    pre[0] = x
    present[x] = 1
    out.append(str(ans))
sys.stdout.write("\n".join(out))
