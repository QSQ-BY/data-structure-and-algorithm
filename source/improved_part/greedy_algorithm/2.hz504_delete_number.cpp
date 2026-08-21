/* 题目描述
? 输入一个高精度的正整数 n（长度不大于 240 位），去掉其中任意 s 个数字后剩下的数字按原左右次序将组成一个新的正整数，现求一种方案，使得新的正整数数值最小。
输入
? 第一行一个整数 n。
? 第二行一个正整数 s。
输出
? 输出一个数表示最小值，输出时忽略数字的前导零。
样例输入1
179566
4
样例输出1
15
样例输入2
903071
3
样例输出2
1 */
#include <iostream>
#include <string>
#include <vector>
using namespace std;
int main(void){
    string number;
    cin>>number;
    int m;
    cin>>m;
    for(int i=0;i<m;i++){
        int j=0;
        int temp = number.size();
        for(int j=0;j<number.size()-1;j++){
            if(number[j+1] < number[j]){
                number.erase(number.begin()+j);
                break;
            }
        }
        if(number.size() == temp){
            number.erase(number.end() - 1);
        }
    }
    while(number.size() > 1 and number[0] == '0'){
        number.erase(number.begin());
    }
    cout<<number<<endl;

    //system("pause");
    return 0;
}