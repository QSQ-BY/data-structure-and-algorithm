/* 有 n 个城市，其中一些彼此相连，另一些没有相连。
如果城市 a 与城市 b 直接相连，
且城市 b 与城市 c 直接相连，
那么城市 a 与城市 c 间接相连。
省份 是一组直接或间接相连的城市，组内不含其他没有相连的城市。
给你一个 n x n 的矩阵 isConnected ，
其中 isConnected[i][j] = 1 表示第 i 个城市和第 j 个城市直接相连，
而 isConnected[i][j] = 0 表示二者不直接相连。
返回矩阵中 省份 的数量。
示例 1：
输入：isConnected = [
[1,1,0],
[1,1,0],
[0,0,1]]
输出：2
示例 2：
输入：isConnected = [[1,0,0],[0,1,0],[0,0,1]]
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
        for(int i=0;i<n;i++){
            father.push_back(i);
            size.push_back(1);
        }
        this->element_num = n;
        this->collection_num = n;
    }

    int find(int x){
        if(father[x] == x) return x;
        return father[x] = find(father[x]);
    }

    int merge(int a,int b){
        int set_a = find(a);
        int set_b = find(b);
        if(set_a == set_b) return 0;
        if(size[set_a] < size[set_b]){
            father[set_a] = set_b;
            size[set_b] += size[set_a];
        }else{
            father[set_b] = set_a;
            size[set_a] += size[set_b];
        }
        collection_num--;
        return 1;
    }

    int merge(const vector<int>& nums){
        int merged = 0;
        for(vector<int>::size_type i = 1;i < nums.size();i++){
            if(merge(nums[0],nums[i])) merged = 1;
        }
        return merged;
    }

    void insert(){
        father.push_back(element_num);
        size.push_back(1);
        element_num++;
        collection_num++;
    }

    int restore(int index){
        int root = find(index);
        if(size[root] == 1) return 0;

        vector<int> members;
        for(int i = 0;i < element_num;i++){
            if(i != index && find(i) == root){
                members.push_back(i);
            }
        }

        int new_root = members[0];
        for(int member:members){
            father[member] = new_root;
            size[member] = 1;
        }
        size[new_root] = static_cast<int>(members.size());
        father[index] = index;
        size[index] = 1;
        collection_num++;
        return 1;
    }

    int is_connected(int a,int b){
        return find(a) == find(b);
    }

    int all_connected(const vector<int>& nodes) {
        if (nodes.empty()) return 1;
        int root = find(nodes[0]);
        for (vector<int>::size_type i = 1; i < nodes.size(); i++) {
            if (find(nodes[i]) != root) {
                return 0;
            }
        }
        return 1;
    }

    vector<int> father;
    vector<int> size;
    int element_num;
    int collection_num;
};

class Solution{
public:
    int findCircleNum(vector<vector<int>>& isConnected) {
        int m = isConnected.size();//纵向长度
        int n = isConnected[0].size();//横向长度
        UnionSet u(n);
        for(int i=0;i<m;i++){//i是纵坐标
            for(int j=0;j<n;j++){//j是横坐标
                int index = i+j*n;
                if(isConnected[i][j] == 1) u.merge(i,j);
            }
        }
        return u.collection_num;
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