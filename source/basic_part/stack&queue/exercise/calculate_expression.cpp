/* 题目描述
? 给出一个表达式,其中运算符仅包含 +,-,*,/,^ 要求求出表达式的最终值。
? 数据可能会出现括号情况，还有可能出现多余括号情况，忽略多余括号，正常计算即可；
输入
? 共一行，即为表达式。表达式长度不会超过1000.
输出
? 共一行，既为表达式算出的结果。
样例输入1
(2+2)^(1+1)
样例输出1
16
样例输入2
9/-9
样例输出2
-1 */

/* 思路分析：
采用表达式树结构对字符串进行重新构建
eg 3*(4+5)
      *
    |   |
    3   +
       |  |
       4  5
    左子树的结果“*”右子树的结果

1.先找到表达式树型结构的根节点（最后一个被计算的运算符）
2.把原表达式切割成两个表达式，再对两个表达式分别求值（递归）
3.使用递归函数解决

如何找到根节点：
1.括号不参与运算，会影响计算的优先级，单独进行分析
2.定义每个符号相关的权值
eg *(2)  +(1)  数字/括号(0)
3.加入括号的影响（附加权重）
从左向右扫描表达式的时候，遇到左括号，附加权重加100，遇到右括号的时候附加权重-100
eg         3     *     (     4     +     5     )
符号权重    0     2     0     0     1     0     0
附加权重    0     0     100   100   100   100   0
                       +100                    -100
真实权重          2                 101
最后得到最低的权重符号是1号位置的乘号“*”
最后按照上述递归的过程求解就行了 */



#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <climits>
using namespace std;
class Solution{
public:
    bool isLeftBracket(char c){
        return c == '(' || c == '[' || c == '{';
    }

    bool isRightBracket(char c){
        return c == ')' || c == ']' || c == '}';
    }

    bool isMatch(char left, char right){
        return (left == '(' && right == ')') ||
               (left == '[' && right == ']') ||
               (left == '{' && right == '}');
    }

    bool hasOuterBracket(const string& s){
        if(s.size() < 2 || !isMatch(s[0], s[s.size() - 1])) return false;

        vector<char> bracket_stack;
        for(int i = 0; i < (int)s.size(); i++){
            if(isLeftBracket(s[i])){
                bracket_stack.push_back(s[i]);
            }else if(isRightBracket(s[i])){
                if(bracket_stack.empty() || !isMatch(bracket_stack.back(), s[i])) return false;
                bracket_stack.pop_back();
                if(bracket_stack.empty() && i != (int)s.size() - 1) return false;
            }
        }
        return bracket_stack.empty();
    }

    int calculate(string s){
        while(hasOuterBracket(s)){
            s = s.substr(1, s.size() - 2);
        }
        vector<int> weight(s.size(),0);
        //附加权重的赋值
        int extra = 0;
        for(int i = 0; i < (int)s.size(); i++){
            if(s[i] == '(' || s[i] == '[' || s[i] == '{'){
                extra += 100;
            }else if(s[i] == ')' || s[i] == ']' || s[i] == '}'){
                extra -= 100;
            }else if(s[i] == '+' || s[i] == '-'){
                if(i == 0 || s[i - 1] == '(' || s[i - 1] == '[' || s[i - 1] == '{' ||
                s[i - 1] == '+' || s[i - 1] == '-' || s[i - 1] == '*' || s[i - 1] == '/' || s[i-1]=='^'){
                    //判断逻辑（符号的前一位是运算符或者符号在第一位）
                    continue; // 一元正负号，不当作二元运算符
                }
                weight[i] = 1 + extra;
            }else if(s[i] == '*' || s[i] == '/'){
                weight[i] = 2 + extra;
            }else if(s[i] == '^'){
                weight[i] = 3 + extra;
            }
        }
        int pos{-1};//权重最小的位置
        string new_expression1;
        string new_expression2;
        int min_weight{INT_MAX};
        for(int i = 0; i < (int)s.size(); i++){
            if(weight[i] > 0 and
            (weight[i] < min_weight or (weight[i] == min_weight and s[i] != '^'))){
                min_weight = weight[i];
                pos = i;
            }
        }
        if(pos == -1){
            int num = 0;
            int sign = 1;
            bool has_digit = false;

            for(int i = 0; i < (int)s.size(); i++){
                if(s[i] == '-'){
                    sign = -1;
                }else if(s[i] >= '0' && s[i] <= '9'){
                    has_digit = true;
                    num = num * 10 + (s[i] - '0');
                }
            }
            return sign * num;
        }
        new_expression1 = s.substr(0, pos);
        new_expression2 = s.substr(pos + 1);
        if(s[pos] == '+') return calculate(new_expression1) + calculate(new_expression2);
        else if(s[pos] == '-') return calculate(new_expression1) - calculate(new_expression2);
        else if(s[pos] == '*') return calculate(new_expression1) * calculate(new_expression2);
        else if(s[pos] == '/') return calculate(new_expression1) / calculate(new_expression2);
        else if(s[pos] == '^'){
            int a = calculate(new_expression1);
            int b = calculate(new_expression2);
            int result{1};
            for(int i=0;i<b;i++){
                result = result*a;
            }
            return result;
        }
        return 0;
    }
};
void test01(){
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
        "100/5+6*3-4",
        "2^3",
        "2*3^2",
        "2^3^2",
        "3+2^4",
        "2^3+4",
        "((123))",
        "(1+2)",
        "((1+2)*3)",
        "((2+2)^(1+1))",
        "{[2+3]*[4+1]}"
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
        34,
        8,
        18,
        512,
        19,
        12,
        123,
        3,
        9,
        16,
        25
    };

    cout << "+------+--------------------+----------+----------+----------+" << endl;
    cout << "| Case | Expression         | Expected | Actual   | Result   |" << endl;
    cout << "+------+--------------------+----------+----------+----------+" << endl;

    int pass_count = 0;
    for(int i = 0; i < (int)inputs.size(); i++){
        int actual = s.calculate(inputs[i]);
        bool pass = (actual == expected[i]);
        pass_count += pass;

        cout << "| ";
        cout.width(4);
        cout << left << i + 1 << " | ";
        cout.width(18);
        cout << left << inputs[i] << " | ";
        cout.width(8);
        cout << left << expected[i] << " | ";
        cout.width(8);
        cout << left << actual << " | ";
        cout.width(8);
        cout << left << (pass ? "PASS" : "FAIL") << " |" << endl;
    }

    cout << "+------+--------------------+----------+----------+----------+" << endl;
    cout << "Passed: " << pass_count << " / " << inputs.size() << endl;
}

void test02(){
    Solution s;
    string expression;
    cin>>expression;
    int result = s.calculate(expression);
    cout<<result<<endl;
}
int main(void){
    //test01();
    test02();
    //system("pause");
    return 0;
}