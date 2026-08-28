/* 一个如下的 6×6 的跳棋棋盘，
有六个棋子被放置在棋盘上，
使得每行、每列有且只有一个，
每条对角线（包括两条主对角线的所有平行线）
上至多有一个棋子。
上面的布局可以用序列 2 4 6 1 3 5 来描述，
第 i 个数字表示在第 i 行的相应位置有一个棋子，如下：
行号 1 2 3 4 5 6
列号 2 4 6 1 3 5
这只是棋子放置的一个解。
请编一个程序找出所有棋子放置的解。
并把它们以上面的序列方法输出，解按字典顺序排列。
请输出前 3 个解。最后一行是解的总个数。
输入格式
一行一个正整数 n，表示棋盘是 n×n 大小的。
输出格式
前三行为前三个解，
每个解的两个数字之间用一个空格隔开。
第四行只有一个数字，表示解的总数。
输入输出样例
输入 #1复制
6
输出 #1复制
2 4 6 1 3 5
3 6 2 5 1 4
4 1 5 2 6 3
4 */
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <unordered_map>
#include <unordered_set>
#include <stack>
#include <queue>
#include <deque>
#include <climits>

using namespace std;
#define MASK(n) (((1)<<((n)+(1))) - (2))//掩码
unordered_map<int,int> ind;//从位权到编号的映射
int total_ans = 3;
int arr[20];
void print_one_result(int n){
    for(int i=1;i<=n;i++){
        if(i>1) printf(" ");
        printf("%d",arr[i]);
    }
    printf("\n");
    total_ans--;
    return;
}

//当前正在分配第几行的皇后，每一行的状态码，每一斜行与反斜行的状态码,棋盘长宽n
int dfs(int i,int t1,int t2,int t3,int n){
    if(i==n + 1){
        if(total_ans > 0) print_one_result(n);
        return 1;
    }
    int ans = 0;
    for(int t = t1;t!=0;t -= (-t&t)){
        int j = ind[(-t&t)];
        if((t2 & (1<<(i + j - 1))) and (t3&(1<<(i-j+n)))){
            arr[i] = j;
            ans += dfs(i+1,t1^(1<<j),t2^(1<<(i+j-1 )),t3^(1<<i-j+n),n);
        }
    }
    return ans;
}

void test01(){
    int n;//在n*n棋盘上放置n个皇后
    cin>>n;
    for(int i=0;i<2*n;i++) ind[1<<i] = i;
    int ans = dfs(1,MASK(n),MASK(2*n-1),MASK(2*n-1),n);
    printf("%d\n",ans);
    return;
}


class Solution {
public:
    vector<int> arr;//第i行的皇后放置到了j号位置
    vector<vector<string>> ans;

    vector<vector<string>> solveNQueens(int n) {
        ans.clear();
        arr.assign(n, 0);
        dfs2(n,0);
        return ans;
    }

    void addRes(int n){
        vector<string> temp;
        for(int i=0;i<n;i++){
            string s;
            for(int j=0;j<n;j++){
                if(j == arr[i]) s.push_back('Q');
                else s.push_back('.');
            }
            temp.push_back(s);
        }
        ans.push_back(temp);
    }

    //r表示当前放置的是第几行的皇后
    void dfs2(int n,int r){
        if(r >= n){
            addRes(n);
            return;
        }
        //把当前这一行的皇后摆好
        for(int i=0;i<n;i++){
            arr[r] = i;
            if(check(r)) dfs2(n,r+1);
        }
    }

    bool check(int r){
        for(int i=0;i<r;i++){
            if(arr[i] == arr[r] or abs(i-r) == abs(arr[i]-arr[r])){
                return false;
            }
        }
        return true;
    }
};

int main(void){
    test01();
    //system("pause");
    return 0;
}