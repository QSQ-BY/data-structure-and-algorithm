/* 题目描述
Perket 是一种流行的美食。为了做好 Perket，厨师必须谨慎选择食材，以在保持传统风味的同时尽可能获得最全面的味道。你有 n 种可支配的配料。对于每一种配料，我们知道它们各自的酸度 s 和苦度 b。当我们添加配料时，总的酸度为每一种配料的酸度总乘积；总的苦度为每一种配料的苦度的总和。

众所周知，美食应该做到口感适中，所以我们希望选取配料，以使得酸度和苦度的绝对差最小。

另外，我们必须添加至少一种配料，因为没有任何食物是只以水为配料的。

输入格式
第一行一个整数 n，表示可供选用的食材种类数。

接下来 n 行，每行 2 个整数 s
i
?
  和 b
i
?
 ，表示第 i 种食材的酸度和苦度。

输出格式
一行一个整数，表示可能的总酸度和总苦度的最小绝对差。

输入输出样例
输入 #1复制

1
3 10
输出 #1复制

7
输入 #2复制

2
3 8
5 8
输出 #2复制

1
输入 #3复制

4
1 7
2 6
3 8
4 9
输出 #3复制

1 */

#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>
using namespace std;
vector<int> s(15);
vector<int> b(15);
int n;
vector<int> dp(70000,INT_MAX);
vector<int> ind(70000);
int ans = INT_MAX;

int calculate_result(int t){
    if(dp[t] != INT_MAX) return dp[t];
    int sum_s = 1;
    int sum_b = 0;
    int temp = t;
    for(temp = t;temp!=0;temp -=(-temp&temp)){
        int bit = -temp&temp;
        int cur_index = ind[bit];
        sum_s *= s[cur_index];
        sum_b += b[cur_index];
    }
    int result = abs(sum_s-sum_b);
    dp[t] = result;
    return result;
}

void dfs(int t) {
    // 不计算空集；已经计算过的状态不用重复搜索
    if (t == 0 or dp[t] != INT_MAX) return;
    // calculate_result 会同时把结果保存到 dp[t]
    ans = min(ans, calculate_result(t));
    // 尝试删除当前集合中的每一种食材
    for (int temp = t; temp != 0; temp -= (temp & -temp)) {
        int bit = temp & -temp;
        dfs(t ^ bit);
    }
    return;
}

int main(void){
    cin>>n;
    for(int i=0;i<n;i++){
        cin>>s[i]>>b[i];
    }
    for (int bit = 1, i = 0; i < n; i++, bit *= 2) {
        ind[bit] = i;
    }
    dfs((1 << n) - 1);
    cout<<ans<<endl;

    //system("pause");
    return 0;
}