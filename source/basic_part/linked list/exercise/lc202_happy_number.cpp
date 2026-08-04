/* 编写一个算法来判断一个数 n 是不是快乐数。
「快乐数」 定义为：
对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。
然后重复这个过程直到该数变为 1，也可能进入无限循环但始终变不到 1。
如果这个过程结果为 1，那么这个数就是快乐数。
如果 n 是快乐数就返回 true；不是，则返回 false。

示例 1：
输入：n = 19
输出：true
解释：
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1

示例 2：
输入：n = 2
输出：false
 */
#include <iostream>
using namespace std;

class Solution {
public:
    int get_next(int n) {
        int next = 0;
        while (n != 0) {
            int digit = n % 10;
            next += digit * digit;
            n /= 10;
        }
        return next;
    }

    // 返回循环开始的位置：快乐数的循环入口是 1；非快乐数会返回非 1 的循环入口。
    int findCycleStart(int n) {
        if (n <= 0) return -1;

        int slow = n;
        int fast = n;

        do {
            slow = get_next(slow);
            fast = get_next(get_next(fast));
        } while (slow != fast);

        slow = n;
        while (slow != fast) {
            slow = get_next(slow);
            fast = get_next(fast);
        }

        return slow;
    }

    bool isHappy(int n) {
        return findCycleStart(n) == 1;
    }
};

void test01() {
    Solution s;

    int nums[] = {19, 2, 7, 20, 1};
    bool expected[] = {true, false, true, false, true};
    int caseCount = sizeof(nums) / sizeof(nums[0]);

    cout << boolalpha;
    cout << "+------+--------+----------+----------+-------------+" << endl;
    cout << "| Case | Input  | Expected | Actual   | Cycle Start |" << endl;
    cout << "+------+--------+----------+----------+-------------+" << endl;

    for (int i = 0; i < caseCount; i++) {
        bool actual = s.isHappy(nums[i]);
        int cycleStart = s.findCycleStart(nums[i]);

        cout << "| ";
        cout.width(4);
        cout << left << i + 1 << " | ";
        cout.width(6);
        cout << left << nums[i] << " | ";
        cout.width(8);
        cout << left << expected[i] << " | ";
        cout.width(8);
        cout << left << actual << " | ";
        cout.width(11);
        cout << left << cycleStart << " |" << endl;
    }

    cout << "+------+--------+----------+----------+-------------+" << endl;
}

int main(void) {
    test01();
    system("pause");
    return 0;
}
