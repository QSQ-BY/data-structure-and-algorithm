""" 题目描述
排列与组合是常用的数学方法，其中组合就是从 n 个元素中抽出 r 个元素（不分顺序且 r≤n），我们可以简单地将 n 个元素理解为自然数 1,2,…,n，从中任取 r 个数。

现要求你输出所有组合。

例如 n=5,r=3，所有组合为：

123,124,125,134,135,145,234,235,245,345。

输入格式
一行两个自然数 n,r(1<n<21,0≤r≤n)。

输出格式
所有的组合，每一个组合占一行且其中的元素按由小到大的顺序排列，每个元素占三个字符的位置，所有的组合也按字典顺序。

注意哦！输出时，每个数字需要 3 个场宽。以 C++ 为例，你可以使用下列代码：

cout << setw(3) << x;

输出占 3 个场宽的数 x。注意你需要头文件 iomanip。

输入输出样例
输入 #1复制

5 3 
输出 #1复制

  1  2  3
  1  2  4
  1  2  5
  1  3  4
  1  3  5
  1  4  5
  2  3  4
  2  3  5
  2  4  5
  3  4  5 """
import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())

n,m = read()
arr = [0]*m
def print_an_answer(ans: list):
    print("".join(f"{number:3d}" for number in ans))

#当前要填入数字的位置，当前能填入数字的最小值
def dfs(pos:int,min:int):
    global arr
    if(pos == m):
        print_an_answer(arr)
        return
    for number in range(min,n+1):
        if(n - number +1 < m-pos ):
            break
        arr[pos] = number
        dfs(pos+1,number+1)
        arr[pos] = 0

dfs(0,1)