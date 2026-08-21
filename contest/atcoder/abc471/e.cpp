/* Problem Statement  问题描述
There are 
N balls numbered 
1 to 
N. Ball 
i has an integer 
A 
i
?
  written on it.
一共有 
N 个球，它们的编号分别是 
1 到 
N 。第 
i 个球上写着整数 
A 
i
?
  。

For a way of choosing some balls from the 
N balls, define the score of that choice as the square of the sum of the numbers written on the chosen balls.
对于从 
N 个球中选取若干个球的方法，将该选取方式的得分定义为所选球上数字之和的平方。

Find the sum, modulo 
998244353, of the scores of all 
( 
K
N
?
 ) ways of choosing 
K balls from the 
N balls.
求从 
N 个球中以 
( 
K
N
?
 ) 种方式选出 
K 个球的得分之和，结果对 
998244353 取模。 */
#include <iostream>
#include <vector>

using namespace std;

const int MOD = 998244353;

vector<long long> val;
vector<int> permutation;
int n, k;
long long ans = 0;

// 结算当前选中的 K 个球的得分
void calculate_result() {
    long long temp_ans = 0;
    
    // 将选出的 K 个球的值相加并取模
    for (int i = 0; i < k; i++) {
        int index = permutation[i];
        temp_ans = (temp_ans + val[index]) % MOD;
    }
    
    // 计算和的平方并取模
    long long score = (temp_ans * temp_ans) % MOD;
    
    // 累加到总得分中
    ans = (ans + score) % MOD;
}

// DFS 搜索所有选出 K 个球的组合
// pos: 当前选了第几个球 (从 0 到 k-1)
// min_idx: 当前位置可选的最小球编号 (从 1 到 n)
void dfs(int pos, int min_idx) {
    // 递归基：如果已经选满了 K 个球，计算得分并返回
    if (pos == k) {
        calculate_result();
        return;
    }
    
    // 剪枝：如果剩余可选的球数量少于还需要的球数量，直接返回
    if (n - min_idx + 1 < k - pos) {
        return;
    }

    for (int i = min_idx; i <= n; i++) {
        permutation.push_back(i);
        dfs(pos + 1, i + 1);  // 递归选择下一个球，编号必须大于当前球 (保证组合不重复)
        permutation.pop_back(); // 回溯
    }
}

void test01() {
    cin >> n >> k;
    
    // 1-based 下标对齐
    val.resize(n + 1);
    for (int i = 1; i <= n; i++) {
        long long number;
        cin >> number;
        // 防止输入负数，规整到 [0, MOD-1] 范围内
        val[i] = (number % MOD + MOD) % MOD;
    }

    // 从第 0 个位置开始选，最小选第 1 号球
    dfs(0, 1);

    cout << ans << endl;
}

int main(void) {
    test01();
    return 0;
}