""" Problem Statement  问题描述
In the Kingdom of AtCoder, two kinds of bills are in circulation: 
1-dollar bills and 
K-dollar bills.
在 AtCoder 王国里，有两种面额的货币在流通： 
1 美元纸币和 
K 美元纸币。

At Company J's fully automated cafeteria in the kingdom, desserts and drinks are sold as products.
在 J 公司在该国的全自动自助餐厅里，甜点和饮料都是作为商品来销售的。

The company's fully automated cafeteria has a dessert vending machine that sells 
N desserts, and a drink vending machine that sells 
M drinks. The desserts are numbered 
1 through 
N, and the drinks are numbered 
1 through 
M.
该公司的全自动自助餐厅里有一台甜点自动售货机，出售 
N 种甜点；还有一台饮料自动售货机，出售 
M 种饮料。这些甜点的编号为 
1 到 
N ，饮料的编号则为 
1 到 
M 。

Dessert 
i costs 
A 
i
​
  dollars, and drink 
j costs 
B 
j
​
  dollars.
甜点 
i 的价格是 
A 
i
​
  美元，饮料 
j 的价格则是 
B 
j
​
  美元。

As payment, the dessert vending machine accepts both 
1-dollar bills and 
K-dollar bills, but the drink vending machine accepts only 
K-dollar bills. Both vending machines give change using only 
1-dollar bills. You cannot buy two or more of the same product.
作为支付方式，甜点自动售货机既接受 
1 美元纸币，也接受 
K 美元纸币；而饮料自动售货机则只接受 
K 美元纸币。两台自动售货机在找零时都只使用 
1 美元纸币。您不能购买同一种商品两件或更多件。

Takahashi came to Company J's fully automated cafeteria with 
X 
1-dollar bills and 
Y 
K-dollar bills.
高桥带着面值为 
X 美元和 
1 美元的钞票，以及面值为 
Y 美元和 
K 美元的钞票，来到了 J 公司的全自动自助餐厅。

Among the combinations of products that he can buy with the bills he has, find the maximum number of products he can purchase.
用他手头的钱，他可以购买各种产品的组合。请找出他能够购买的产品数量的最大值。

Constraints  约束
1≤N≤2×10 
5
 
1≤M≤2×10 
5
 
2≤K≤10 
9
 
0≤X≤10 
15
 
0≤Y≤10 
9
 
1≤A 
i
​
 ≤10 
9
  (
1≤i≤N)
1≤B 
j
​
 ≤10 
9
  (
1≤j≤M)
All input values are integers.
所有输入值均为整数。
Input  输入
The input is given from Standard Input in the following format:
输入从标准输入以以下格式给出：

N 
M 
K
X 
Y
A 
1
​
  
… 
A 
N
​
 
B 
1
​
  
… 
B 
M
​
 
Output  输出
Output the answer.  输出答案。

Sample Input 1  示例输入 1 复制
Copy  副本
2 3 10
50 6
22 30
20 12 24
Sample Output 1  示例输出 1 复制
Copy  副本
4
By shopping as follows, Takahashi can buy four products.
通过上述购物方式，高桥可以购买到四件商品。

Pay two 
10-dollar bills to buy drink 
1. No change.
支付两张 
10 美元的钞票来购买 
1 饮料。无需找零。
Pay two 
10-dollar bills to buy drink 
2. The change is eight 
1-dollar bills.
支付两张 
10 美元的钞票来购买 
2 饮料。找零是八张 
1 美元的钞票。
Pay two 
10-dollar bills and ten 
1-dollar bills to buy dessert 
2. No change.
支付两张 
10 美元的钞票和十张 
1 美元的钞票，就可以购买 
2 甜点。无需找零。
Pay twenty-two 
1-dollar bills to buy dessert 
1. No change.
支付 22 张 
1 美元纸币才能购买 
1 甜点。没有零钱找零。
He cannot buy more than four products, so the answer is 
4.
他最多只能购买四种产品，所以答案是 
4 。

Sample Input 2  示例输入 2 复制
Copy  副本
1 7 67
677677677766666 0
777666777
20 12 24 67 67 67 67
Sample Output 2  样本输出 2Copy
Copy  副本
1
By shopping as follows, Takahashi can buy one product.
通过以下购物方式，高桥可以购买一件商品。

Pay 
600000777666777 
1-dollar bills to buy dessert 
1. The change is 
600000000000000 
1-dollar bills.
支付 
600000777666777 
1 美元来购买 
1 中的甜点。找回的零钱是 
600000000000000 
1 美元。
He cannot buy more than one product, so the answer is 
1.
他只能购买一件产品，因此答案是 
1 。

Sample Input 3  示例输入 3 复制
Copy  副本
20 20 30
605776135 133105105
97363214 218434035 697895427 109255624 299037330 227873982 195540071 411713803 828357845 244535208 138059186 639510883 39844882 707397687 371274487 696536603 351588202 319490007 47121612 87169661
32256972 567982330 554885983 299718223 443859449 687952877 264684780 666659381 576335424 941894234 406248934 321334900 423472560 863738035 213143887 384834384 468161291 673106162 164648316 15903323
Sample Output 3  示例输出 3 复制
Copy  副本
22 """
import sys
from bisect import bisect_right
from itertools import accumulate 
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())

