/* During a geometry lesson, Iskander got very bored, so he decided to draw in Yura's notebook. To do this, he took a row and drew horizontal lines on it. Some lines are long, some are short, and some parts of the page remain empty.
在几何课上课期间，伊斯坎德感到非常无聊，于是他决定在尤拉的本子上画画。他先画了一排水平线。有些线条很长，有些则很短，而且页面上有些地方是空白的。
The page is represented by a string s
, where the character '*' denotes an empty part of the paper, and the character '#' denotes one centimeter of a drawn line. A continuous sequence of '#' characters forms a single line.
该页面由字符串 表示，其中字符'*'表示纸张的空白部分，而字符'#'则表示一厘米长的实线。连续的'#'字符则构成一个单独的线。

Yura decided to erase all the lines and made Iskander help him: they will erase one of the lines from both ends simultaneously.
尤拉决定删除所有的线条，于是请伊斯坎德帮助他：他们打算同时从两端删除这些线条。

Each second, Iskander erases 1
 centimeter from the right end of the line, and Yura erases 1
 centimeter from the left end.
每一秒，伊斯坎德尔会从线的右端移除 厘米，而尤拉则会从线的左端移除 厘米。
If the current length of the line is 1
 or 2
 centimeters, then in the next second it is erased completely, and the process ends.
如果线条的当前长度等于 或 厘米，那么下一秒它就会完全被删除，整个过程也就结束了。
Yura wants to choose a line so that, together with Iskander, they erase it for as long as possible. Help him determine this maximum time. If there are no lines on the page, the answer is 0
 seconds.
尤拉想要选择一条线，这样与伊斯坎德一起，他们就能尽可能长时间地隐藏这条线。帮助他确定这个最大时间。如果页面上没有任何线条，那么答案就是 秒。

Input  输入
The first line contains a single integer t
(1≤t≤2500
) — the number of test cases.
第一行包含一个整数 ( )，表示测试用例的数量。
The first line of each test case contains an integer n
(1≤n≤10
) — the length of the string s
.
每个测试案例的第一行包含一个整数 ( )，表示字符串 的长度。
The second line of each test case contains a string s
of length n
, consisting of characters '#' and '*'.
每个测试案例的第二行包含一个长度为 的字符串 ，该字符串由字符'#'和'*'组成。
Output  输出结果
For each test case, output a single integer — the maximum time required to erase a line.
对于每个测试案例，输出一个整数——即擦除一行文本所需的最大时间。
Example  示例
Input  输入
5
7
#*##*##
8
########
8
********
8
#*****##
6
*#####
Output  输出结果
1
4
0
1
3 */
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <unordered_map>
#include <unordered_set>
#include <stack>
#include <queue>

using namespace std;

int f(string s,int len){
    int max_len = 0;
    int temp_len = 0;
    for(int i=0;i<len;i++){
        if(s[i]=='#') temp_len++;
        if(s[i]=='*'){
            max_len = max(temp_len,max_len);
            temp_len = 0;
        }
        if(i==s.size()-1) max_len = max(temp_len,max_len);
    }
    int ans = (max_len+1)/2;
    return ans;
}

void test01(){
    int n=0;
    cin>>n;
    vector<string> str;
    vector<int> len;
    for(int i=0;i<n;i++){
        int temp = 0;
        cin>>temp;
        len.push_back(temp);
        string s;
        cin>>s;
        str.push_back(s);
    }
    for(int i=0;i<n;i++){
        cout<<f(str[i],len[i])<<endl;
    }
}

int main(void){
    test01();
    //system("pause");
    return 0;
}