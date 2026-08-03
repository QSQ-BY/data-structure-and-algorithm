//广义表表示法进行序列化
/* 空树：（）
单一节点：A or A（）
表示父子关系：A（B，） or A（B) ->根节点是A，仅有一个左子树B
父节点（左子树节点，右子树节点）
A（B，C）  -> A的左子树是B右子树是C */

//问题1：二叉树->广义表
//问题2：广义表->二叉树
/* #include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#define KEY(n) (n?n->data:-1)

//二叉树转广义表的过程
typedef struct node{
    int data;
    struct node* lchild;
    struct node* rchild;
}node;

node* get_new_node(int data){
    node* p = (node*)malloc(sizeof(node));
    p->data = data;
    p->lchild = nullptr;
    p->rchild = nullptr;
    return p;
}

//将某个节点随机插入二叉树中的某个位置
node* insert(node* root,int data){
    if(root == nullptr) return get_new_node(data);
    if(rand()%2){
        root->lchild = insert(root->lchild,data);
    }else{
        root->rchild = insert(root->rchild,data);
    }
    return root;
}

//随机生成一个拥有n个节点的二叉树
node* get_random_binary_tree(int n){
    node* root = nullptr;
    for(int i =0;i<n;i++){
        root = insert(root,rand()%100);
    }
    return root;
}

void clear(node* root){
    if(root == nullptr) return;
    clear(root->lchild);
    clear(root->rchild);
    free(root);
    return;
}
char buff[10000];
int len = 0;


//二叉树转广义表
void __serialize(node* root){
    //类似于前序遍历
    if(root == nullptr) return;
    //先输出根节点的信息
    len += sprintf(buff + len,"%d", root->data);
    if(root->lchild == nullptr and root->rchild == nullptr) return;
    len += sprintf(buff + len,"(");

    __serialize(root->lchild);
    if(root->rchild) len+=sprintf(buff+len,",");
    __serialize(root->rchild);
    len += sprintf(buff+len,")");
    return;
}

void serialize(node* root){
    memset(buff,0,sizeof(buff));
    len = 0;
    __serialize(root);
    return;
}

void print(node* root){
    printf("%d(%d,%d)\n",KEY(root),KEY(root->lchild),KEY(root->rchild));
    return;
}

void output(node* root ){
    if(root == nullptr) return;
    print(root);
    output(root->lchild);
    output(root->rchild);
    return;
}

//广义表转二叉树
/* 思路分析:
要想恢复整个树，要先恢复左子树，再恢复右子树
具有完全包含关系
遇到左括号先把根节点压入到栈中，把根节点悬挂起来
处理到逗号的时候，接下来就要处理右子树的部分
接下来遇到右括号，栈顶元素出栈 */
/* 1.遇到关键字->生成新的节点
2.如果遇到左括号->把刚刚新生成的节点压入到栈中,标记设置成左子树
3.遇到逗号->打上一个标记(标记当前处理的是左子树还是右子树),标记当前位置应该处理的是右子树
4.遇到右括号->将栈顶元素出栈
5.每次生成一个新的节点->根据标记设置栈顶元素的左右子树 */
/* node* deserialize(char* buff, int n){
    node** stack = (node**)malloc(sizeof(node*)*(n > 0 ? n : 1));
    int top = -1;
    int flag = 0;
    node* root = nullptr;//用于记录我们最后一个被弹栈的节点（即根节点）是谁
    node* p = nullptr;//永远指向最后一个生成的节点
    int scode = 0;//状态码
    for(int i = 0;i<n;i++){
        switch(scode) {
            case 0:{
                //状态码0用于做状态分发
                if(buff[i]>='0' and buff[i]<='9') scode=1;//根据关键字生成新的节点
                else if(buff[i] == '(') scode = 2;//压栈
                else if(buff[i] == ')') scode = 3;//弹栈
                else if(buff[i] == ',') scode = 4;//更改左右括号标记（flag）
                i--;//抵消循环的推进

            }break;
            case 1:{
                int cur_number = 0;
                while(buff[i]<='9' and buff[i]>='0'){
                    cur_number = cur_number*10 + buff[i] - '0';
                    i++;//推进到下一位
                }
                i--;//再把i回退一步，抵消外层循环的i++
                p = get_new_node(cur_number);
                if(root == nullptr) root = p;
                if(top>=0 and flag == 0) stack[top]->lchild = p;
                if(top>=0 and flag == 1) stack[top]->rchild = p;
                scode = 0;//每次处理完任务之后都要重新分发任务
            }break;
            case 2:{
                top++;
                stack[top] = p;
                flag = 0;
                scode = 0;
            }break;
            case 3:{
                root = stack[top];
                top--;
                scode = 0;
            }break;
            case 4:{
                flag = 1;
                scode = 0;
            }break;
        }
    }
    free(stack);
    return root;
}


//测试代码
void test01(){
    node* root = get_random_binary_tree(10);
    output(root);//输出树的相关信息
    serialize(root);
    printf("%s\n",buff);

    node* new_root = deserialize(buff,len);
    output(new_root);
    clear(root);
    clear(new_root);
}

int main(void){
    srand(time(0));
    test01();
    system("pause");
    return 0;
} */


