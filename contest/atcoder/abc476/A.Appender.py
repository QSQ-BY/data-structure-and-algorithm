""" Problem Statement  问题描述
You are given a string 
S consisting of lowercase English letters.
你得到的是一个由小写英文字母组成的字符串 
S 。

Output the string 
T determined as follows.
按照以下方式输出字符串 
T 。

If the last character of 
S is e, 
T is the string obtained by appending r to the end of 
S.
如果 
S 的最后一个字符是 e ，那么 
T 就是将 r 附加到 
S 的末尾后得到的字符串。
If the last character of 
S is not e, 
T is the string obtained by appending er to the end of 
S.
如果 
S 的最后一个字符不是 e ，那么 
T 就是将 er 附加到 
S 的末尾后得到的字符串。
Constraints  约束
S is a string consisting of lowercase English letters.
S 是由小写英文字母组成的字符串。
The length of 
S is between 
1 and 
10, inclusive.
S 的长度介于 
1 到 
10 之间，包含。
Input  输入
The input is given from Standard Input in the following format:
输入从标准输入以以下格式给出：

S
Output  输出
Output the answer.  输出答案。

Sample Input 1  示例输入 1 复制
Copy  副本
live
Sample Output 1  示例输出 1 复制
Copy  副本
liver
The last character of live is e, so the string liver, obtained by appending r to the end of live, is the string 
T to be outputted.
live 的最后一个字符是 e ，因此字符串 liver ，通过在 live 末尾加上 r 得到，就是要输出的字符串 
T 。

Sample Input 2  示例输入 2 复制
Copy  副本
femur
Sample Output 2  样本输出 2Copy
Copy  副本
femurer
The last character of femur is not e, so the string femurer, obtained by appending er to the end of femur, is the string 
T to be outputted.
femur 的最后一个字符不是 e ，因此字符串 femurer 是通过在 femur 末尾加上 er 得到的字符串 
T 。

Sample Input 3  示例输入 3 复制
Copy  副本
chimpanzee
Sample Output 3  示例输出 3 复制
Copy  副本
chimpanzeer
The last character of chimpanzee is e, so the string chimpanzeer, obtained by appending r to the end of chimpanzee, is the string 
T to be outputted.
chimpanzee 的最后一个字符是 e ，因此字符串 chimpanzeer ，通过在 chimpanzee 末尾加上 r 得到，就是要输出的字符串 
T 。 """
import sys
input = sys.stdin.buffer.readline
string = list(input().decode().strip())
if(string[-1] == "e"):
    string.append("r")
else:
    string.append("er")
print(*string,sep = "")
