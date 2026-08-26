#include <algorithm>
#include <array>
#include <iostream>
#include <vector>

using namespace std;

constexpr int MAX_K = 50;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int k = 0;
    int capacity_limit = 0;
    int item_count = 0;
    cin >> k >> capacity_limit >> item_count;

    // dp[capacity] 按价值从大到小保存恰好装满该容量的前 K 优解。
    vector<array<long long, MAX_K>> dp(capacity_limit + 1);
    vector<int> solution_count(capacity_limit + 1, 0);
    solution_count[0] = 1;
    dp[0][0] = 0;

    for (int item = 0; item < item_count; ++item) {
        int weight = 0;
        long long value = 0;
        cin >> weight >> value;

        // 倒序枚举容量，保证当前物品最多选择一次。
        for (int capacity = capacity_limit; capacity >= weight; --capacity) {
            const int not_take_count = solution_count[capacity];
            const int take_count = solution_count[capacity - weight];
            const int merged_count = min(k, not_take_count + take_count);

            array<long long, MAX_K> merged{};
            int not_take_index = 0;
            int take_index = 0;

            for (int index = 0; index < merged_count; ++index) {
                const bool choose_not_take =
                    take_index >= take_count ||
                    (not_take_index < not_take_count &&
                    dp[capacity][not_take_index] >=
                        dp[capacity - weight][take_index] + value);

                if (choose_not_take) {
                    merged[index] = dp[capacity][not_take_index];
                    ++not_take_index;
                } else {
                    merged[index] = dp[capacity - weight][take_index] + value;
                    ++take_index;
                }
            }

            copy_n(merged.begin(), merged_count, dp[capacity].begin());
            solution_count[capacity] = merged_count;
        }
    }

    long long answer = 0;
    for (int index = 0; index < solution_count[capacity_limit]; ++index) {
        answer += dp[capacity_limit][index];
    }
    cout << answer << '\n';

    return 0;
}
