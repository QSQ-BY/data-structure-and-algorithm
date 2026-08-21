/* 
题目背景
这次不是数列的问题了。
题目描述
给定一个 n 行 m 列的矩阵 a，有 q 次询问，每次给定 (u,v) 和 (x,y)，请你求出：
( 
i=u
∑
x
?
  
j=v
∑
y
?
 a 
i,j
?
 )mod2 
64
 
也就是求出以 (u,v) 为左上角、(x,y) 为右下角的矩形元素和对 2 
64
  取余数的结果。
输入式
本题单测试点内有多组测试数据。
输入的第一行是一个整数 T，表示数据组数。接下来依次给出每组数据的输入信息：
第一行三个整数，依次表示矩阵的行数 n 和列数 m 以及询问数 q。
接下来 n 行，每行 m 个整数。第 i 行第 j 个整数表示 a 
i,j
。
接下来 q 行，每行四个整数，依次为 u,v,x,y，表示一组询问。
输出格式
为了避免输出过大，对于每组数据，请输出一行一个整数，表示本组数据的所有询问的答案的按位异或和。
输入输出样例
输入 #1复制
2
3 3 3
1 2 3
4 5 6
7 8 9
1 1 3 3
2 1 2 2
1 2 2 3
2 2 1
1 3
4 6
2 2 2 2
输出 #1复制
52
6 */
#include <iostream>
#include <vector>
using namespace std;
int main(void){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;//测试数据数
    cin>>T;
    for(int i=0;i<T;i++){
        int n;//行数
        int m;//列数
        int q;//询问数
        cin>>n>>m>>q;
        vector<vector<unsigned long long>> prefix(
            n+1,vector<unsigned long long>(m+1,0)
        );
        for(int j=1;j<=n;j++){
            for(int k=1;k<=m;k++){
                unsigned long long number;
                cin>>number;
                prefix[j][k] = number
                            + prefix[j-1][k]
                            + prefix[j][k-1]
                            - prefix[j-1][k-1];
            }
        }
        unsigned long long ans = 0;

        for(int j=0;j<q;j++){
            int u,v,x,y;
            cin>>u>>v>>x>>y;
            unsigned long long temp_ans = prefix[x][y]
                                        - prefix[u-1][y]
                                        - prefix[x][v-1]
                                        + prefix[u-1][v-1];

            ans = ans^temp_ans;
        }
        cout<<ans<<endl;
    }

    //system("pause");
    return 0;
}
