""" 题目描述
小蓝的字典中有 n 个互不相同的单词 s 
1
​
 ,s 
2
​
 ,…,s 
n
​
 。每个单词仅由小写字母组成，长度不超过 20。

小蓝定义了一种操作：对一个单词进行下面两种变换之一：

在任意位置插入一个小写字母；
删除其中任意一个字母。
除插入或删除的位置外，原有字母的相对顺序保持不变。

现在请你统计有多少个有序单词对 (s 
i
​
 ,s 
j
​
 )（其中 i

=j）满足：可以通过对 s 
i
​
  恰好进行一次上述操作，使其变为 s 
j
​
 。

输入格式
第一行一个正整数 n。

接下来 n 行，每行一个仅由小写字母组成的字符串，表示一个单词。

输出格式
输出一行一个整数，表示满足条件的有序单词对数量。

输入输出样例
输入 #1复制

5
aab
ab
a
bb
b
输出 #1复制

8
说明/提示
【样例说明】
满足条件的 8 个有序单词对分别为：

(aab,ab)：从 aab 中删除第 1 个字母 a，得到 ab；
(ab,aab)：在 ab 的第 1 个位置插入字母 a，得到 aab；
(ab,a)：从 ab 中删除第 2 个字母 b，得到 a；
(a,ab)：在 a 的第 2 个位置插入字母 b，得到 ab；
(ab,b)：从 ab 中删除第 1 个字母 a，得到 b；
(b,ab)：在 b 的第 1 个位置插入字母 a，得到 ab；
(bb,b)：从 bb 中删除第 1 个字母 b，得到 b；
(b,bb)：在 b 的第 1 个位置插入字母 b，得到 bb。
【评测用例规模与约定】
对于 30% 的评测用例，1≤n≤100；

对于所有评测用例，1≤n≤10000。保证所有单词互不相同。 """
import sys

def solve():
    input = sys.stdin.buffer.readline
    
    n = int(input())
    words = []
    h = set()
    # 1. 第一次遍历：读取所有单词，同时存入列表和哈希集合 h
    for _ in range(n):
        word = input().decode().strip()
        words.append(word)
        h.add(word)

    ans = 0

    # 2. 第二次遍历：检查每个单词
    for cur_word in words:
        seen = set()

        # 尝试删除 cur_word 中的每一个字符
        for delete in range(len(cur_word)):
            sub = cur_word[:delete] + cur_word[delete+1:]
            # 去重判断
            if sub in seen:
                continue
            seen.add(sub)

            # 如果删掉一个字符后的单词在全量集合 h 中存在，说明匹配成功
            if sub in h:
                ans += 1

    print(2*ans)

if __name__ == '__main__':
    solve()


