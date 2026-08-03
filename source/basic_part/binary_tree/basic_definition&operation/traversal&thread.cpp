#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

typedef struct node {
    int data;
    int left_tag;
    int right_tag;
    struct node* left_child;
    struct node* right_child;
}node;

node* get_new_node(int data){
    node* p = (node*)malloc(sizeof(node));
    p->data = data;
    p->left_child = nullptr;
    p->right_child = nullptr;
    p->left_tag = 0;
    p->right_tag = 0;

    return p;
}

node* insert(node* root,int data){
    if(root == nullptr) return get_new_node(data);
    if(rand()%2){
        if(root->left_tag == 0) root->left_child = insert(root->left_child,data);
    }else{
        if(root->right_tag == 0) root->right_child = insert(root->right_child,data);
    }
    return root;
}

void clear(node* root){
    if(root ==nullptr) return;
    if(root->left_tag == 0) clear(root->left_child);
    if(root->right_tag == 0) clear(root->right_child);
    free(root);
    return;
}

//前序遍历
void pre_order(node* root){
    if(root == nullptr) return;
    printf("%d ",root->data);
    if(root->left_tag == 0) pre_order(root->left_child);
    if(root->right_tag == 0) pre_order(root->right_child);
    return;
}

//中序遍历
void in_order(node* root){
    if(root == nullptr) return;
    if(root->left_tag == 0) in_order(root->left_child);
    printf("%d ",root->data);
    if(root->right_tag == 0) in_order(root->right_child);
    return;
}

//后序遍历
void post_order(node* root){
    if(root == nullptr) return;
    if(root->left_tag == 0) post_order(root->left_child);
    if(root->right_tag == 0) post_order(root->right_child);
    printf("%d ",root->data);
    return;
}

//中序遍历线索化
//左指针指向当前节点的前驱，右指针指向当前节点的后继
node* pre_node{nullptr};
int flag{0};
node* start{nullptr};
void __inorder_thread(node* root){
    if(root == nullptr) return;
    if(root->left_tag == 0) __inorder_thread(root->left_child);
    if(flag == 0){
        start = root;
        flag = 1;
    }
    if(root->left_child == nullptr){
        root->left_tag = 1;
        root->left_child = pre_node;
    }
    if(pre_node and pre_node->right_child == nullptr){
        pre_node->right_tag = 1;
        pre_node->right_child = root;
    }
    pre_node = root;
    if(root->right_tag == 0) __inorder_thread(root->right_child);
    return;
}

//进行了上述的中序遍历之后，整个子树最右侧的那个节点，也就是中序遍历结果中
//根节点前面的那个节点，也就是根节点的前驱，他是没有右子树的，线索化会让他
//指向中序遍历中自己的后继，也就是树的最右侧节点会指向整个树的根节点
//需要进行二次封装把他的右指针指向空
node* inorder_thread(node* root){
    pre_node = nullptr;
    flag = 0;
    start = nullptr;
    __inorder_thread(root);
    pre_node->right_child = nullptr;//把根节点的前驱指向空
    return root;
}

node* get_next(node* root){
    if(root == nullptr) return nullptr;
    if(root->right_tag == 1) return root->right_child;
    //右指针是真是的树就找到右子树中靠左的节点
    root = root->right_child;
    while(root and root->left_tag == 0){
        root = root->left_child;
    }
    return root;
}

void test01(){
    srand(time(0));
    node* root = nullptr;
    for(int i = 0;i<10;i++){
        root = insert(root , rand()%100);
    }
    pre_order(root);
    printf("\n");
    in_order(root);
    printf("\n");
    post_order(root);
    printf("\n");
    inorder_thread(root);
    node* p = start;
    /* while(p and p->left_tag == 0){
        p = p->left_child;
    } */
    //直接使用循环结构找到整个中序遍历的起始节点，即最左边的节点
    while(p){
        printf("%d ",p->data);
        p=get_next(p);
    }
    printf("\n");
    clear(root);
}
int main(void){
    test01();
    system("pause");
    return 0;
}