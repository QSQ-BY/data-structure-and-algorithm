//反转二叉树
/* 给你一棵二叉树的根节点 root ，
翻转这棵二叉树，并返回其根节点。
示例 1：
输入：root = [4,2,7,1,3,6,9]
输出：[4,7,2,9,6,3,1]
示例 2：
输入：root = [2,1,3]
输出：[2,3,1]
示例 3：
输入：root = []
输出：[] */
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
    TreeNode* invertTree(TreeNode* root) {
        if(root == nullptr) return nullptr;
        swap(root->left,root->right);
        root->left = invertTree(root->left);
        root->right = invertTree(root->right);
        return root;
    }
};

class Solution2{
public:
    TreeNode* invertTree2(TreeNode* root){
        if(root==nullptr) return nullptr;
        swap(root->left,root->right);
        root->left = invertTree2(root->left);
        root->right = invertTree2(root->right);
        return root;
    }
};

string treeToString(TreeNode* root){
    if(root == nullptr) return "#";
    return to_string(root->val) + "(" + treeToString(root->left) + "," + treeToString(root->right) + ")";
}

void deleteTree(TreeNode* root){
    if(root == nullptr) return;
    deleteTree(root->left);
    deleteTree(root->right);
    delete root;
}

void test01(){
    Solution s;

    TreeNode* roots[4];
    string expected[4];
    string names[4] = {"empty","single","example1","small"};

    roots[0] = nullptr;
    expected[0] = "#";

    roots[1] = new TreeNode(1);
    expected[1] = "1(#,#)";

    roots[2] = new TreeNode(4);
    roots[2]->left = new TreeNode(2);
    roots[2]->right = new TreeNode(7);
    roots[2]->left->left = new TreeNode(1);
    roots[2]->left->right = new TreeNode(3);
    roots[2]->right->left = new TreeNode(6);
    roots[2]->right->right = new TreeNode(9);
    expected[2] = "4(7(9(#,#),6(#,#)),2(3(#,#),1(#,#)))";

    roots[3] = new TreeNode(2);
    roots[3]->left = new TreeNode(1);
    roots[3]->right = new TreeNode(3);
    expected[3] = "2(3(#,#),1(#,#))";

    cout << boolalpha;
    cout << "+------+----------+-----------------------------------------+-----------------------------------------+-------+" << endl;
    cout << "| Case | Name     | Expected                                | Actual                                  | Pass  |" << endl;
    cout << "+------+----------+-----------------------------------------+-----------------------------------------+-------+" << endl;

    for(int i=0;i<4;i++){
        TreeNode* root = s.invertTree(roots[i]);
        string actual = treeToString(root);
        bool pass = actual == expected[i];

        cout << "| ";
        cout.width(4);
        cout << left << i + 1 << " | ";
        cout.width(8);
        cout << left << names[i] << " | ";
        cout.width(39);
        cout << left << expected[i] << " | ";
        cout.width(39);
        cout << left << actual << " | ";
        cout.width(5);
        cout << left << pass << " |" << endl;

        deleteTree(root);
    }

    cout << "+------+----------+-----------------------------------------+-----------------------------------------+-------+" << endl;
}

int main(void){
    test01();
    system("pause");
    return 0;
}