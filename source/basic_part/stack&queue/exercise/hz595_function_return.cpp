/* 题目描述
? 众所周知，计算机程序中通常含有许多的函数调用，而调用关系往往是嵌套的，
也就是说被调用的函数可能会调用另一个函数，这导致我们常常在debug的时候遇到困难，并希望能弄清楚其上层的一系列调用关系。
? 在这道题目中，我们会给定一篇代码，并希望你能找到指定函数第一次被调用时的调用链，
将其打印出来；当然，你有可能会发现给定的函数没有在代码中出现，那么你应该打印一行“NOT REFERENCED”并结束你的程序。

? 为了降低难度，给定的代码是经过极度简化的，
它只包括函数调用和返回语句（表示退出这层调用），
并且没有任何额外的语法格式。

输入
? 第一行是一个数字 N，代表代码共有 N 行；　
? 接下来的 N 行，第 i+1 行是一个字符串 S[i]，代表第 i 行代码：　
? 　　1. 这行代码是一个函数调用，那么它的形式类似“fun()”；　
? 　　2. 这行代码是返回语句，它的内容固定为“return”；　
? 第 N+2 行是一个字符串，代表欲寻找到的函数。　
? （0<N≤100000，0<|S[i]|≤110；给定的被调用函数名保证合法，其一定以“()”结尾并只由大小写字母和下划线组成）

输出
? 输出一行：
　　1. 如果指定的函数在代码中出现了，那么打印出其调用关系链，用“->”连接；
　　2. 否则，打印一行“NOT REFERENCED”。
样例输入
5
fun1()
fun2()
return
fun3()
fun4()
fun4()
样例输出
fun1()->fun3()->fun4()
 */

//程序调用关系
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;
class Solution{
public:
    string findCallChain(vector<string> ops, string target){
        vector<string> stack;

        for(int i = 0; i < (int)ops.size(); i++){
            if(ops[i] == "return"){
                if(!stack.empty()){
                    stack.pop_back();
                }
            }else{
                stack.push_back(ops[i]);
                if(ops[i] == target){
                    string ans;
                    for(int j = 0; j < (int)stack.size(); j++){
                        if(j != 0) ans += "->";
                        ans += stack[j];
                    }
                    return ans;
                }
            }
        }

        return "NOT REFERENCED";
    }

    void f(){
        int n;
        cin >> n;
        vector<string> ops(n);
        for(int i = 0; i < n; i++){
            cin >> ops[i];
        }

        string target;
        cin >> target;
        cout << findCallChain(ops, target) << endl;
    }
};
void test01(){
    Solution s;

    struct Case{
        string name;
        vector<string> ops;
        string target;
        string expected;
    };

    vector<Case> cases = {
        {"sample", {"fun1()", "fun2()", "return", "fun3()", "fun4()"}, "fun4()", "fun1()->fun3()->fun4()"},
        {"single call", {"main()"}, "main()", "main()"},
        {"not found", {"main()", "work()", "return"}, "target()", "NOT REFERENCED"},
        {"after return", {"root()", "left()", "return", "right()"}, "right()", "root()->right()"},
        {"first target", {"A()", "target()", "return", "target()"}, "target()", "A()->target()"},
        {"deep chain", {"A()", "B()", "C()", "D()"}, "D()", "A()->B()->C()->D()"}
    };

    cout << "+------+--------------+-------+------------+--------------------------+--------------------------+----------+" << endl;
    cout << "| Case | Name         | Lines | Target     | Expected                 | Actual                   | Result   |" << endl;
    cout << "+------+--------------+-------+------------+--------------------------+--------------------------+----------+" << endl;

    int passCount = 0;
    for(int i = 0; i < (int)cases.size(); i++){
        string actual = s.findCallChain(cases[i].ops, cases[i].target);
        bool pass = (actual == cases[i].expected);
        if(pass) passCount++;

        cout << "| ";
        cout.width(4);
        cout << left << i + 1 << " | ";
        cout.width(12);
        cout << left << cases[i].name << " | ";
        cout.width(5);
        cout << left << cases[i].ops.size() << " | ";
        cout.width(10);
        cout << left << cases[i].target << " | ";
        cout.width(24);
        cout << left << cases[i].expected << " | ";
        cout.width(24);
        cout << left << actual << " | ";
        cout.width(8);
        cout << left << (pass ? "PASS" : "FAIL") << " |" << endl;
    }

    cout << "+------+--------------+-------+------------+--------------------------+--------------------------+----------+" << endl;
    cout << "Passed: " << passCount << " / " << cases.size() << endl;
}
int main(void){
    test01();
    system("pause");
    return 0;
}