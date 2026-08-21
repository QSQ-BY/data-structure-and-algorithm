/* # B3612 【深进1.例1】求区间和

## 题目描述

给定 $n$ 个正整数组成的数列 $a_1, a_2, \cdots, a_n$ 和 $m$ 个区间 $[l_i,r_i]$，分别求这 $m$ 个区间的区间和。

## 输入格式

第一行包含一个正整数 $n$，表示序列的长度。

第二行包含 $n$ 个正整数 $a_1,a_2, \cdots ,a_n$。

第三行包含一个正整数 $m$，表示区间的数量。

接下来 $m$ 行，每行包含两个正整数 $l_i,r_i$，满足 $1\le l_i\le r_i\le n$。

## 输出格式

共 $m$ 行，其中第 $i$ 行包含一个正整数，表示第 $i$ 组答案的询问。

## 输入输出样例 #1

### 输入 #1

```
4
4 3 2 1
2
1 4
2 3
```

### 输出 #1

```
10
5
```

## 说明/提示

### 样例解释
第 $1$ 到第 $4$ 个数加起来和为 $10$。第 $2$ 个数到第 $3$ 个数加起来和为 $5$。
### 数据范围
对于 $50 \%$ 的数据：$n,m\le 1000$；

对于 $100 \%$ 的数据：$1 \le n, m\le 10^5$，$1 \le a_i\le 10^4$。 */
#include <iostream>
#include <vector>
using namespace std;
int main(void){
    int n=0;
    cin>>n;//序列长度
    vector<int> prefix(n+1,0);
    for(int i=1;i<n+1;i++){
        cin>>prefix[i];
        prefix[i] = prefix[i] + prefix[i-1];
    }
    for(int i=0;i<n+1;i++){
        cout<<prefix[i]<<" ";
    }
    int m;//测试数量
    cin>>m;
    for(int i=0;i<m;i++){
        int l = 0;
        cin>>l;
        int r;
        cin>>r;
        cout<<prefix[r] - prefix[l-1]<<endl;
    }
    //system("pause");
    return 0;
}