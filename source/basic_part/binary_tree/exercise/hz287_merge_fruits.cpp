/* 题目描述
? 在一个果园里，多多已经将所有的果子打了下来，
而且按果子的不同种类分成了不同的堆。
多多决定把所有的果子合成一堆。
? 每一次合并，多多可以把两堆果子合并到一起，消耗的体力等于两堆果子的重量之和。
可以看出，所有的果子经过 n?1 次合并之后，就只剩下一堆了。
多多在合并果子时总共消耗的体力等于每次合并所耗体力之和。
? 因为还要花大力气把这些果子搬回家，
所以多多在合并果子时要尽可能地节省体力。
假定每个果子重量都为 1，并且已知果子的种类数和每种果子的数目，
你的任务是设计出合并的次序方案，使多多耗费的体力最少，并输出这个最小的体力耗费值。
? 例如有 3 种果子，数目依次为 1，2，9。
可以先将 1、2 堆合并，新堆数目为 3，耗费体力为 3。
接着，将新堆与原先的第三堆合并，又得到新的堆，数目为 12，耗费体力为 12。
所以多多总共耗费体力为 3+12=15。可以证明 15 为最小的体力耗费值。
输入
? 输入包括两行，第一行是一个整数 n(1≤n≤10000)，表示果子的种类数。
? 第二行包含 n 个整数，用空格分隔，第 i 个整数 ai(1≤ai≤20000) 是第 i 种果子的数目。
输出
? 输出包括一行，这一行只包含一个整数，也就是最小的体力耗费值。输入数据保证这个值小于 231。
样例输入
3
1 2 9
样例输出
15
 */

//哈夫曼编码
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
using namespace std;

void test01(){
    int N = 0;
    cin>>N;
    vector<int> weight(N);
    for(int i =0;i<N;i++){
        cin>>weight[i];
    }
    if(N==1){
        cout<<0<<endl;
        return;
    }
    int ans = 0;
    for(int i =0;i<N-1;i++){
        sort(weight.rbegin(),weight.rend());
        int temp_weight = 0;
        temp_weight = weight[weight.size()-1] + weight[weight.size()-2];
        ans += temp_weight;
        weight[weight.size()-2] = temp_weight;
        weight.pop_back();
    }
    cout<<ans<<endl;
    return;
}

typedef pair<int,int> PII;

void test02(){
    //数字*数字在二叉树中的路径深度
    int n;
    cin>>n;
    set<PII> s;//*s.begin()返回集合中的最小值,且不允许有重复元素
    //把果子得数量和果子得编号进行打包防止过滤重复元素
    for(int i=0,num;i<n;i++){
        cin>>num;
        s.insert(PII(num,i));//果子数量和果子编号
    }
    int ans=0;
    for(int i=1;i<n;i++){
        int a = s.begin()->first;
        s.erase(s.begin());
        int b = s.begin()->first;
        s.erase(s.begin());
        ans+=a+b;
        s.insert(PII(a+b,n+i));
    }
    cout<<ans<<endl;
    return;
}

int main(void){
    test02();
    system("pause");
    return 0;
}