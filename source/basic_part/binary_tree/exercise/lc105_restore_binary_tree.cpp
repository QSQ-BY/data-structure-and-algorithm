/* 给定两个整数数组 preorder 和 inorder ，
其中 preorder 是二叉树的先序遍历， 
inorder 是同一棵树的中序遍历，
请构造二叉树并返回其根节点。

示例 1:
输入: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
输出: [3,9,20,null,null,15,7]
示例 2:
输入: preorder = [-1], inorder = [-1]
输出: [-1]
 */
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
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
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        if(preorder.size() == 0 or inorder.size() == 0) return nullptr;
        int pos = 0;//中序遍历根节点位置
        int n = preorder.size();
        while(inorder[pos]!= preorder[0]) pos++;
        TreeNode* root = new TreeNode(preorder[0]);
        vector<int> pre_arr,in_arr;
        for(int i=1;i<=pos;i++) pre_arr.push_back(preorder[i]);
        for(int i=0;i<=pos-1;i++) in_arr.push_back(inorder[i]);
        root->left = buildTree(pre_arr,in_arr);
        pre_arr.clear();
        in_arr.clear();
        for(int i = pos+1;i<n;i++) pre_arr.push_back(preorder[i]);
        for(int i = pos+1;i<n;i++) in_arr.push_back(inorder[i]);
        root->right = buildTree(pre_arr,in_arr);
        return root;
    }
};


class Solution2{
    public:
    TreeNode* build_tree(vector<int> preorder,vector<int> inorder){
        if(preorder.size()==0 or inorder.size()==0) return nullptr;
        int pos = 0;
        while(preorder[0]!=inorder[pos]) pos++;
        int n = preorder.size();
        TreeNode* root = new TreeNode(preorder[0]);
        vector<int> pre_arr;
        vector<int> in_arr;
        for(int i =1;i<=pos;i++){
            pre_arr.push_back(preorder[i]);
        }
        for(int i = 0;i<=pos-1;i++){
            in_arr.push_back(inorder[i]);
        }
        root->left = build_tree(pre_arr,in_arr);
        pre_arr.clear();
        in_arr.clear();
        for(int i = pos+1;i<n;i++){
            pre_arr.push_back(preorder[i]);
        }
        for(int i = pos+1;i<n;i++){
            in_arr.push_back(inorder[i]);
        }
        root->right = build_tree(pre_arr,in_arr);
        return root;
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

void getPreorder(TreeNode* root,vector<int>& arr){
    if(root == nullptr) return;
    arr.push_back(root->val);
    getPreorder(root->left,arr);
    getPreorder(root->right,arr);
}

void getInorder(TreeNode* root,vector<int>& arr){
    if(root == nullptr) return;
    getInorder(root->left,arr);
    arr.push_back(root->val);
    getInorder(root->right,arr);
}

void deleteTree(TreeNode* root){
    if(root == nullptr) return;
    deleteTree(root->left);
    deleteTree(root->right);
    delete root;
}

void test01(){
    Solution s;

    vector<int> preorderCases[5] = {
        {},
        {-1},
        {3,9,20,15,7},
        {1,2,3,4},
        {1,2,3,4}
    };
    vector<int> inorderCases[5] = {
        {},
        {-1},
        {9,3,15,20,7},
        {4,3,2,1},
        {1,2,3,4}
    };
    string names[5] = {"empty","single","example1","left_chain","right_chain"};

    cout << boolalpha;
    cout << "+------+-------------+-----------------+-----------------+-----------------+-----------------+-------+" << endl;
    cout << "| Case | Name        | Preorder        | ActualPre       | Inorder         | ActualIn        | Pass  |" << endl;
    cout << "+------+-------------+-----------------+-----------------+-----------------+-----------------+-------+" << endl;

    for(int i=0;i<5;i++){
        vector<int> pre = preorderCases[i];
        vector<int> in = inorderCases[i];
        TreeNode* root = s.buildTree(pre,in);
        vector<int> actualPre;
        vector<int> actualIn;

        getPreorder(root,actualPre);
        getInorder(root,actualIn);
        bool pass = actualPre == preorderCases[i] && actualIn == inorderCases[i];

        cout << "| ";
        cout.width(4);
        cout << left << i + 1 << " | ";
        cout.width(11);
        cout << left << names[i] << " | ";
        cout.width(15);
        cout << left << vectorToString(preorderCases[i]) << " | ";
        cout.width(15);
        cout << left << vectorToString(actualPre) << " | ";
        cout.width(15);
        cout << left << vectorToString(inorderCases[i]) << " | ";
        cout.width(15);
        cout << left << vectorToString(actualIn) << " | ";
        cout.width(5);
        cout << left << pass << " |" << endl;

        deleteTree(root);
    }

    cout << "+------+-------------+-----------------+-----------------+-----------------+-----------------+-------+" << endl;
}

int main(void){
    test01();
    system("pause");
    return 0;
}