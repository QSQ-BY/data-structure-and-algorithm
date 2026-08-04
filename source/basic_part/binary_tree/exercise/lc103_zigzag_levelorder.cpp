/* 给你二叉树的根节点 root ，返回其节点值的 锯齿形层序遍历 。
（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
示例 1：
输入：root = [3,9,20,null,null,15,7]
输出：[[3],[20,9],[15,7]]
示例 2：
输入：root = [1]
输出：[[1]]
示例 3：
输入：root = []
输出：[] */

#include <iostream>
#include <vector>
#include <algorithm>
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

//先进行正常的层序遍历，最后再把偶数行的结果翻转
class Solution{
public:
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        if(root == nullptr) return vector<vector<int>>();
        vector<vector<int>> ans;
        queue<TreeNode*> q;
        q.push(root);
        while(!q.empty()){
            TreeNode* node = nullptr;
            int cnt = q.size();
            vector<int> temp;
            for(int i = 0;i<cnt;i++){
                node = q.front();
                if(node->left) q.push(node->left);
                if(node->right) q.push(node->right);
                temp.push_back(node->val);
                q.pop();
            }
            ans.push_back(temp);
        }
        for(int i=0;i<ans.size();i++){
            if(i%2 == 1) reverse(ans[i].begin(),ans[i].end());
        }
        return ans;
    }



    void dfs(TreeNode* root,int level,vector<vector<int>>& ans){
        if(root ==nullptr) return;
        if(level == ans.size()) ans.push_back(vector<int>());
        ans[level].push_back(root->val);
        if(root->left) dfs(root->left,level+1,ans);
        if(root->right) dfs(root->right,level+1,ans);
        return;
    }

    vector<vector<int>> zigzagLevelOrder2(TreeNode* root){
        if(root==nullptr) return vector<vector<int>>();
        vector<vector<int>> ans;
        int level = 0;
        dfs(root,level,ans);
        for(int i=0;i<ans.size();i++){
            if(i%2==1) reverse(ans[i].begin(),ans[i].end());
        }
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