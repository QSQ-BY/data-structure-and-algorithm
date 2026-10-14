""" 题目描述
在一个字符串 S 中，如果 S 
i
​
 =S 
i−1
​
  且 S 
i
​
 

=S 
i+1
​
 ，则称 S 
i
​
  和 S 
i+1
​
  为边缘字符。如果 S 
i
​
 

=S 
i−1
​
  且 S 
i
​
 =S 
i+1
​
 ，则 S 
i−1
​
  和 S 
i
​
  也称为边缘字符。其它的字符都不是边缘字符。

对于一个给定的串 S，一次操作可以一次性删除该串中的所有边缘字符（操作后可能产生新的边缘字符）。

请问经过 2 
64
  次操作后，字符串 S 变成了怎样的字符串，如果结果为空则输出 EMPTY。

输入格式
输入一行包含一个字符串 S 。

输出格式
输出一行包含一个字符串表示答案，如果结果为空则输出 EMPTY。

输入输出样例
输入 #1复制

edda
输出 #1复制

EMPTY
输入 #2复制

sdfhhhhcvhhxcxnnnnshh
输出 #2复制

s
说明/提示
评测用例规模与约定
对于 25% 的评测用例, ∣S∣≤10 
3
 ，其中 ∣S∣ 表示 S 的长度；
对于 50% 的评测用例, ∣S∣≤10 
4
 ；
对于 75% 的评测用例, ∣S∣≤10 
5
 ；
对于所有评测用例, ∣S∣≤10 
6
 ，S 中仅含小写字母。 """
import sys
input = sys.stdin.buffer.readline
string = list(input().decode().strip())
n = len(string)
#用来判断字符是否被删除
available = bytearray(n)
#用来保存每一个字符前驱和后继的下标
#-1表示指向空节点，n号节点是虚拟尾节点
pre = [-1]*(n+1)
nxt = [-1]*(n+1)
for i,ch in enumerate(string):
    if(i == 0):
        nxt[i] = i+1
        continue
    nxt[i] = i+1
    pre[i] = i-1

#进行一轮的删除
def delete():
    global available
    d = []
    for i,ch in enumerate(string):
        if(available[i] == 1):
            continue
        j,k = pre[i],nxt[i]
        #头尾节点不能作为判断中心，但可能被相邻节点标记删除
        if(j==-1 or j==n or k==-1 or k== n):
            continue
        pre_ch = string[j]
        nxt_ch = string[k]
        #删除当前节点和后继节点
        if(pre_ch == ch and nxt_ch!=ch):
            d.append(i)
            d.append(k)

        #删除当前节点和前驱节点
        if(nxt_ch == ch and pre_ch != ch):
            d.append(j)
            d.append(i)

    if(len(d) == 0):
        ans = []
        for i in range(n):
            if(available[i] == 0):
                ans.append(string[i])
        if(len(ans) == 0):
            print("EMPTY")
        else:
            print("".join(ans))
        sys.exit()
    else:
        #本轮判断完成后统一删除，同一节点只删除一次
        #使用set进行去重
        for index in set(d):
            j,k = pre[index],nxt[index]
            if(j != -1):
                nxt[j] = k
            pre[k] = j
            available[index] = 1

def delete2():
    # 第一轮检查全部字符
    check = set(range(n))
    while check:
        d = set()
        # 第一阶段：找出本轮所有待删除字符
        for i in check:
            if available[i] == 1:
                continue
            j, k = pre[i], nxt[i]
            if j == -1 or k == n:
                continue

            ch = string[i]

            if string[j] == ch and string[k] != ch:
                d.add(i)
                d.add(k)

            if string[k] == ch and string[j] != ch:
                d.add(j)
                d.add(i)

        if not d:
            break

        # 第二阶段：统一删除，并收集下一轮候选位置
        #没有加入下一轮check的下标表示下一轮和上一轮中
        #这一个节点的前驱和后继没有任何的变化
        next_check = set()

        for index in d:
            j, k = pre[index], nxt[index]

            if j != -1:
                nxt[j] = k
                next_check.add(j)

            pre[k] = j
            if k != n:
                next_check.add(k)
            available[index] = 1
        check = next_check

    # 最后只需扫描一次，输出存活字符
    ans = []
    for i in range(n):
        if not available[i]:
            ans.append(string[i])

    print("".join(ans) if ans else "EMPTY")

delete2()
