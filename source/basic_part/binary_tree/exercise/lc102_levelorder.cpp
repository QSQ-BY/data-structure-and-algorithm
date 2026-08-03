/* 给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 
（即逐层地，从左到右访问所有节点）。
示例 1：
输入：root = [3,9,20,null,null,15,7]
输出：[[3],[9,20],[15,7]]
示例 2：
输入：root = [1]
输出：[[1]]
示例 3：
输入：root = []
输出：[]
 */

 //二叉树的层序遍历
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <queue>
using namespace std;

//Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};


class Solution{
public:
    vector<vector<int>> levelOrder1(TreeNode* root) {
        if(root == nullptr) return vector<vector<int>>();
        TreeNode* node;
        queue<TreeNode *> q;
        q.push(root);
        vector<vector<int>> ans;
        while(!q.empty()){
            int cnt = q.size();
            vector<int> temp;
            for(int i=0;i<cnt;i++){
                node = q.front();
                temp.push_back(node->val);
                if(node->left) q.push(node->left);
                if(node->right) q.push(node->right);
                q.pop();
            }
            ans.push_back(temp);
        }
        return ans;
    }

//使用栈（深度遍历）完成层序遍历
    void dfs(TreeNode* root,int level,vector<vector<int>>& ans){
        //level表示当前节点的层数
        if(root == nullptr) return;
        if(level == (int)ans.size()) ans.push_back(vector<int>());
        ans[level].push_back(root->val);
        dfs(root->left,level+1,ans);
        dfs(root->right,level+1,ans);
    }

    vector<vector<int>> levelOrder2(TreeNode* root){
        if(root == nullptr) return vector<vector<int>>();
        vector<vector<int>> ans;
        dfs(root,0,ans);
        return ans;
    }
};

string vectorToString(vector<int> arr){
    string s = "[";
    for(int i=0;i<(int)arr.size();i++){
        if(i) s += ",";
        s += to_string(arr[i]);
    }
    s += "]";
    return s;
}

string matrixToString(vector<vector<int>> arr){
    string s = "[";
    for(int i=0;i<(int)arr.size();i++){
        if(i) s += ",";
        s += vectorToString(arr[i]);
    }
    s += "]";
    return s;
}

void deleteTree(TreeNode* root){
    if(root == nullptr) return;
    deleteTree(root->left);
    deleteTree(root->right);
    delete root;
}





class Solution2{
    public:
    vector<vector<int>> level_order(TreeNode* root){
        if(root == nullptr) return vector<vector<int>>();
        vector<vector<int>> ans;
        queue<TreeNode*> q;
        q.push(root);
        while(q.empty()==0){
            vector<int> temp;
            int cnt = q.size();
            for(int i = 0;i<cnt;i++){
                TreeNode* node = q.front();
                temp.push_back(node->val);
                if(node->left) q.push(node->left);
                if(node->right) q.push(node->right);
                q.pop();
            }
            ans.push_back(temp);
        }
        return ans;
    }

    void dfs(TreeNode* root,int level,vector<vector<int>>& ans){
        if(root == nullptr) return;
        if(level == ans.size()) ans.push_back(vector<int>());//每次访问到边界层数的时候都新建一个空容器，否则访问会越界
        ans[level].push_back(root->val);
        if(root->left) dfs(root->left,level+1,ans);
        if(root->right) dfs(root->right,level+1,ans);
        return;
    }

    vector<vector<int>> level_order2(TreeNode* root){
        if(root == nullptr) return vector<vector<int>>();
        int level = 0;
        vector<vector<int>> ans;
        dfs(root,level,ans);
        return ans;
    }

    /* vector<vector<int>> level_order(TreeNode* root){
        if(root == nullptr) return vector<vector<int>>();
        vector<vector<int>> ans;
        queue<TreeNode*> q;
        q.push(root);
        while(q.empty()==0){
            vector<int> temp;
            int cnt = q.size();
            for(int i =0;i<cnt;i++){
                TreeNode* node = q.front();
                temp.push_back(node->val);
                if(node->left) q.push(node->left);
                if(node->right) q.push(node->right);
                q.pop();
            }
            ans.push_back(temp);
        }
        return ans;
    } */
};




void test01(){
    Solution s;

    TreeNode* roots[4];
    vector<vector<int>> expected[4];
    string names[4] = {"empty","single","example1","left_chain"};

    roots[0] = nullptr;
    expected[0] = {};

    roots[1] = new TreeNode(1);
    expected[1] = {{1}};

    roots[2] = new TreeNode(3);
    roots[2]->left = new TreeNode(9);
    roots[2]->right = new TreeNode(20);
    roots[2]->right->left = new TreeNode(15);
    roots[2]->right->right = new TreeNode(7);
    expected[2] = {{3},{9,20},{15,7}};

    roots[3] = new TreeNode(1);
    roots[3]->left = new TreeNode(2);
    roots[3]->left->left = new TreeNode(3);
    roots[3]->left->left->left = new TreeNode(4);
    expected[3] = {{1},{2},{3},{4}};

    cout << boolalpha;
    cout << "+------+------------+-----------------------+-----------------------+-----------------------+-------+" << endl;
    cout << "| Case | Name       | Expected              | BFS                   | DFS                   | Pass  |" << endl;
    cout << "+------+------------+-----------------------+-----------------------+-----------------------+-------+" << endl;

    for(int i=0;i<4;i++){
        vector<vector<int>> actual1 = s.levelOrder1(roots[i]);
        vector<vector<int>> actual2 = s.levelOrder2(roots[i]);
        bool pass = actual1 == expected[i] && actual2 == expected[i];

        cout << "| ";
        cout.width(4);
        cout << left << i + 1 << " | ";
        cout.width(10);
        cout << left << names[i] << " | ";
        cout.width(21);
        cout << left << matrixToString(expected[i]) << " | ";
        cout.width(21);
        cout << left << matrixToString(actual1) << " | ";
        cout.width(21);
        cout << left << matrixToString(actual2) << " | ";
        cout.width(5);
        cout << left << pass << " |" << endl;
    }

    cout << "+------+------------+-----------------------+-----------------------+-----------------------+-------+" << endl;

    for(int i=0;i<4;i++){
        deleteTree(roots[i]);
    }
}

int main(void){
    test01();
    system("pause");
    return 0;
}