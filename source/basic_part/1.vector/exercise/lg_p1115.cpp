/* 题目描述
给出一个长度为 n 的序列 a，选出其中连续且非空的一段使得这段和最大。

输入格式
第一行是一个整数，表示序列的长度 n。

第二行有 n 个整数，第 i 个整数表示序列的第 i 个数字 a
i
?
 。

输出格式
输出一行一个整数表示答案。

输入输出样例
输入 #1复制

7
2 -4 3 -1 2 -4 3
输出 #1复制
4 */
#include <iostream>
#include <vector>
#include <climits>
using namespace std;
int main(void){
    int n;
    cin>>n;
    vector<int> prefix(n+1,0);
    for(int i=1;i<=n;i++){
        scanf("%d",&prefix[i]);
        prefix[i] += prefix[i-1];
    }
    int ans = INT_MIN;
    int right_index = 1;
    int left_index=0;
    for(right_index = 1;right_index<=n;right_index++){
        if(prefix[right_index-1] < prefix[left_index]){
            left_index = right_index-1;
        }
        ans = max(ans,prefix[right_index] - prefix[left_index]);
    }
    cout<<ans<<endl;
    //system("pause");
    return 0;
}