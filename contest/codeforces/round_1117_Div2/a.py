""" The Beaver was given a set of words S
, which initially contained n
 words. Then he performed the following operation m
 times:
海狸得到了一组单词 S
 ，其中最初包含 n
 个单词。然后，海狸重复执行了 m
 次以下操作：

The Beaver forms a sequence of one or more words from the set S
. The same word may appear in the sequence several times. An abbreviation∗
 is formed from the resulting phrase.
“海狸”这个单词是由集合 S
 中的一个或多个单词组合而成的。同一个单词可以在该序列中出现多次。而由这些单词组合而成的短语，则可以被缩写为 ∗
 。
Then the Beaver adds the resulting abbreviation to S
 and can now use it in subsequent operations as an ordinary word.
然后，海狸会将得到的缩写添加到 S
 中，之后就可以像使用普通单词一样在后续操作中加以使用了。
You are given the n
 initial words that were in the set S
, and the set of abbreviations that the Beaver formed. Determine whether the Beaver made a mistake and whether all these abbreviations could have appeared as a result of the operation described above. Note that the abbreviations did not necessarily appear in the same order in which they are given to you.
你已知悉最初存在于集合 S
 中的 n
 个单词，以及 Beaver 所创造的那些缩写形式。你需要判断 Beaver 是否犯了错误，以及这些缩写是否确实可以通过上述操作过程生成。请注意，这些缩写出现的顺序不一定与给定的顺序相同。

∗
The abbreviation of a sequence is the word produced by the first letters of the words in the sequence. For example, the sequence birch OAK birch redwood produces the abbreviation BOBR.
∗
 一个序列的缩写，是由该序列中各个单词的首字母组成的单词。例如，序列“birch OAK birch redwood”的缩写就是“BOBR”。

Input  输入
Each test contains multiple test cases. The first line contains the number of test cases t
 (1≤t≤500
). The description of the test cases follows.
每个测试包含多个测试用例。第一行包含测试用例的数量 t
 ( 1≤t≤500
 )。测试用例的描述随后给出。

The first line of each test case contains two integers n
 and m
 — the number of ordinary words and the number of abbreviations, respectively (1≤n,m≤100
).
每个测试用例的第一行包含两个整数： n
 和 m
 。它们分别表示普通单词的数量和缩写词的数量（ 1≤n,m≤100
 ）。

Each of the next n
 lines contains one string wi
 — an ordinary word (1≤|wi|≤20
).
接下来的每一行都包含一个字符串——也就是一个普通的单词而已。

Each of the next m
 lines contains one string ai
 — an abbreviation formed by Bobr (1≤|ai|≤20
).
接下来的每一行 m
 都包含一个字符串 ai
 ——这些字符串都是 Bobr( 1≤|ai|≤20
 )所创造的缩写形式。

All ordinary words consist of lowercase English letters, and all abbreviations consist of uppercase English letters. In each test case, all strings w1,w2,…,wn,a1,a2,…,am
 are pairwise distinct.
所有的普通单词都由小写英文字母组成，而所有的缩写则由大写英文字母组成。在每个测试案例中，所有的字符串 、 w1,w2,…,wn,a1,a2,…,am
 都是互不相同的。

The total length of all strings over all test cases does not exceed 50000
.
所有测试用例中所有字符串的总长度都不超过 50000
 。

Output  输出结果
For each test case, print "YES" if there exists a suitable order in which the given abbreviations could have appeared, and "NO" otherwise.
对于每个测试用例，如果存在一种合适的顺序，使得给定的缩写能够按该顺序出现，则输出“YES”；否则输出“NO”。

You may print each letter in any case (lowercase or uppercase). For example, the strings "yEs", "yes", "Yes", and "YES" will be accepted as a positive answer.
您可以以任意大小写形式来输入每个字母。例如，“yEs”、“yes”、“Yes”和“YES”都被视为有效的回答。
"""
import sys
input = sys.stdin.readline

def solve()->None:
    n , m = map(int,input().split())
    strings = {}
    for i in range(n):
        new_string = str(input().strip())
        ch = new_string[0].upper()
        if( ch not in strings):
            strings[ch] = 1
    flag = 1
    for i in range(m):
        string = str(input().strip())
        for j in range(len(string)):
            if(string[j] in strings):continue
            flag = 0

    if flag == 1:
        print("YES")
    else:
        print("NO")
    return

def main()->None:
    t = int(input())
    while t:
        solve()
        t -=1

if (__name__ == "__main__"):
    main()