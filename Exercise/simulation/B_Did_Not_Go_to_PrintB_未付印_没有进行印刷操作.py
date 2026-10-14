""" B. Did Not Go to Print
B. 未付印/没有进行印刷操作
time limit per test2 seconds
每个测试用例的时间限制：2 秒
memory limit per test256 megabytes
每次测试的记忆限制：256 兆字节
Recently, K1o0n bought himself a new expensive printer, which is distinguished by its memory, that is, it may not print immediately. Yesterday, while he was away from his new purchase, his friends used the printer.
最近，K1o0n 给自己买了一台价格不菲的新打印机。这台打印机的特点在于其内存较大，不过它不能立即开始打印任务。昨天，当 K1o0n 不在家时，他的朋友们使用了这台打印机。

There are n
 documents numbered from 1
 to n
. Initially, the printer memory is empty. The friends sequentially performed n
 commands on the printer, where the i
-th command can be one of:
共有 n
 份文档，其编号范围为 1
 到 n
 。最初，打印机的内存是空的。朋友们依次对打印机执行了 n
 条指令。其中，第 i
 条指令可以是以下指令中的任意一条：

'1'  — scanning. Document i
 is sent to the device memory and is placed on top of everything already there.
“1” — 扫描模式。文档 i
 会被发送到设备内存中，并存储在内存中已有的所有数据之上。
'2'  — printing from memory. If the memory is not empty, the device prints the topmost document in memory and removes it from there. Otherwise, the device prints document i
.
“2”——从内存中打印。如果内存不为空，设备会打印内存中最上面的文档，然后将该文档从内存中移除。否则，设备会打印文档 i
 。
'3'  — quick print. The device prints document i
.
“3” — 快速打印模式。该设备将打印文档 i
 。
Today, the friends came to K1o0n with a complaint — not all documents were printed. Help K1o0n find the indices of all documents that were not printed.
今天，朋友们来到 K1o0n 那里投诉——并非所有的文档都已被打印出来。请帮助 K1o0n 找出所有未被打印出来的文档的索引。

Input  输入
The first line contains an integer t
 (1≤t≤104
) — the number of testcases.
第一行包含一个整数 t
 ( 1≤t≤104
 )，表示测试用例的数量。

The first line of each testcase contains an integer n
 (1≤n≤2⋅105
) — the number of documents.
每个测试用例的第一行包含一个整数 n
 ( 1≤n≤2⋅105
 )，表示该测试用例中包含的文档数量。

The second line of each testcase contains a string s
 of length n
, consisting of the characters '1', '2' and '3' — the friends' commands.
每个测试用例的第二行包含一个长度为 n
 的字符串 s
 ，该字符串由字符‘1’、‘2’和‘3’组成——这些字符代表了朋友们的指令。

It is guaranteed that the sum of n
 over all testcases does not exceed 2⋅105
.
可以保证，所有测试用例中 n
 的值之和不会超过 2⋅105
 。

Output  输出
For each testcase, output two lines.
对于每个测试用例，输出两行。

In the first line — the number k
 of documents that were not printed.
第一行显示了未打印的文档数量： k
 份。

In the second line — their numbers in increasing order, separated by spaces. If k=0
, the second line is empty.
第二行中，这些数字按递增顺序排列，数字之间用空格分隔。如果为 k=0
 ，则第二行为空。 """
import sys
input = sys.stdin.buffer.readline
t = int(input())
for _ in range(t):
    stack = []
    n= int(input())#文档的数量
    string = "a"+input().decode().strip()
    Print = [False]*(n+1)#print[i]表示第i个文件有没有被打印
    for i in range(1,n+1):
        match(string[i]):
            case "1":
                stack.append(i)
            case "2":
                if(len(stack) != 0):
                    Print[stack[-1]] = True
                    stack.pop()
                else:
                    Print[i] = True
            case "3":
                Print[i] = True

    ans = []
    for i in range(1,n+1):
        if(Print[i] == False):
            ans.append(i)
    print(len(ans))
    print(*ans)

