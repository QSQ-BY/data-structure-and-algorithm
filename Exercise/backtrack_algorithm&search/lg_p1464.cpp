/* # P1464 [PacNW 1999] Function

## 题目描述

对于一个递归函数 $w(a,b,c)$


- 如果 $a \le 0$ 或 $b \le 0$ 或 $c \le 0$ 就返回值 $1$。
- 如果 $a>20$ 或 $b>20$ 或 $c>20$ 就返回 $w(20,20,20)$
- 如果 $a<b$ 并且 $b<c$ 就返回 $w(a,b,c-1)+w(a,b-1,c-1)-w(a,b-1,c)$。
- 其它的情况就返回 $w(a-1,b,c)+w(a-1,b-1,c)+w(a-1,b,c-1)-w(a-1,b-1,c-1)$


这是个简单的递归函数，但实现起来可能会有些问题。当 $a,b,c$ 均为 $15$ 时，调用的次数将非常的多。你要想个办法才行。

注意：例如 $w(30,-1,0)$ 又满足条件 $1$ 又满足条件 $2$，请按照最上面的条件来算，答案为 $1$。

## 输入格式

会有若干行。

并以 $-1,-1,-1$ 结束。

## 输出格式

输出若干行，每一行格式：

`w(a, b, c) = ans`

注意空格。

## 输入输出样例 #1

### 输入 #1

```
1 1 1
2 2 2
-1 -1 -1
```

### 输出 #1

```
w(1, 1, 1) = 2
w(2, 2, 2) = 4
```

## 说明/提示

### 数据规模与约定

保证输入的数在 $[-9223372036854775808,9223372036854775807]$ 之间，并且是整数。

保证不包括 $-1, -1, -1$ 的输入行数 $T$ 满足 $1 \leq T \leq 10 ^ 5$。 */


#include <iostream>
#include <vector>
using namespace std;
long long memory[21][21][21];


long long  w(long long  a,long long  b,long long  c){
    if(a<=0 or b<=0 or c<=0) return 1;
    if(a>20 or b>20 or c>20) {
        if(memory[20][20][20] != -1){
            return memory[20][20][20];
        }
        return memory[20][20][20] = w(20,20,20);
    }
    if(memory[a][b][c] != -1){
        return memory[a][b][c];
    }
    if(a<b and b<c) {
        return memory[a][b][c] = w(a,b,c-1) + w(a,b-1,c-1) - w(a,b-1,c);
    }
    return memory[a][b][c] = w(a-1,b,c)+w(a-1,b-1,c)+w(a-1,b,c-1)-w(a-1,b-1,c-1);
}


int main(void){
    for(long long  i=0;i<21;i++){
        for(long long  j=0;j<21;j++){
            for(long long  k=0;k<21;k++){
                memory[i][j][k] = -1;
            }
        }
    }
    memory[0][0][0] = 1;
    while(1){
        long long  a;
        long long  b;
        long long  c;
        cin>>a>>b>>c;
        if(a==-1 and b==-1 and c==-1) break;
        printf("w(%lld, %lld, %lld) = %lld\n",a,b,c,w(a,b,c));
    }

    //system("pause");
    return 0;
}