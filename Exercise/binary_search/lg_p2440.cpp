/* 题目背景
要保护环境。

题目描述
木材厂有 n 根原木，现在想把这些木头切割成 k 段长度均为 l 的小段木头（木头有可能有剩余）。

当然，我们希望得到的小段木头越长越好，请求出 l 的最大值。

木头长度的单位是 cm，原木的长度都是正整数，我们要求切割得到的小段木头的长度也是正整数。

例如有两根原木长度分别为 11 和 21，要求切割成等长的 6 段，很明显能切割出来的小段木头长度最长为 5。

输入格式
第一行是两个正整数 n,k，分别表示原木的数量，需要得到的小段的数量。

接下来 n 行，每行一个正整数 L
i
?
 ，表示一根原木的长度。

输出格式
仅一行，即 l 的最大值。

如果连 1cm 长的小段都切不出来，输出 0。

输入输出样例
输入 #1复制

3 7
232
124
456
输出 #1复制

114 */
#include <iostream>
#include <vector>
#include <set>
#include <climits>
#include <algorithm>
using namespace std;
vector<long long > arr;
long long  n;
long long  k;

//判断整个数组能否切成k段长度为len的小块
long long  check(long long  len){
    long long  result = 0;
    for(long long  i=0;i<arr.size();i++){
        result += arr[i]/len;
        if(result >= k){
            return 1;
        }
    }
    return 0;
}
int main(void){
    cin>>n>>k;
    long long  max_len = INT_MIN;
    long long  sum = 0;
    for(long long  i=0;i<n;i++){
        long long  number;
        cin>>number;
        arr.push_back(number);
        max_len = max(number,max_len);
        sum+=number;
    }
    if(sum < k){
        cout<<0<<endl;
        return 0;
    }
    long long  left = 1;
    long long  right = max_len;
    while(left < right){
        long long  mid = left + (right-left)/2;
        if(check(mid) == 1) left = mid+1;
        else if(check(mid) == 0) right = mid;
    }
    cout<<left-1<<endl;
    //system("pause");
    return 0;
}