/* 给定一个 n 叉树的根节点  root ，
返回 其节点值的 前序遍历 。
n 叉树 在输入中按层序遍历进行序列化表示，
每组子节点由空值 null 分隔（请参见示例）。
示例 1：
输入：root = [1,null,3,2,4,null,5,6]
输出：[1,3,5,6,2,4]
示例 2：
输入：root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
输出：[1,2,3,6,7,11,14,4,8,12,5,9,13,10]
 */

// Definition for a Node.

//N插树的前序遍历
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
class Solution{
public:
    void __preorder(Node* root,vector<int>& ans){
        if(root==nullptr) return;
        ans.push_back(root->val);
        for(auto x:root->children){
            __preorder(x,ans);
        }
        return;
    }
    vector<int> preorder(Node* root) {
        if(root == nullptr) return vector<int>();
        vector<int> ans;
        __preorder(root,ans);
        return ans;
    }

    vector<int> preorder_2(Node* root){
        if(root == nullptr) return vector<int>();
        vector<int> ans;
        ans.push_back(root->val);
        for(auto x:root->children){
            vector<int> temp = preorder_2(x);
            for(auto y:temp){
                ans.push_back(y);
            }
        }
        return ans;
    }
};

class Solution2{
public:
    vector<int> preorder(Node* root){
        if(root == nullptr) return vector<int>();
        vector<int> ans;
        ans.push_back(root->val);
        for(auto x:root->children){
            vector<int> temp;
            temp = preorder(x);
            for(auto y:temp){
                ans.push_back(y);
            }
        }
        return ans;
    }

    void __preorder2(Node* root,vector<int>& ans){
        if(root == nullptr) return;
        ans.push_back(root->val);
        for(auto x:root->children){
            __preorder2(x,ans);
        }
        return;
    }
    vector<int> preorder2(Node* root){
        if(root == nullptr) return vector<int>();
        vector<int> ans;
        __preorder2(root,ans);
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

void deleteTree(Node* root){
    if(root == nullptr) return;
    for(auto child:root->children){
        deleteTree(child);
    }
    delete root;
}

void test01(){
    Solution s;

    Node* roots[4];
    vector<int> expected[4];
    string names[4] = {"empty","single","example1","wide"};

    roots[0] = nullptr;
    expected[0] = {};

    roots[1] = new Node(1);
    expected[1] = {1};

    Node* node5 = new Node(5);
    Node* node6 = new Node(6);
    Node* node3 = new Node(3,{node5,node6});
    Node* node2 = new Node(2);
    Node* node4 = new Node(4);
    roots[2] = new Node(1,{node3,node2,node4});
    expected[2] = {1,3,5,6,2,4};

    Node* node7 = new Node(7);
    Node* node8 = new Node(8);
    Node* node9 = new Node(9);
    Node* node10 = new Node(10);
    roots[3] = new Node(1,{new Node(2),new Node(3,{node7,node8}),new Node(4),new Node(5,{node9,node10})});
    expected[3] = {1,2,3,7,8,4,5,9,10};

    cout << boolalpha;
    cout << "+------+----------+-----------------------+-----------------------+-----------------------+-------+" << endl;
    cout << "| Case | Name     | Expected              | Preorder              | Preorder2             | Pass  |" << endl;
    cout << "+------+----------+-----------------------+-----------------------+-----------------------+-------+" << endl;

    for(int i=0;i<4;i++){
        vector<int> actual1 = s.preorder(roots[i]);
        vector<int> actual2 = s.preorder_2(roots[i]);
        bool pass = actual1 == expected[i] && actual2 == expected[i];

        cout << "| ";
        cout.width(4);
        cout << left << i + 1 << " | ";
        cout.width(8);
        cout << left << names[i] << " | ";
        cout.width(21);
        cout << left << vectorToString(expected[i]) << " | ";
        cout.width(21);
        cout << left << vectorToString(actual1) << " | ";
        cout.width(21);
        cout << left << vectorToString(actual2) << " | ";
        cout.width(5);
        cout << left << pass << " |" << endl;
    }

    cout << "+------+----------+-----------------------+-----------------------+-----------------------+-------+" << endl;

    for(int i=0;i<4;i++){
        deleteTree(roots[i]);
    }
}

int main(void){
    test01();
    system("pause");
    return 0;
}