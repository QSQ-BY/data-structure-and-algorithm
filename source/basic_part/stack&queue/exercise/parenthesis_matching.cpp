/* 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，
判断字符串是否有效。

有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
每个右括号都有一个对应的相同类型的左括号。

示例 1：
输入：s = "()"
输出：true

示例 2：
输入：s = "()[]{}"
输出：true

示例 3：
输入：s = "(]"
输出：false

示例 4：
输入：s = "([])"
输出：true

示例 5：
输入：s = "([)]"
输出：false
 */


//力扣第20题-有效的括号
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;
class Solution{
public:
    bool match(char a,char b){
        if(a=='(' and b==')') return true;
        else if(a=='[' and b==']') return true;
        else if(a=='{' and b=='}') return true;
        else return false;

        return false;
    }
    bool isValid(string s){
        //使用栈的结构进行模拟
        //遇到左括号就入栈，遇到右括号检查是否与栈顶的括号匹配
        string stack;
        int top = -1;
        if(s.size()==1) return false;
        if(s[0] == ')' or s[0] == ']' or s[0] == '}') return false;
        if(s.empty()) return false;
        for(int i = 0;i<s.size();i++){
            if(s[i]=='(' or s[i]=='{' or s[i]=='['){
                stack.push_back(s[i]);
                top++;
            }else if(s[i]==')' or s[i]==']' or s[i]=='}'){
                if(top == -1) return false;
                if(match(stack[top], s[i])){
                    stack.pop_back();
                    top--;
                }else{
                    return false;
                }       
            }
        }
        if(top == -1) return true;
        else return false;
    }
};


void test01(){
    Solution s;

    vector<string> inputs = {
        "()",
        "()[]{}",
        "(]",
        "([])",
        "([)]",
        ")",
        "(((",
        "({[]})",
        "({[)]}"
    };

    vector<bool> expected = {
        true,
        true,
        false,
        true,
        false,
        false,
        false,
        true,
        false
    };

    cout << boolalpha;
    cout << "+------+------------+----------+----------+----------+" << endl;
    cout << "| Case | Input      | Expected | Actual   | Result   |" << endl;
    cout << "+------+------------+----------+----------+----------+" << endl;

    int pass_count = 0;
    for(int i = 0; i < (int)inputs.size(); i++){
        bool actual = s.isValid(inputs[i]);
        bool pass = (actual == expected[i]);
        pass_count += pass;

        cout << "| ";
        cout.width(4);
        cout << left << i + 1 << " | ";
        cout.width(10);
        cout << left << inputs[i] << " | ";
        cout.width(8);
        cout << left << expected[i] << " | ";
        cout.width(8);
        cout << left << actual << " | ";
        cout.width(8);
        cout << left << (pass ? "PASS" : "FAIL") << " |" << endl;
    }

    cout << "+------+------------+----------+----------+----------+" << endl;
    cout << "Passed: " << pass_count << " / " << inputs.size() << endl;
}

int main(void){
    test01();
    system("pause");
    return 0;
}