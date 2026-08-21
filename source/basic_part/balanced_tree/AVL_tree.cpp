//AVL树-平衡二叉排序树
//|H(left) - H(right)| <= 1
//左右子树的树高不能超过1
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <stdbool.h>

typedef struct Node{
    int key;
    int height;//树高变量
    struct Node* lchild;
    struct Node* rchild;
}Node;

//虚拟空节点
Node __NIL;
#define NIL (&__NIL)
#define H(n) (n->height)
#define L(n) (n->lchild)
#define R(n) (n->rchild)
#define K(n) (n->key)
__attribute__((constructor))//用来设置函数的属性
void init_NIL(){
    NIL->key = -1;
    NIL->height = 0;
    NIL->lchild = NIL->rchild = NIL;
    return;
}

int abs(int a){
    if(a<0) a = -a;
    else if(a>=0) return a;
    return a;
}

Node* get_new_node(int key){
    Node* p = (Node*)malloc(sizeof(Node));
    p->key = key;
    p->height = 1;
    p->lchild = p->rchild = NIL;//NIL为虚拟空节点
    return p;
}

void update_height(Node* root){
    if(root == NIL) return;
    if(H(root->lchild) > H(root->rchild)) H(root) = H(root->lchild)+1;
    else H(root) = H(root->rchild) +1;
    return;
}

//左旋
Node* left_rotate(Node* root){
    printf("left_rotate:%d\n",root->key);
    Node* new_root = root->rchild;
    root->rchild = new_root->lchild;
    new_root->lchild = root;
    update_height(root);
    update_height(new_root);
    return new_root;
}

//右旋
Node* right_rotate(Node* root){
    printf("left_rotate:%d\n",root->key);
    Node* new_root = root->lchild;
    root->lchild = new_root->rchild;
    new_root->rchild = root;
    update_height(root);
    update_height(new_root);
    return new_root;
}

const char* type_str[5]= {
    "",
    "maintain type : LL",
    "maintain type : LR",
    "maintain type : RR",
    "maintain type : RL",
};

Node* maintain(Node* root){
    if(abs(H(R(root)) - H(L(root))) <= 1) return root;
    int type = 0;
    if(H(L(root))>H(R(root))){
        if(H(root->lchild->rchild) > H(root->lchild->lchild)){
            //LR失衡类型
            root->lchild = left_rotate(root->lchild);
            type++;//type = 1
        }
        //LL类型失衡
        root = right_rotate(root);
        type++;//type = 2
    }else if(H(root->rchild) > H(root->lchild)){
        type = 2;
        if(H(root->rchild->lchild) > H(root->rchild->rchild)){
            //RL失衡类型
            root->rchild = right_rotate(root->rchild);
            type++;//type = 3
        }
        //RR类型失衡
        root = left_rotate(root);
        type++;//type = 4
    }
    printf("%s\n",type_str[type]);
    return root;
}

Node* insert(Node* root,int key){
    if(root==NIL) return get_new_node(key);
    if(root->key == key) return root;
    if(key<root->key) root->lchild = insert(root->lchild,key);
    else if(key>root->key) root->rchild = insert(root->rchild,key);
    update_height(root);
    return maintain(root);
}

Node* pre(Node* root){
    if(root==NIL) return root;
    Node* p = root->lchild;
    while(p->rchild!=NIL) p = p->rchild;
    return p;
}

Node* erase(Node* root,int key){
    if(root == NIL) return root;
    if(key<root->key) root->lchild = erase(root->lchild, key);
    else if(key>root->key) root->rchild = erase(root->rchild,key);
    else if(key == root->key){
        if(root->lchild == NIL or root->rchild == NIL){
            Node* temp = NIL;
            if(root->lchild!=NIL) temp = root->lchild;
            else if(root->rchild!=NIL) temp = root->rchild;
            free(root);
            return temp;
        }else if(root->lchild!=NIL and root->rchild!=NIL){
            Node* temp = pre(root);
            root->key = temp->key;
            root->lchild = erase(root->lchild,temp->key);
        }
    }
    update_height(root);
    return maintain(root);
}

Node* find(Node* root,int key){
    if(root==NIL) return root;
    if(root->key == key) return root;
    if(key<root->key) return find(root->lchild,key);
    else if(key>root->key) return find(root->rchild,key);
    return root;
}

void clear(Node* root){
    if(root == NIL) return;
    clear(root->lchild);
    clear(root->rchild);
    free(root);
    return;
}

void output(Node* root){
    if(root == NIL) return;
    printf("(%d[%d] | %d,%d)\n",root->key,root->height,K(L(root)),K(R(root)));
    output(root->lchild);
    output(root->rchild);
    return;
}

void test01(){
    Node* root = NIL;
    int x;
    //插入测试
    while(~scanf("%d",&x)){
        if(x==-1) break;
        printf("向AVL树中插入%d\n",x);
        root = insert(root,x);
        output(root);
        printf("\n");
    }

    //删除测试
    while(~scanf("%d",&x)){
        if(x==-1) break;
        printf("从AVL树中删除%d\n",x);
        root = erase(root,x);
        output(root);
        printf("\n");
    }

    //查找测试
    while(~scanf("%d",&x)){
        if(x==-1) break;
        printf("从AVL树中查找%d : %d\n",x,find(root,x)!=NIL);
        printf("\n");
    }
    clear(root);
    return;
}

int main(void){
    srand(time(0));
    test01();
    system("pause");
    return 0;
}