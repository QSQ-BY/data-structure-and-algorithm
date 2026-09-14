""" 题目描述
小蓝有一张门电路的逻辑图，如下图所示：



图中每个三角形代表着一种门电路，可能是与门、或门、异或门中的任何一种，它接受上一层中的两个圆形中的数据作为输入，产生一个输出值输出到下一级（如图中箭头所示）。图中圆形表示的是暂存的输出结果，取值只可能是 0 或 1，为了便于表示我们用 arr[i][j] 表示第 i（0≤i≤4）行第 j（0≤j≤i）个圆形的值。其中 arr[0]=(In[0],In[1],In[2],In[3],In[4]) 表示的是输入数据，对于某个 arr[i][j]（i≤0），计算方式为 arr[i][j]=arr[i−1][j] op arr[i−1][j+1]，其中 op 表示的是将 arr[i−1][j]、arr[i−1][j+1] 作为输入，将 arr[i][j] 作为输出的那个门电路, 与门、或门、异或门分别对应于按位与 (&)、按位或 (∣)、按位异或 (^) 运算符。

现在已知输入为 In[0]=1,In[1]=0,In[2]=1,In[3]=0,In[4]=1，小蓝想要使得最终的输出 Out 的值为 1，请问一共有多少种不同的门电路组合方式？其中上图中显示的就是一种合法的方式。

输入格式
无

输出格式
这是一道结果填空的题，你只需要算出结果后提交即可。本题的结果为一个整数，在提交答案时只输出这个整数，填写多余的内容将无法得分。 
"""
In = [[0]*5 for _ in range(5)]
In[0] = [1,0,1,0,1]
for i in range(1,5):
    In[i] = [-1] *(5-i)

op = [[""]*4 for _ in range(4)]
for i in range(1,4):
    op[i] = [""] * (4-i)
operations = ["&","^","|"]
ans = 0
def calculate():
    global ans
    for i in range(1,5):
        for j in range(0,5 - i):
            operation = op[i-1][j]
            match(operation):
                case "&":
                    In[i][j] = In[i-1][j] & In[i-1][j+1]
                case "|":
                    In[i][j] = In[i-1][j] | In[i-1][j+1]
                case "^":
                    In[i][j] = In[i-1][j] ^ In[i-1][j+1]
    if(In[4][0] == 1):
        ans += 1
def dfs(layer,index):
    if(layer >= 4):
        calculate()
        return
    for operation in operations:
        op[layer][index] = operation
        if(layer + index == 3):
            dfs(layer + 1,0)
        else:
            dfs(layer,index + 1)
dfs(0,0)
print(ans)