/* 给定两棵二叉树 tree1 和 tree2，判断 tree2 
是否以 tree1 的某个节点为根的子树具有
相同的结构和节点值 。
注意，空树 不会是以 tree1 的某个节点为根的子树具有 相同的结构和节点值 。
示例 1：
输入：tree1 = [1,7,5], tree2 = [6,1]
输出：false
解释：tree2 与 tree1 的一个子树没有相同的结构和节点值。
示例 2：
输入：tree1 = [3,6,7,1,8], tree2 = [6,1]
输出：true
解释：tree2 与 tree1 的一个子树拥有相同的结构和节点值。即 6 - > 1。
 */

#include <iostream>
#include <vector>
#include <algorithm>
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

class Solution {
public:
    bool match(TreeNode* A,TreeNode* B){
        if(A==nullptr) return B==nullptr;
        if(B==nullptr) return true;
        if(A->val != B->val) return false;
        if(A->val == B->val){
            return (match(A->left,B->left) and match(A->right,B->right));
        }
        return false;
    }

    bool isSubStructure(TreeNode* A, TreeNode* B) {
        if(A==nullptr and B==nullptr) return false;
        if(A==nullptr) return B==nullptr;
        if(B==nullptr) return false;
        if(A->val == B->val and (match(A,B))) return true;
        if(A->left and isSubStructure(A->left,B)) return true;
        if(A->right and isSubStructure(A->right,B)) return true;
        return false;
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