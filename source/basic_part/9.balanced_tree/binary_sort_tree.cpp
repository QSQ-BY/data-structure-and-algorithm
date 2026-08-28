/* 二叉排序树/二叉搜索树
左子树<根节点
右子树>根节点
二叉排序树中序遍历的结果是有序的 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <stdbool.h>

typedef struct Node{
    int key;
    struct Node* lchild;
    struct Node* rchild;
}Node;

#define KEY(n) (n ? n->key : -1)


Node* get_new_node(int key){
    Node* p = (Node*)malloc(sizeof(Node));
    p->key = key;
    p->lchild = p->rchild = nullptr;
    return p;
}

//插入节点操作
Node* insert(Node* root,int key){
    if(root == nullptr) return get_new_node(key);
    if(key == root->key) return root;
    if(key<root->key) root->lchild = insert(root->lchild,key);
    else root->rchild = insert(root->rchild,key);
    return root;
}

//寻找节点前驱
Node* pre(Node* root){
    if(root==nullptr) return root;
    Node* temp = root->lchild;
    while(temp->rchild!=nullptr) temp=temp->rchild;
    return temp;
}

//删除节点操作
Node* erase(Node* root,int key){
    if(root == nullptr) return root;
    if(key<root->key) root->lchild = erase(root->lchild,key);
    else if(key > root->key) root->rchild = erase(root->rchild,key);
    else if(root->key = key){
        //度为0 1 2的情况
        if(root->lchild == nullptr and root->rchild == nullptr){
            free(root);
            return nullptr;
        }else if(root->rchild == nullptr or root->lchild == nullptr){
            Node* temp = nullptr;
            if(root->lchild != nullptr) temp = root->lchild;
            else if(root->rchild != nullptr)temp = root->rchild;
            free(root);
            return temp;
        }else if(root->rchild!=nullptr and root->lchild!=nullptr){
            //将根节点前驱的值和进行交换
            Node* temp = pre(root);
            root->key = temp->key;
            root->lchild = erase(root->lchild,temp->key);
        }
    }
    return root;
}

//清理二叉排序树操作
void clear(Node* root){
    if(root == nullptr) return;
    if(root->lchild == nullptr and root->rchild == nullptr) free(root);
    clear(root->lchild);
    clear(root->rchild);
    return;
}

void output(Node* root){
    if(root == nullptr) return;
    printf("(%d;%d,%d)\n",KEY(root),KEY(root->lchild),KEY(root->rchild));
    output(root->lchild);
    output(root->rchild);
    return;
}

void inorder(Node* root){
    if(root == nullptr) return;
    inorder(root->lchild);
    printf("%d ",root->key);
    inorder(root->rchild);
    return;
}

void test01(){
    #define MAX_OP 10
    Node* root = nullptr;
    for(int i=0;i<MAX_OP;i++){
        int key = rand()%100;
        printf("将%d插入二叉排序树\n",key);
        root = insert(root,key);
    }
    output(root);
    printf("中序遍历：");
    inorder(root);
    printf("\n\n");

    int x = 0;
    while(~scanf("%d",&x)){
        printf("从二叉排序树中移除%d\n",x);
        root = erase(root,x);
        output(root);
        inorder(root);
        printf("\n\n");
    }
    return;
}

int main(void){
    srand(time(0));
    test01();
    system("pause");
    return 0;
}