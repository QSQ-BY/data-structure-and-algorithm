""" 题目描述
某个校验系统需要把 1,2,…,n 这 n 个编号各使用一次，排成一个长度为 n 的序列 p 
1
​
 ,p 
2
​
 ,…,p 
n
​
 。这样的序列称为一个排列。

系统会根据排列中相邻两个编号的差值奇偶性生成一个长度为 n−1 的校验串。对于每个 1≤i<n，第 i 位校验字符 c 
i
​
  按如下规则确定：

如果 ∣p 
i
​
 −p 
i+1
​
 ∣ 为偶数，则 c 
i
​
  为 0；
如果 ∣p 
i
​
 −p 
i+1
​
 ∣ 为奇数，则 c 
i
​
  为 1。
现在给定一个长度为 n−1 的目标校验串 S。你需要构造一个排列，使它生成的校验串 c 
1
​
 c 
2
​
 …c 
n−1
​
  恰好等于 S。

如果存在多个满足要求的排列，请输出字典序最小的一个。对于两个不同排列 a 
1
​
 ,a 
2
​
 ,…,a 
n
​
  与 b 
1
​
 ,b 
2
​
 ,…,b 
n
​
 ，若存在位置 k，使得前 k−1 个数都相同且 a 
k
​
 <b 
k
​
 ，则称排列 a 的字典序小于排列 b。

如果不存在满足要求的排列，请输出 −1。

输入格式
第一行包含一个整数 n，表示编号数量。

第二行包含一个长度为 n−1 的字符串 S，表示目标校验串，字符串仅由字符 0 和 1 组成。

输出格式
如果不存在满足要求的排列，输出一行一个整数 −1。

否则输出一行 n 个整数，表示字典序最小的合法排列。相邻两个整数之间用一个空格分隔。

输入输出样例
输入 #1复制

5
1010
输出 #1复制

1 2 4 3 5
输入 #2复制

6
00000
输出 #2复制

-1
输入 #3复制

8
0101101
输出 #3复制

1 3 2 4 5 6 8 7
说明/提示
【样例说明 1】
该排列对应的相邻差值依次为：

∣1−2∣=1，为奇数，对应 1；
∣2−4∣=2，为偶数，对应 0；
∣4−3∣=1，为奇数，对应 1；
∣3−5∣=2，为偶数，对应 0。
因此生成的校验串为 1010。在所有合法排列中，1 2 4 3 5 的字典序最小。

【样例说明 2】
目标校验串的每一位都是 0，因此任意相邻两个编号的差值都必须为偶数，也就是它们奇偶性相同。这样所有位置上的编号都必须具有相同奇偶性，但 1 到 6 中既有奇数也有偶数，所以无解。

【样例说明 3】
输出排列生成的校验串依次为 0、1、0、1、1、0、1，与目标校验串 0101101 相同。

【评测用例规模与约定】
对于 30% 的评测用例，2≤n≤8。

对于 60% 的评测用例，2≤n≤5000。

对于所有评测用例，2≤n≤2×10 
5
 ，且 S 的长度为 n−1。 """

#只要首位的奇偶性确定，剩下所有位置的奇偶性就确定了
import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())

n = int(input())
code = list(input().decode().strip())
odd_count = (n+1)//2
even_count = n//2
def build(first):
    #first表示第一个是偶数还是奇数
    parity = [0]*(n)
    parity[0] = first
    for i in range(n-1):
        if(code[i] == "0"):
            parity[i+1] = parity[i]
        elif(code[i] == "1"):
            parity[i+1] = parity[i]^1
    even_need = parity.count(0)
    odd_need = parity.count(1)
    if(even_need != even_count or odd_need != odd_count):
        return None
    odd = 1
    even = 2
    ans = []
    for x in parity:
        if(x == 1):
            ans.append(odd)
            odd += 2
        else:
            ans.append(even)
            even += 2
    return ans

ans = build(1)
if(ans is None):
    ans = build(0)
if(ans is None):
    print(-1)
else:
    print(*ans)
