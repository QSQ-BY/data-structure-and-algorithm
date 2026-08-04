//二叉树的遍历与线索化
/* 二叉树遍历：
1.前序遍历 2.中序遍历 3.后序遍历
使用前/后加上中序遍历即可还原一个二叉树
但是使用前和后序遍历无法还原一个二叉树

二叉树的线索化（废物利用）
把二叉树空下来的左指针指向该节点的前驱，
空下来的右指针指向 该节点的后继 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

typedef struct node{
    int data;
    struct node* lchild;
    struct node* rchild;
    int left_tag;
    int right_tag;//等于一即为线索，等于0就是实际的边
}node;

node* get_new_node(int data){
    node* p = (node*) malloc(sizeof(node));
    p->lchild = nullptr;
    p->rchild = nullptr;
    p->data = data;
    p->left_tag = 0;
    p->right_tag = 0;
    return p;
}

node* insert(node* root,int data){
    if(root == nullptr) return get_new_node(data);
    else{
        if(rand()%2) root->lchild = insert(root->lchild,data);
        else root->rchild = insert(root->rchild,data);
    }
    return root;
}

void clear(node* root){
    if(root == nullptr) return;
    if(root->left_tag == 0) clear(root->lchild);
    if(root->right_tag == 0) clear(root->rchild);
    free(root);
    return ;
}

//前序遍历
void pre_order(node* root){
    if(root == nullptr) return;
    printf("%d ",root->data);
    if(root->left_tag == 0) pre_order(root->lchild);
    if(root->right_tag == 0) pre_order(root->rchild);
    return ;
}

//中序遍历
void in_order(node* root){
    if(root==nullptr) return;
    if(root->left_tag == 0) in_order(root->lchild);
    //该处就是中序序列中的当前节点
    printf("%d ",root->data);//打印位置
    //我们可以在该处遍历中序遍历结果的每一个节点
    //该函数就是按照中序遍历的顺序遍历树中的每一个节点，不管对当前节点是做打印操作、赋值操作还是任何其他的操作都是按照中序遍历的顺序进行的
    //可以在该处记录该节点的前/后一个结点，建立线索化的关键信息
    if(root->right_tag == 0) in_order(root->rchild);
    return;
}

//后序遍历
void post_order(node* root){
    if(root==nullptr) return;
    if(root->left_tag == 0) post_order(root->lchild);
    if(root->right_tag == 0) post_order(root->rchild);
    printf("%d ",root->data);
    return;
}

//建立中序线索化
bool flag{false};
node* pre_node{nullptr};
node* inorder_root{nullptr};//中序遍历的第一个节点
void __build_inorder_thread(node* root){
    if(root==nullptr) return;
    if(root->left_tag == 0) __build_inorder_thread(root->lchild);
    if(flag == false) {
        inorder_root = root;
        flag = true;
    }
    //在这个位置可以访问到中序遍历的每一个节点
    if(root->lchild == nullptr){
        root->lchild = pre_node;
        root->left_tag = 1;
    }
    //如果节点的前驱存在
    if(pre_node and pre_node->rchild == nullptr){
        pre_node->rchild = root;
        pre_node->right_tag = 1;
    }
    pre_node = root;
    if(root->right_tag == 0) __build_inorder_thread(root->rchild);
    return;
}

void build_inorder_thread(node* root){
    pre_node = nullptr;
    inorder_root = nullptr;
    flag = false;
    __build_inorder_thread(root);
    pre_node->rchild = nullptr;
    pre_node->right_tag = 1;
    return;
}

node* get_next(node* root){
    if(root == nullptr) return nullptr;
    if(root->right_tag == 1){
        return root->rchild;
    }
    root = root->rchild;
    while(root->left_tag == 0 and root->lchild){
        root = root->lchild;
    }
    return root;
}

void test01(){
    srand(time(0));
    node* root = nullptr;
    for(int i =0;i<10;i++){
        root = insert(root,rand()%100);
    }
    //建立中序线索化
    build_inorder_thread(root);

    pre_order(root);//前序遍历
    printf("前序遍历\n");
    in_order(root);//中序遍历
    printf("中序遍历\n");
    post_order(root);//后序遍历
    printf("后序遍历\n");

    //经过线索化后二叉树就变得像链表一样，进行中序遍历可以不用递归
    node* p = inorder_root;
    while(p!=nullptr) {
        printf("%d ",p->data);
        p = get_next(p);
    }

    printf("线索化中序遍历\n");
    clear(root);
    return;
}

int main(void){
    test01();
    system("pause");
    return 0;
}