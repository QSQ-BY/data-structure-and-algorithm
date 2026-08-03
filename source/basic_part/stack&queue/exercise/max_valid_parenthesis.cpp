/* 题目描述
? Candela 是一名漫画家，她有一个奇特的爱好，就是在纸上画括号。
这一天，刚刚起床的 Candela 画了一排括号序列，其中包含小括号 ()、中括号 [] 和大括号 {}，总长度为 N。
这排随意绘制的括号序列显得杂乱无章，于是 Candela 定义了什么样的括号序列是美观的：

1. 空的括号序列是美观的；
2. 若括号序列 `A` 是美观的，则括号序列 `(A)、[A]、{A}` 也是美观的；
3. 若括号序列 `A、B` 都是美观的，则括号序列 `AB` 也是美观的；
例如 [(){}]() 是美观的括号序列，而 )({)[}]( 则不是。

现在 Candela 想在她绘制的括号序列中，找出其中连续的一段，
满足这段子序列是美观的，并且长度尽量大。
你能帮帮她吗？

输入
? 1 个长度为 N 的括号序列。(5≤N≤10000)
输出
? 一个整数，表示最长的美观的连续子序列的长度。
样例输入
[[[[]]{}]]
样例输出
10 */

#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;
class Solution{
public:
    int max_len(vector<char> arr){
        vector<int> match(arr.size(),-1);
        vector<int> stack;
        //构建match数组，代表括号序列中的匹配关系，用下标数字表示
        for(int i=0;i<arr.size();i++){
            if(arr[i] == '(' or arr[i] == '[' or arr[i] == '{') {
                stack.push_back(i);
            }else{
                if(!stack.empty()){
                    if((arr[stack.back()] == '[' and arr[i] == ']') 
                    or (arr[stack.back()] == '(' and arr[i] == ')')
                    or (arr[stack.back()] == '{' and arr[i] == '}')
                    ){
                        match[i] = stack.back();
                        match[stack.back()] = i;
                        stack.pop_back();
                    }else{
                        stack.push_back(i);
                    }
                }
            }
        }
        //通过match整理答案
        int temp_ans{0};//当前统计值
        int ans{0};//最终答案
        int i=0;
        while(i<arr.size()){
            if(match[i]!=-1 and i<match[i]){
                //i位置含有匹配信息，记录后跳转到匹配位置，继续检索是否有连续的片段
                temp_ans = temp_ans + abs(match[i]-i)+1;
                i = match[i]+1;
            }else{
                //没有匹配信息，继续检索下一位
                temp_ans = 0;
                i++;
            }
            if(temp_ans>=ans) ans = temp_ans;
        }
        return ans;
    };
};

void test01(){
    Solution s;

    vector<string> inputs = {
        "[[[[]]{}]]",
        "()[]{}",
        "([])",
        ")([]",
        "([)]",
        "]]][[",
        "([{}])[]{}",
        "]()[{}](",
        "{[)]}()",
        "((((()",
        ")))))",
        "{}[()](())",
        "({[]})[)]{}"
    };
    vector<int> expected = {10, 6, 4, 2, 0, 0, 10, 6, 2, 2, 0, 10, 6};

    cout << "+------+--------------+----------+----------+" << endl;
    cout << "| Case | Input        | Expected | Actual   |" << endl;
    cout << "+------+--------------+----------+----------+" << endl;

    for(int i = 0; i < inputs.size(); i++){
        vector<char> arr(inputs[i].begin(), inputs[i].end());
        int actual = s.max_len(arr);

        cout << "| ";
        cout.width(4);
        cout << left << i + 1 << " | ";
        cout.width(12);
        cout << left << inputs[i] << " | ";
        cout.width(8);
        cout << left << expected[i] << " | ";
        cout.width(8);
        cout << left << actual << " |" << endl;
    }

    cout << "+------+--------------+----------+----------+" << endl;
}

int main(void){
    test01();
    system("pause");
    return 0;
}