#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <unordered_map>
#include <unordered_set>
#include <stack>
#include <queue>

#define MAX_N 10
using namespace std;
//二叉树中序遍历转非递归形式
class Node{
public:
    Node(int key){
        this->key = key;
        this->lchild = nullptr;
        this->rchild = nullptr;
    }
    int key;
    Node* lchild;
    Node* rchild;
};

Node* insert(int key, Node* root) {
    if (root == nullptr) return new Node(key);
    if (rand() % 2 == 0)
        root->lchild = insert(key, root->lchild);
    else
        root->rchild = insert(key, root->rchild);
    return root;
}

Node* get_binary_tree(int n){
    Node* root = nullptr;
    for(int i=0;i<n;i++){
        int val = rand()%100;
        root = insert(val,root);
    }
    return root;
}

void inorder(Node* root){
    if(root==nullptr) return; //scode=0
    inorder(root->lchild);    //scode=1
    printf("%d ",root->key);  //scode=2
    inorder(root->rchild);    //scode=3
    return;                   //scode=4
}

class Data{
public:
    Data(Node* root){
        this->root = root;
        this->scode = 0;
    }
    Node* root;
    int scode;
};

void non_inorder(Node* root){
    stack<Data> s;
    Data d(root);
    s.push(d);
    while(!s.empty()){
        Data& cur_data = s.top();
        switch(cur_data.scode){
            case 0:{
                if(cur_data.root==nullptr) s.pop();
                else cur_data.scode = 1;
            };break;
            case 1:{
                Data new_data(cur_data.root->lchild);
                s.push(new_data);
                cur_data.scode =2;
            };break;
            case 2:{
                printf("%d ",cur_data.root->key);
                cur_data.scode = 3;
            };break;
            case 3:{
                Data new_data(cur_data.root->rchild);
                s.push(new_data);
                cur_data.scode = 4;
            };break;
            case 4:{
                s.pop();
            };break;
        }
    }
    return;
}

void test01(){
    Node* root = get_binary_tree(MAX_N);
    inorder(root);
    cout<<endl;
    non_inorder(root);
    cout<<endl;
    return;
}

int main(void){
    test01();
    system("pause");
    return 0;
}