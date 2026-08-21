//B树
/* 一颗m阶B树需要满足一下性质：
1.树中的每一个节点最多含有m棵子树
2.若根节点不是叶子节点，则至少含有两棵子树
3.除了根节点以外的所有非终端节点至少有m/2（向上取整）棵子树
4.如果一个节点有n-1个关键字，则该节点有n个分支，
    且这n-1个关键字按照递增序列排序
5.每个节点结构为：（n,A0,K1,A1,K2,A2.....Kn,An）
6.飞根节点中关键字的个数为n，满足m/2（向上取整）-1<=n<=m-1
7.所有叶子节点处在同一层 */
/* B树的性质解读：
1.B树中只有根节点没办法满足至少拥有m/2（向上取整）棵子树的条件的其他均满足
2.B树是一种高度平衡的树形结构（所有叶子节点都处在同一层） */
/* 
B树插入调整是为了解决上溢节点，关键字数量为m，核心操作：节点分裂
B树删除调整是为了解决下溢节点，关键字数量为m/2（向上取整）-2，核心操作：左旋、右旋、合并 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <stdbool.h>

#define MAX_M 5
#define MAX_OP 50
#define lchild(root,pos) (root->next[pos])
#define rchild(root,pos) (root->next[pos+1])
typedef struct Node{
    int n;//当前节点所存储的关键字的数量
    int key[MAX_M+1];//节点中所存储的关键字
    struct Node* next[MAX_M+1];//每个节点最多有m+1条边 
}Node;

Node* get_new_node(){
    Node* p = (Node*)malloc(sizeof(Node));
    p->n = 0;
    memset(p->next,0,sizeof(Node*)*(MAX_M+1));
    return p;
}

Node* insert_maintain(Node* root,Node* child,int pos){
    if(child->n < MAX_M) return root;
    int spos = MAX_M/2;
    Node* node1 = get_new_node();
    Node* node2 = get_new_node();
    node1->n = spos;
    node2->n = MAX_M-1-node1->n;
    for(int i=0;i<spos;i++){
        node1->key[i] = child->key[i];
        node1->next[i] = child->next[i];
    }
    node1->next[spos] = child->next[spos];
    for(int i=0;i<node2->n;i++){
        node2->key[i] = child->key[i+spos+1];
        node2->next[i] = child->next[i+spos+1];
    }
    node2->next[node2->n] = child->next[child->n];
    for(int i = root->n;i>=pos;i--){
        root->key[i+1] = root->key[i];
        root->next[i+1] = root->next[i];
    }
    root->key[pos] = child->key[spos];
    root->next[pos] = node1;
    root->next[pos+1] = node2;
    root->n++;
    free(child);
    return root;
}

Node* insert_key(Node* root,int key){
    if(root==nullptr){
        root = get_new_node();
        root->key[0] = key;
        root->n = 1;
        return root;
    }
    int pos = 0;
    while(pos<root->n and root->key[pos]<key) pos++;
    if(pos<root->n and root->key[pos] == key) return root;
    else{
        for(int i = root->n-1;i>=pos;i--){
            root->key[i+1] = root->key[i];
        }
        root->key[pos] =key;
        root->n++;
        return root;
    }
}

Node* __insert(Node* root,int key){
    if(root==nullptr or root->next[0] == nullptr){
        return insert_key(root,key);
    }
    int pos = 0;
    while(pos<root->n and root->key[pos] < key) pos++;
    if(pos<root->n and root->key[pos]==key) return root;
    __insert(root->next[pos],key);
    return insert_maintain(root,root->next[pos],pos);
}

Node* insert(Node* root,int key){
    root = __insert(root,key);
    if(root->n >= MAX_M){
        Node* p = get_new_node();
        p->next[0] = root;
        root = insert_maintain(p,root,0);//根节点，发生失衡的子树，发生失衡的子树的编号
    }
    return root;
}

void clear(Node* root){
    if(root==nullptr) return;
    for(int i=0;i<root->n+1;i++) clear(root->next[i]);
    free(root);
    return;
}

void print_node(Node* root){
    printf("%d:",root->n);
    for(int i=0;i<root->n;i++){
        printf("%4d",root->key[i]);
    }
    printf(" | ");
    if(root->next[0]==nullptr){
        printf("\n");
        return;
    }else{
        for(int i=0;i<root->n+1;i++){
            printf("%4d",root->next[i]->key[0]);
        }
        printf("\n");
        return;
    }
}

void output(Node* root){
    if(root == nullptr) return;
    print_node(root);
    for(int i=0;i<root->n+1;i++) output(root->next[i]);
    return;
}

//在终端节点处删除pos位置的值
Node* erase_pos(Node* root,int pos){
    for(int i=pos+1;i<=root->n-1;i++){
        root->key[i-1] = root->key[i];
    }
    root->n--;
    return root;
}

//右旋，把pos位置的值借给pos+1位置
Node* right_rotate(Node* root,int pos){
    for(int i = rchild(root,pos)->n;i >=0;i--){
        //把该位置右孩子的值全部向后移动一位
        rchild(root,pos)->key[i+1] = rchild(root,pos)->key[i];
        rchild(root,pos)->next[i+1] = rchild(root,pos)->next[i];
    }
    rchild(root,pos)->key[0] = root->key[pos];
    root->key[pos] = lchild(root,pos)->key[lchild(root,pos)->n-1];
    rchild(root,pos)->next[0] = lchild(root,pos)->next[lchild(root,pos)->n];
    lchild(root,pos)->next[lchild(root,pos)->n]=nullptr;
    rchild(root,pos)->n++;
    lchild(root,pos)->n--;
    return root;
}

//左旋，把pos+1位置的值借给pos
Node* left_rotate(Node* root,int pos){
    lchild(root,pos)->key[lchild(root,pos)->n] = root->key[pos];
    lchild(root,pos)->n++;
    root->key[pos] = rchild(root,pos)->key[0];
    lchild(root,pos)->next[lchild(root,pos)->n] = rchild(root,pos)->next[0];
    for(int i=0;i<=rchild(root,pos)->n-1;i++){
        rchild(root,pos)->key[i] = rchild(root,pos)->key[i+1];
        rchild(root,pos)->next[i]= rchild(root,pos)->next[i+1];
    }
    rchild(root,pos)->next[rchild(root,pos)->n] = nullptr;
    rchild(root,pos)->n--;
    return root;
}

//合并操作(合并pos和pos+1的节点)
Node* merge_node(Node* root,int pos){
    Node* new_node = get_new_node();
    //把左节点的所有信息拷贝到新节点中
    for(int i = 0;i<=lchild(root,pos)->n;i++){
        new_node->key[i] = lchild(root,pos)->key[i];
        new_node->next[i]= lchild(root,pos)->next[i];
    }
    new_node->n = lchild(root,pos)->n;
    //在新节点尾部插入根节点pos位置的值
    new_node->key[new_node->n] = root->key[pos];
    new_node->n++;
    //把右节点的所有信息接到新节点中
    for(int i =0;i<rchild(root,pos)->n+1;i++){
        new_node->key[i+new_node->n] = rchild(root,pos)->key[i];
        new_node->next[i+new_node->n] = rchild(root,pos)->next[i];
    }
    new_node->n+= rchild(root,pos)->n;
    //清理旧的左右节点
    free(lchild(root,pos));
    free(rchild(root,pos));
    //把根节点pos后面的值向前移
    for(int i= pos+1;i<=root->n;i++){
        root->key[i-1] = root->key[i];
        root->next[i-1]= root->next[i];
    }
    root->next[pos] = new_node;
    root->n--;
    return root;
}

Node* erase_maintain(Node* root,int pos){
    //下限
    int low_bound = (MAX_M+1)/2-1;//向上取整
    if(root->next[pos]->n >= low_bound) return root;//未发生失衡
    
    //发生失衡
    if(pos>0 and root->next[pos-1]->n > low_bound){
        //向前兄弟节点借，右旋
        root = right_rotate(root,pos-1);
    }else if(pos<root->n and root->next[pos+1]->n > low_bound){
        //向后兄弟节点借，左旋
        root = left_rotate(root,pos);
    }else{
        //合并操作
        if(pos>0) root = merge_node(root,pos-1);//merge(root,j)->把j和j+1节点进行合并
        else root = merge_node(root,pos);
    }
    return root;
}

Node* __erase(Node* root , int key){
    if(root == nullptr) return nullptr;

    //终端节点的情况
    int pos = 0;
    if(root->next[0] == nullptr){
        //当前节点没有子树
        while(pos<root->n and root->key[pos] < key) pos++;
        if(pos>=root->n) return root;
        if(pos<root->n and root->key[pos] > key) return root;
        else if(root->key[pos] == key){
            root = erase_pos(root,pos);
            return root;
        }
    }

    //非终端节点
    while(pos<root->n and root->key[pos]<key) pos++;
    //如果我们删除的值在当前节点处
    if(pos<root->n and root->key[pos] == key){
        Node* temp = root->next[pos];
        while(temp->next[temp->n]!=nullptr) temp = temp->next[temp->n];
        int val = temp->key[temp->n-1];
        root->key[pos] = val;
        root->next[pos] = __erase(root->next[pos],val); 
    }else{
        //不在当前节点则顺着往下走
        root->next[pos] = __erase(root->next[pos],key);
    }
    return erase_maintain(root,pos);
}

Node* erase(Node* root,int key){
    if(root == nullptr) return nullptr;
    root = __erase(root,key);
    if(root->n==0){
        Node* temp = root->next[0];
        free(root);
        root = temp;
    }
    return root;
}

void test01(){
    Node* root = nullptr;
    for(int i=0;i<MAX_OP;i++){
        int val = rand()%100;
        root = insert(root,val);
        printf("\n将%d插入B树\n",val);
        output(root);
    }

    int x;
    while(~scanf("%d",&x)){
        printf("从B树中删除%d\n",x);
        root = erase(root,x);
        output(root);
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