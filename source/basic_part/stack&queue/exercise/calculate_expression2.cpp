#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <climits>
#include <cmath>
using namespace std;
#define INF 0x3f3f3f3f
class Solution
{
public:
    bool isOperator(char c)
    {
        return c == '+' || c == '-' || c == '*' || c == '/' || c == '^';
    }

    bool isLeftBracket(char c)
    {
        return c == '(';
    }

    bool isUnarySign(string &s, int l, int pos)
    {
        if (s[pos] != '+' && s[pos] != '-')
            return false;
        if (pos == l)
            return true;
        return isLeftBracket(s[pos - 1]) || isOperator(s[pos - 1]);
    }

    int calculate(string &s, int l, int r)
    {
        // l、r表示区间范围
        int pos = -1;
        int min_weight{INF};
        int cur_weight;
        int temp_weight{0};
        for (int i = l; i < r; i++)
        {
            cur_weight = 0;
            switch (s[i])
            {
            case '(':
                temp_weight += 100;
                break;
            case ')':
                temp_weight -= 100;
                break;
            case '+':
            case '-':
                if (isUnarySign(s, l, i))
                    break;
                cur_weight = 1 + temp_weight;
                break;
            case '*':
            case '/':
                cur_weight = temp_weight + 2;
                break;
            case '^':
                cur_weight = 3 + temp_weight;
                break;
            default:
                break;
            }
            if (cur_weight > 0 and
                (cur_weight < min_weight or (cur_weight == min_weight and s[i] != '^')))
            {
                min_weight = cur_weight;
                pos = i;
            }
        }
        // 处理纯数字的情况
        if (pos == -1)
        {
            int num{0};
            int sign{1};
            for (int i = l; i < r; i++)
            {
                if (s[i] == '-' && isUnarySign(s, l, i))
                {
                    sign = -sign;
                    continue;
                }
                if (s[i] == '+' && isUnarySign(s, l, i))
                    continue;
                if (s[i] < '0' or s[i] > '9')
                    continue;
                num = num * 10 + (s[i] - '0');
            }
            return sign * num;
        }
        int num1 = calculate(s, l, pos);
        int num2 = calculate(s, pos + 1, r);
        switch (s[pos])
        {
        case '*':
            return num1 * num2;
            break;
        case '-':
            return num1 - num2;
            break;
        case '+':
            return num1 + num2;
            break;
        case '/':
            return num1 / num2;
            break;
        case '^':
            return pow(num1, num2);
            break;
        default:
            return 0;
        }
        return 0;
    }
};


//测试代码
void test01()
{
    Solution s;
    vector<string> inputs = {
        "123",
        "-9",
        "1+2",
        "7-10",
        "3+4*5",
        "8/4/2",
        "1-2-3",
        "9/-9",
        "-6*7+8",
        "51+89-56--78",
        "56--78",
        "56+-78",
        "56-+78",
        "56++78",
        "2^3",
        "2*3^2",
        "2^3^2",
        "(1+2)",
        "((1+2)*3)",
        "(2+2)^(1+1)"
    };

    vector<int> expected = {
        123,
        -9,
        3,
        -3,
        23,
        1,
        -4,
        -1,
        -34,
        162,
        134,
        -22,
        -22,
        134,
        8,
        18,
        512,
        3,
        9,
        16
    };

    cout << "+------+----------------------+----------+----------+----------+" << endl;
    cout << "| Case | Expression           | Expected | Actual   | Result   |" << endl;
    cout << "+------+----------------------+----------+----------+----------+" << endl;

    int pass_count = 0;
    for (int i = 0; i < (int)inputs.size(); i++)
    {
        string expression = inputs[i];
        int actual = s.calculate(expression, 0, expression.size());
        bool pass = (actual == expected[i]);
        pass_count += pass;

        cout << "| ";
        cout.width(4);
        cout << left << i + 1 << " | ";
        cout.width(20);
        cout << left << inputs[i] << " | ";
        cout.width(8);
        cout << left << expected[i] << " | ";
        cout.width(8);
        cout << left << actual << " | ";
        cout.width(8);
        cout << left << (pass ? "PASS" : "FAIL") << " |" << endl;
    }

    cout << "+------+----------------------+----------+----------+----------+" << endl;
    cout << "Passed: " << pass_count << " / " << inputs.size() << endl;
}
//调试代码
void test02()
{
    Solution s;
    string str;
    cin >> str;
    cout << s.calculate(str, 0, str.size()) << endl;
}

int main(void)
{
    //test01();
    test02();
    //system("pause");
    return 0;
}