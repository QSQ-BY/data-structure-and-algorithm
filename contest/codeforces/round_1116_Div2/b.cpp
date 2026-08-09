#include <iostream>
#include <string>
#include <vector>

using namespace std;

// 检查给定的子序列 fits 哪种交替模式（0101... 或 1010...）
// 返回合法的模式数量 (0, 1, 或 2)
int countValidPatterns(const string& seq) {
    bool can_be_pattern_01 = true; // 期待序列: 0, 1, 0, 1, 0, 1 ...
    bool can_be_pattern_10 = true; // 期待序列: 1, 0, 1, 0, 1, 0 ...
    for (int i = 0; i < seq.length(); ++i) {
        if (seq[i] == '?') continue;

        char expected_01 = (i % 2 == 0) ? '0' : '1';
        char expected_10 = (i % 2 == 0) ? '1' : '0';

        if (seq[i] != expected_01) can_be_pattern_01 = false;
        if (seq[i] != expected_10) can_be_pattern_10 = false;
    }
    return (can_be_pattern_01 ? 1 : 0) + (can_be_pattern_10 ? 1 : 0);
}

void solve() {
    int n;
    cin >> n;
    string s;
    cin >> s;

    // 1. 拆分为奇数下标子序列和偶数下标子序列
    string odd_indexed_seq = "";
    string even_indexed_seq = "";

    for (int i = 0; i < n; ++i) {
        if (i % 2 == 0) {
            odd_indexed_seq += s[i];   // 下标 0, 2, 4, ...
        } else {
            even_indexed_seq += s[i];  // 下标 1, 3, 5, ...
        }
    }

    // 2. 分别计算奇数与偶数位置的合法方案数
    long long odd_ways = countValidPatterns(odd_indexed_seq);
    long long even_ways = countValidPatterns(even_indexed_seq);

    // 3. 独立事件根据乘法原理计算总方案数
    long long total_ways = (odd_ways * even_ways) % 998244353;
    cout << total_ways << "\n";
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}