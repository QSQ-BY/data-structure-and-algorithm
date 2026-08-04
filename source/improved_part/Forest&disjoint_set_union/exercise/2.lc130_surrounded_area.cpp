/* 给你一个 m x n 的矩阵 board ，由若干字符 'X' 和 'O' 组成，
捕获 所有 被围绕的区域：
连接：一个单元格与水平或垂直方向上相邻的单元格连接。
区域：连接所有 'O' 的单元格来形成一个区域。
围绕：如果一个区域中的所有 'O' 单元格都不在棋盘的边缘，
则该区域被包围。这样的区域 完全 被 'X' 单元格包围。
通过 原地 将输入矩阵中的所有 'O' 替换为 'X' 来 捕获被围绕的区域。
你不需要返回任何值。

示例 1：
输入：board = [
['X','X','X','X'],
['X','O','O','X'],
['X','X','O','X'],
['X','O','X','X']]

输出：[
['X','X','X','X'],
['X','X','X','X'],
['X','X','X','X'],
['X','O','X','X']]
解释：
在上图中，底部的区域没有被捕获，
因为它在 board 的边缘并且不能被围绕。
示例 2：
输入：board = [['X']]
输出：[['X']] */
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

class UnionSet{
public:
    UnionSet(int n){
        for(int i=0;i<=n;i++){
            father.push_back(i);
            size.push_back(1);
        }
    }

    int find(int x){
        if(father[x] == x) return x;
        return father[x] = find(father[x]);
    }

    void merge(int a,int b){
        int set_a = find(a);
        int set_b = find(b);
        if(set_a == set_b) return;
        if(size[set_a] < size[set_b]){
            father[set_a] = set_b;
            size[set_b]+=size[set_a];
        }else{
            father[set_b] = set_a;
            size[set_a]+=size[set_b];
        }
        return;
    }

    int is_connected(int a,int b){
        if(find(a) == find(b)) return 1;
        else if(find(a) !=find(b)) return 0;
        return 0;
    }

    vector<int> father;
    vector<int> size;
};
class Solution{
public:
    //坐标映射到下标-> y*n+x+1
    void solve(vector<vector<char>>& board) {
        int m = board.size();//m是纵向长度
        int n = board[0].size();//n是横向长度
        UnionSet u(m*n);
        for(int i=0;i<m;i++){
            for(int j = 0;j<n;j++){
                //i是纵坐标y，j是横坐标x
                int index = i*n+j+1;
                if(board[i][j] != 'O') continue;
                if(i==0 or i==m-1) u.merge(index,0);
                if(j==0 or j==n-1) u.merge(index,0);
                if(j+1<n and board[i][j+1] == 'O') u.merge(index,index+1);
                if(i+1<m and board[i+1][j] == 'O') u.merge(index,index+n);
            }
        }
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                if(board[i][j] != 'O') continue;
                int index = i*n+j+1;
                if(u.find(index) != u.find(0)) board[i][j] = 'X';
            }
        }
    }
};
void test01(){

}

int main(void){
    test01();
    system("pause");
    return 0;
}