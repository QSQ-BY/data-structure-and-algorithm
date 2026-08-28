/* 已知 n 个整数 x 
1
?
 ,x 
2
?
 ,?,x 
n
?
 ，以及 1 个整数 k（k<n）。从 n 个整数中任选 k 个整数相加，可分别得到一系列的和。例如当 n=4，k=3，4 个整数分别为 3,7,12,19 时，可得全部的组合与它们的和为：

3+7+12=22

3+7+19=29

7+12+19=38

3+12+19=34

现在，要求你计算出和为素数共有多少种。

例如上例，只有一种的和为素数：3+7+19=29。

输入格式
第一行两个空格隔开的整数 n,k（1≤n≤20，k<n）。

第二行 n 个整数，分别为 x 
1
?
 ,x 
2
?
 ,?,x 
n
?
 （1≤x 
i
?
 ≤5×10 
6
 ）。

输出格式
输出一个整数，表示种类数。

输入输出样例
输入 #1复制

4 3
3 7 12 19
输出 #1复制

1 */

#include <iostream>
#include <vector>
#include <algorithm>
#include <vector>
using namespace std;
vector<int> arr;
long long ans = 0;

int is_prime(int x){
    for(int i=2;i*i <= x;i++){
        if(x%i == 0) return 0;
    }
    return 1;
}
//当前选取的数字位置pos，当前选择的数字的最小下标min，
// 数字总数n，最多选择的数字个数max,当前所选的数字的和sum
void dfs(int pos,int min,int n,int max,int sum){
    if(pos >= max) {
        if(is_prime(sum) == 1) ans++;
        return;
    }
    for(int i = min;i<n;i++){
        dfs(pos + 1,i+1,n,max,sum+arr[i]);
    }
}

int main(void){
    int n;
    int k;
    cin>>n>>k;
    for(int i=0;i<n;i++){
        int number;
        scanf("%d",&number);
        arr.push_back(number);
    }
    dfs(0,0,n,k,0);
    printf("%lld\n",ans);
    //system("pause");
    return 0;
}