/* 题目描述
? 一群人去旅行，要租用独木舟，每艘独木舟最多乘两人，且所有独木舟有一个统一的载重限度。给出独木舟的载重限度和每个人的体重，现求最少需要租用多少独木舟。

输入
? 第一行一个整数 w，表示独木舟的载重量。（80≤w≤200）

? 第二行一个整数 n，表示旅游人数。 （1≤n≤30000）

? 接下来 n 行，每行一个数表示 ai，即每个人的重量 （5≤ai≤w）

输出
? 输出一个数表示最少需要的独木舟数量。

样例输入
100
9
90
20
20
30
50
60
70
80
90
样例输出
6
 */
#include <iostream>
#include <set>
#include <algorithm>
#include <vector>
using namespace std;
typedef pair<int,int> PII;
int main(void){
    int tot = 0;
    int n;
    int m;
    cin>>m>>n;
    vector<int> weight(n);
    for(int i=0;i<n;i++){
        cin>>weight[i];
    }
    sort(weight.begin(),weight.end());
    int ans = 0;
    while(!weight.empty()){
        if(weight.size() == 1){
            ans++;
            weight.clear();
            break;
        }
        int min_weight = weight[0];
        int max_weight = weight[weight.size()-1];
        if(min_weight + max_weight > m){
            weight.erase(weight.begin() + weight.size() - 1);
        }else if(min_weight + max_weight <= m){
            weight.erase(weight.begin()+ weight.size()-1);
            weight.erase(weight.begin());
        }
        ans++;
    }
    cout<<ans<<endl;
    //system("pause");
    return 0;
}