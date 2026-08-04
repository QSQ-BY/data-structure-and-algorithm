/* 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，
请你计算网格中岛屿的数量。
岛屿总是被水包围，
并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
此外，你可以假设该网格的四条边均被水包围。
示例 1：
输入：grid = [
['1','1','1','1','0'],
['1','1','0','1','0'],
['1','1','0','0','0'],
['0','0','0','0','0']
]
输出：1
示例 2：
输入：grid = [
['1','1','0','0','0'],
['1','1','0','0','0'],
['0','0','1','0','0'],
['0','0','0','1','1']
]
输出：3 */

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

    int merge(int a,int b){
        int set_a = find(a);
        int set_b = find(b);
        if(set_a == set_b) return 0;
        if(set_a < set_b){
            father[set_a] = set_b;
            size[set_b]+=size[set_a];
        }
        else{
            father[set_b] = set_a;
            size[set_a]+=set_b;
        }
        return 1;
    }

    vector<int> father;
    vector<int> size;
};
class Solution{
public:
    int numIslands(vector<vector<char>>& grid) {
        int m = grid.size();//纵向长度
        int n = grid[0].size();//横向长度
        UnionSet u(n*m);
        for(int i=0;i<m;i++){
            for(int j = 0;j<n;j++){
                //i为纵坐标
                //j为横坐标
                if(grid[i][j] == '0') continue;
                int index = j+1+i*n;
                if(j+1<n and grid[i][j+1] == '1') u.merge(index,index+1);
                if(i+1<m and grid[i+1][j] == '1') u.merge(index,index+n);
            }
        }
        int ans = 0;
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                int index = j+1+i*n;
                if(grid[i][j] == '1' and u.find(index) == index) ans++;
            }
        }
        return ans;
    }
};
void test01(){
    return;
}

int main(void){
    test01();
    system("pause");
    return 0;
}