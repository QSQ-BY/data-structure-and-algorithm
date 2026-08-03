#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#define MAX_NODE 10
typedef struct node{
    int data;
    //struct node* next[2];
    struct node *lchild,*rchild;
}node;

node* get_new_node(int data){
    node* p = (node*)malloc(sizeof(node));
    p->data = data;
    p->lchild = nullptr;
    p->rchild = nullptr;
    return p;
}

node* insert(node* root,int data){
    if(root == nullptr) return get_new_node(data);
    if(rand()%2 == 1) root->lchild = insert(root->lchild,data);
    else root->rchild = insert(root->rchild,data);
    return root;
}

//广度优先搜索（层序遍历）
void bfs(node* root){
    if(root==nullptr) return;
    node* queue[MAX_NODE+5];
    int head,tail;
    head = tail=0;
    queue[tail] = root;
    tail++;
    while(head<tail){
        node* cur_node = queue[head];
        printf("\nnode:%d\n",cur_node->data);
        if(cur_node->lchild) {
            queue[tail++] = cur_node->lchild;
            printf("\t%d->%d\n(left)",cur_node->data,cur_node->lchild->data);
        }
        if(cur_node->rchild) {
            queue[tail++] = cur_node->rchild;
            printf("\t%d->%d\n(right)",cur_node->data,cur_node->rchild->data);
        }
        head++;
    }
    return ;
}

//深度优先遍历
int tot=0;
void dfs(node* root){
    if(root == nullptr) return;
    int start,end;
    tot++;
    start = tot;
    if(root->lchild) dfs(root->lchild);
    if(root->rchild) dfs(root->rchild);
    tot++;
    end = tot;
    printf("%d:[%d,%d]\n",root->data,start,end);
    return;
}

void clear(node* root){
    if(root == nullptr) return;
    //递归函数
    clear(root->lchild);
    clear(root->rchild);
    free(root);
    return ;
}

void test01(){
    srand(time(0));
    node* root = nullptr;
    for(int i=0;i<MAX_NODE;i++){
        root = insert(root,rand()%100);
    }
    bfs(root);
    printf("\n\n\n");
    dfs(root);
    clear(root);
}
int main(void){
    test01();
    system("pause");
    return 0;
}