#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
typedef struct node{
    int data;
    struct node* lchild;
    struct node* rchild;
}node;

node* get_new_node(int data){
    node* p = (node*)malloc(sizeof(node));
    p->lchild = nullptr;
    p->rchild = nullptr;
    p->data = data;
    return p;
}

node* insert(node* root,int data){
    if(root == nullptr) return get_new_node(data);
    if(rand()%2){
        root->lchild = insert(root->lchild,data);
    }else{
        root->rchild = insert(root->rchild,data);
    }
    return root;
}


node* get_random_binary_tree(int n){
    node* root = nullptr;
    for(int i=0;i<n;i++){
        root = insert(root,rand()%100);
    }
    return root;
}


void clear(node* root){
    if(root == nullptr) return;
    clear(root->lchild);
    clear(root->rchild);
    free(root);
    return;
}

//二叉树转广义表
char buff[10000] = {0};
int len = 0;
void __serialize(node* root){
    if(root == nullptr) return;
    len += sprintf(buff+len,"%d",root->data);
    if(root->lchild == nullptr and root->rchild == nullptr) return;
    len+=sprintf(buff+len,"(");
    if(root->lchild) __serialize(root->lchild);
    len+=sprintf(buff+len,",");
    if(root->rchild) __serialize(root->rchild);
    len+=sprintf(buff+len,")");
}

void serialize(node* root){
    memset(buff,0,sizeof(buff));
    len = 0;
    __serialize(root);
    return;
}

void print(node* root){
    if(root == nullptr) return;
    int left_data = -1;
    int right_data = -1;
    printf("%d\n",root->data);
    if(root->lchild) left_data = root->lchild->data;
    if(root->rchild) right_data = root->rchild->data;
    printf("(%d,%d)\n",left_data,right_data);
    print(root->lchild);
    print(root->rchild);
    return;
}

//广义表转二叉树

/*
1.扫描整个字符串
2.碰到关键字就创造一个新的节点 scode = 1
3.每次生成一个新的节点就根据标记设置成栈顶元素的左右子树 scode = 1
4.碰到左括号就把刚刚创造的节点压入到栈中，同时将标记设置为左子树 scode=2
5.碰到右括号，把栈顶元素弹出栈中 scode=3
6.碰到逗号，将标记设置为右子树  scode=4
*/
node* deserialize(char* buff){
    int flag = 0;//0代表左子树，1代表右子树
    int scode = 0;//有限状态机分配任务
    node** stack = (node**)malloc(sizeof(node*)*strlen(buff));//树的节点构成的栈
    int top=-1;//栈顶指针
    int number = 0;//新节点数字
    node* p=nullptr;//永远指向新节点的指针
    node* root = nullptr;//指向第一个入栈的元素，即根节点,也是最后一个被弹栈的元素
    for(int i = 0;buff[i];i++){
        switch(scode){
            case 0:{
                if(buff[i]>='0' and buff[i]<='9') scode = 1;
                else if(buff[i] == '(') scode = 2;
                else if(buff[i] == ')') scode = 3;
                else if(buff[i] == ',') scode = 4;
                i--;
            }break;
            case 1:{
                number = 0;
                while(buff[i]>='0' and buff[i]<='9'){
                    number=number*10+buff[i] - '0';
                    i++;
                }
                p = get_new_node(number);
                if(root == nullptr) root = p;
                if(flag == 0){
                    if(top!=-1) stack[top]->lchild = p;
                }else{
                    if(top!=-1) stack[top]->rchild = p;
                }
                i--;
                scode = 0;
            }break;
            case 2:{
                top++;
                stack[top] = p;
                flag = 0;
                scode = 0;
            }break;
            case 3:{
                top--;
                scode = 0;
            }break;
            case 4:{
                flag = 1;
                scode = 0;
            }break;
            default:{}break;
        }
    }
    free(stack);
    return root;
}

void test01(){
    node* root = get_random_binary_tree(10);
    serialize(root);
    print(root);
    printf("%s\n",buff);
    node* new_root = nullptr;
    new_root = deserialize(buff);
    print(new_root);
    clear(root);
    clear(new_root);
    return;
}
int main(void){
    srand(time(0));
    test01();
    system("pause");
    return 0;
}
