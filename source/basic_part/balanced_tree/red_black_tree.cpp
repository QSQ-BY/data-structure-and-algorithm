
//红黑树
/* 平衡条件：
1.每个节点非黑即红
2.根节点一定是黑色
3.NIL节点一定是黑色
4.红色节点的子节点一定都是黑色
5.到达每个NIL叶子节点的路径上的黑色节点数量一定都相同 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <stdbool.h>

#define RED (0)
#define BLACK (1)
#define DBLACK (2)
#define NIL (&__NIL)
#define K(n) (n->key)
#define L(n) (n->lchild)
#define R(n) (n->rchild)
#define C(n) (n->color)

typedef struct Node{
    int key;
    struct Node* lchild;
    struct Node* rchild;
    int color;//用0表示红色，用1表示黑色，用2表示双重黑
}Node;

Node __NIL;
__attribute__((constructor))
void init_NIL(){
    NIL->key = -1;
    NIL->color = BLACK;
    NIL->lchild = NIL;
    NIL->rchild = NIL;
    return;
}

Node* get_new_node(int key){
    Node* p = (Node*)malloc(sizeof(Node));
    p->key = key;
    p->color = RED;
    p->lchild = p->rchild = NIL;
    return p;
}

bool has_red_node(Node* root){
    return root->lchild == RED or root->rchild->color == RED;
}

Node* right_rotate(Node* root){
    if(root==NIL) return root;
    if(root->lchild == NIL and root->rchild == NIL) return root;
    Node* new_root = root->lchild;
    root->lchild = new_root->rchild;
    new_root->rchild = root;
    return new_root;
}

Node* left_rotate(Node* root){
    if(root==NIL) return root;
    if(root->lchild == NIL and root->rchild == NIL) return root;
    Node* new_root = root->rchild;
    root->rchild = new_root->lchild;
    new_root->lchild = root;
    return new_root;
}

Node* insert_maintain(Node* root){
    //判断是否发生了失衡,即出现了双红交叉的情况
    if(root==NIL) return root;
    if(!has_red_node(root)) return root;
    int flag = 0;
    if(root->lchild->color == RED and has_red_node(root->lchild)) flag = 1;
    if(root->rchild->color == RED and has_red_node(root->rchild)) flag = 2;
    if(flag == 0) return root;

    //两边都是红色
    if(root->lchild->color==RED and root->rchild->color==RED){
        root->color = RED;
        C(L(root)) = C(R(root)) = BLACK;
        return root;
    }

    //只有一边是红色
    if(flag==1){
        //左子树为红色(L)
        if(C(R(root->lchild)) == RED){
            //LR
            root->lchild = left_rotate(root->lchild);
        }
        //LL类型
        root = right_rotate(root);
    }else{
        if(C(L(root->rchild)) == RED){
            //RL
            root->rchild = right_rotate(root->rchild);
        }
        //RR类型
        root = left_rotate(root);
    }
    //红色上浮调整策略
    root->color = RED;
    root->lchild->color = root->rchild->color = BLACK;
    //红色下沉调整策略
    //root->color =BLACK;
    //root->lchild->color = root->rchild->color = RED;
    return root;
}

Node* __insert(Node* root,int key){
    if(root==NIL) return get_new_node(key);
    if(root->key == key) return root;
    if(key < root->key) root->lchild = __insert(root->lchild,key);
    else if(key>root->key) root->rchild = __insert(root->rchild,key);
    root = insert_maintain(root);
    return root;
}

Node* insert(Node* root,int key){
    root = __insert(root,key);
    root->color = BLACK;
    return root;
}

//删除调整策略
/*     红          黑
0   直接删除    把当前NIL节点标记为双重黑然后进行删除调整（干掉双重黑）

1   不存在      红提升并变黑（度为1的黑色节点只能链接一个红色节点）

2->可转化为删除度为1或者度为0的问题    
*/

Node* pre(Node* root){
    Node* p = root->lchild;
    if(p->rchild != NIL) p = p->rchild;
    return p;
}

Node* erase_maintain(Node* root,int key){
    if(C(L(root)) != DBLACK and C(R(root))!=DBLACK) return root;
    if(has_red_node(root)){
        //兄弟节点是红色
        root->color = RED;//原根节点变为红色
        if(root->lchild->color == RED) {
            root = right_rotate(root);
            root->rchild = erase_maintain(root->rchild,key);
        }
        else if(root->rchild->color == RED) {
            root = left_rotate(root);
            root->lchild = erase_maintain(root->lchild,key);
        }
        root->color = BLACK;//新根节点变为黑色
        return root;
    }else{
        //兄弟节点是黑色
        if((root->lchild->color == DBLACK and !has_red_node(root->rchild)) or
            root->rchild->color == DBLACK and !has_red_node(root->lchild)){
            //兄弟节点没有任何红色子节点
            root->color++;
            root->lchild--;
            root->rchild--;
            return root;
        }
        if(root->rchild->color == DBLACK){
            if(root->lchild->rchild->color ==RED){
                //LR失衡
                root->lchild = left_rotate(root->lchild);
            }
            root->lchild->color = root->color;//新根节点的颜色变为原根节点的颜色
            //LL失衡
            root = right_rotate(root);
            root->lchild->color = BLACK;
            root->rchild->color = BLACK;//新根节点的子树的颜色强制改黑
        }else if(root->lchild->color == DBLACK){
            if(root->rchild->lchild->color == RED){
                //RL失衡
                root->rchild = right_rotate(root->rchild);
            }
            root->rchild->color = root->color;
            //RR失衡
            root = left_rotate(root);
            root->lchild->color = BLACK;
            root->rchild->color = BLACK;
        }
    }
    return root;
}

Node* __erase(Node* root,int key){
    if(root == NIL) return root;
    if(key<root->key) root->lchild = __erase(root->lchild,key);
    else if(key>root->key) root->rchild = __erase(root->rchild,key);
    else if(key == root->key){
        //度为1或0
        if(root->lchild ==NIL or root->rchild ==NIL){
            Node* temp = NIL;
            if(root->lchild != NIL) temp = root->lchild;
            else if(root->rchild != NIL) temp = root->rchild;
            temp->color += root->color;
            free(root);
            return temp;
        }else if(root->lchild!=NIL and root->rchild!=NIL){
            Node* temp = pre(root);
            root->key = temp->key;
            root->lchild = __erase(root->lchild,temp->key);
        }
    }
    return erase_maintain(root,key);
}

Node* erase(Node* root,int key){
    if(root == NIL) return root;
    root = __erase(root,key);
    root->color = BLACK;
    return root;
}

void output(Node* root){
    if(root==NIL) return;
    printf("(%d| %d; %d,%d)\n",C(root),K(root),K(L(root)),K(R(root)));
    output(root->lchild);
    output(root->rchild);
    return;
}

void clear(Node* root){
    if(root==NIL) return;
    if(root->lchild == NIL and root->rchild ==NIL){
        free(root);
        return;
    }
    clear(root->lchild);
    clear(root->rchild);
    free(root);
}

void test01(){
    #define MAX_N (10)
    Node* root = NIL;
    //插入测试
    for(int i=0;i<MAX_N;i++){
        int x = rand()%100;
        printf("向红黑树中插入%d\n",x);
        root = insert(root,x);
        output(root);
        printf("\n");
    }
    
    //删除测试
    int x=0;
    while(~scanf("%d",&x)){
        printf("\n从红黑树中删除%d\n",x);
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