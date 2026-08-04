/* 给定 s 和 t 两个字符串，
当它们分别被输入到空白的文本编辑器后，
如果两者相等，返回 true 。
# 代表退格字符。
注意：如果对空文本输入退格字符，文本继续为空。
示例 1：
输入：s = "ab#c", t = "ad#c"
输出：true
解释：s 和 t 都会变成 "ac"。
示例 2：
输入：s = "ab##", t = "c#d#"
输出：true
解释：s 和 t 都会变成 ""。
示例 3：
输入：s = "a#c", t = "b"
输出：false
解释：s 会变成 "c"，但 t 仍然是 "b"。 */
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;
class Solution{
public:
    string restore(string s){
        string stack{};//使用栈去模拟
        int top{-1};
        for(int i=0;i<s.size();i++){
            if(top==-1 and s[i] == '#'){
                continue;
            }else if(s[i] == '#' and i!=-1){
                stack.pop_back();
                top--;
            }else{
                top++;
                stack.push_back(s[i]);
            }
        }
        return stack;
    }

    bool backspaceCompare(string s,string t){
        string true_s{};
        string true_t{};
        true_s = restore(s);
        true_t = restore(t);
        if(true_s == true_t) return true;
        else return false;
    }
};
void test01(){
    Solution s;

    vector<string> left_input{
        "ab#c",
        "ab##",
        "a#c",
        "#a",
        "a##c",
        "xywrrmp"
    };
    vector<string> right_input{
        "ad#c",
        "c#d#",
        "b",
        "a",
        "#a#c",
        "xywrrmu#p"
    };
    vector<bool> expected{
        true,
        true,
        false,
        true,
        true,
        true
    };

    cout << boolalpha;
    cout << "+------+------------+------------+----------+----------+--------+" << endl;
    cout << "| Case | s          | t          | Expected | Actual   | Result |" << endl;
    cout << "+------+------------+------------+----------+----------+--------+" << endl;

    for(int i = 0; i < left_input.size(); i++){
        bool actual = s.backspaceCompare(left_input[i], right_input[i]);

        cout << "| ";
        cout.width(4);
        cout << left << i + 1 << " | ";
        cout.width(10);
        cout << left << left_input[i] << " | ";
        cout.width(10);
        cout << left << right_input[i] << " | ";
        cout.width(8);
        cout << left << expected[i] << " | ";
        cout.width(8);
        cout << left << actual << " | ";
        cout.width(6);
        cout << left << (actual == expected[i] ? "PASS" : "FAIL") << " |" << endl;
    }

    cout << "+------+------------+------------+----------+----------+--------+" << endl;
}

int main(void){
    test01();
    system("pause");
    return 0;
}