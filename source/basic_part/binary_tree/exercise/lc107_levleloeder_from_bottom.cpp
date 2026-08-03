/* 给你二叉树的根节点 root ，返回其节点值 自底向上的层序遍历 。 
（即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）
示例 1：
输入：root = [3,9,20,null,null,15,7]
输出：[[15,7],[9,20],[3]]
示例 2：
输入：root = [1]
输出：[[1]]
示例 3：
输入：root = []
输出：[] */

//Definition for a binary tree node.


#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

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
    vector<vector<int>> levelOrderBottom(TreeNode* root) {
        if(root == nullptr) return vector<vector<int>>();
        vector<vector<int>> ans_positive;
        vector<vector<int>> ans_negative;
        queue<TreeNode*> q;
        q.push(root);
        while(q.empty() == 0){
            vector<int> temp;
            int cnt = q.size();
            for(int i=0;i<cnt;i++){
                TreeNode* node = q.front();
                if(node->left) q.push(node->left);
                if(node->right) q.push(node->right);
                temp.push_back(node->val);
                q.pop();
            }
            ans_positive.push_back(temp);
        }
        /* for(int i = ans_positive.size()-1;i>=0;i++){
            ans_negative.push_back(ans_positive[i]);
        }
        return ans_negative; */
        reverse(ans_positive.begin(),ans_positive.end());
        return ans_positive;
    }

    void dfs(TreeNode* root,int level,vector<vector<int>>& ans){
        //root、level是传入参数
        //ans是传出参数
        if(root == nullptr) return;
        if(level == ans.size()) ans.push_back(vector<int>());
        ans[level].push_back(root->val);
        if(root->left) dfs(root->left,level+1,ans);
        if(root->right) dfs(root->right,level+1,ans);
        return;
    }

    vector<vector<int>> levelOrderBottom2(TreeNode* root){
        if(root == nullptr) return vector<vector<int>>();
        int level = 0;//层数
        vector<vector<int>> ans;
        dfs(root,level,ans);
        reverse(ans.begin(),ans.end());
        return ans;
    }
};

void test01(){
    Solution s;
}

int main(void){
    test01();
    system("pause");
    return 0;
}