def test01():
    n,m,k = read()#甜点既接受1元纸币也接受K元纸币，饮料只接受K元纸币,每个都会找零1元纸币
    x,y = read()#有x个一美元纸币和y个k美元纸币

    dessert_price = list(read())
    drink_price = list(read())
    #输出最大能购买多少件商品
    dessert_price.sort()
    drink_price.sort()

    ans = 0

    def calculate(a:int):
        #我们打算拿m个k元纸币去买饮料
        k_number = a
        one_number = (y - a)*10 + x
        cnt = 0
        ret = 0
        for drink in drink_price:
            while(cnt <= k_number and cnt * k<drink):
                cnt += 1
            if(cnt <= k_number and cnt*k >= drink):
                k_number -= cnt
                ret += 1
                one_number += cnt*k - drink
            else:
                break

        s = 0
        for dessert in dessert_price:
            s += dessert
            if(one_number >= s):
                ret += 1
        return ret

    #枚举我们打算拿多少个十元纸币去买饮料
    for a in range(y+1):
        #我们打算用k个十元纸币去买饮料
        ans = max(calculate(a),ans)

    print(ans)


def test02():
    n,m,k = read()#甜点既接受1元纸币也接受K元纸币，饮料只接受K元纸币,每个都会找零1元纸币
    x,y = read()#有x个一美元纸币和y个k美元纸币
    # 解析甜点价格
    a = list(read())
    b = list(read())
    #输出最大能购买多少件商品
    a.sort()
    b.sort()
    
    # 预处理甜点的价格前缀和，方便后续二分查找
    pref_a = [0,*accumulate(a)]
        
    max_items = 0
    
    # 当前已选饮料所需消耗的 K 美元纸币总数
    req_k_bills = 0
    # 当前已选饮料所消耗的总金额
    cost_sum = 0
    # 我们初始拥有的总资产价值
    total_money = x + y * k
    
    # 枚举购买前 c 瓶饮料（c 从 0 到 m）
    for c in range(0,m + 1):
        if(c>0):
            drink_price = b[c-1]
            # 购买这瓶饮料需要的 K 美元纸币数量（向上取整）
            req_k_bills += (drink_price + k - 1) // k
            cost_sum += drink_price
        
        # 如果当前所需的 K 纸币数量超标，或者总金额超标，后续必定也不行
        if req_k_bills > y or cost_sum > total_money:
            break
        # 计算剩余总金额
        rem_money = total_money - cost_sum
        
        # 二分查找：用 rem_money 最多能买多少个甜点
        # bisect_right 返回插入点，减 1 就是最多能买的甜点数量
        d = bisect_right(pref_a, rem_money) - 1#返回严格大于的店
        
        # 更新最大购买件数
        max_items = max(max_items,c+d)
            
    print(max_items)

#test01()
test02()

