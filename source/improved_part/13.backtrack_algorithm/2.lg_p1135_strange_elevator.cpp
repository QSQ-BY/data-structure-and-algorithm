/* 题目描述
呵呵，有一天我做了一个梦，梦见了一种很奇怪的电梯。大楼的每一层楼都可以停电梯，而且第 i 层楼（1≤i≤N）上有一个数字 K 
i
?
 （0≤K 
i
?
 ≤N）。电梯只有四个按钮：开，关，上，下。上下的层数等于当前楼层上的那个数字。当然，如果不能满足要求，相应的按钮就会失灵。例如：3,3,1,2,5 代表了 K 
i
?
 （K 
1
?
 =3，K 
2
?
 =3，……），从 1 楼开始。在 1 楼，按“上”可以到 4 楼，按“下”是不起作用的，因为没有 ?2 楼。那么，从 A 楼到 B 楼至少要按几次按钮呢？

输入格式
共二行。

第一行为三个用空格隔开的正整数，表示 N,A,B（1≤N≤200，1≤A,B≤N）。

第二行为 N 个用空格隔开的非负整数，表示 K 
i
?
 。

输出格式
一行，即最少按键次数，若无法到达，则输出 -1。

输入输出样例
输入 #1复制

5 1 5
3 3 1 2 5
输出 #1复制

3 */
#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>
using namespace std;
vector<int> arr;
vector<int> dis;//表示起点到达每个点的最短距离
//当前一共走了几步，当前层号，目标层号，总的楼层数量n
void dfs(int cnt,int cur,int target,int n){
    //历史答案剪枝
    if(dis[cur] <= cnt) return;
    else dis[cur] = cnt;
    if(cur + arr[cur] <=n) dfs(cnt+1,cur+arr[cur],target,n);
    if(cur - arr[cur] >=1) dfs(cnt+1,cur-arr[cur],target,n);
    return;
}

int main(void){
    int N;//总楼数
    int A;//第一层
    int B;//最后一层
    cin>>N>>A>>B;
    arr.push_back(0);
    dis.push_back(N+1);
    for(int i=0;i<N;i++){
        int number;
        scanf("%d",&number);
        arr.push_back(number);
        dis.push_back(N+1);
    }

    dfs(0,A,B,N);
    if(dis[B] == N+1) printf("-1\n");
    else printf("%d\n",dis[B]);
    //system("pause");
    return 0;
}