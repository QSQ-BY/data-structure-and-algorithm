#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

typedef struct node{
    char ch;
    int freq;
    struct node *lchild,*rchild;
}node;

node* get_new_node(int freq,char ch){
    node* p = (node*)malloc(sizeof(node));
    p->ch = ch;
    p->freq = freq;
    p->lchild = p->rchild = nullptr;
    return p;
}
void swap_node(node** node_arr,int i,int j){
    node* temp = node_arr[i];
    node_arr[i] = node_arr[j];
    node_arr[j] = temp;
    return;
}

int find_min_node(node** node_arr,int len){
    int index = 0;
    for(int j=0;j<=len;j++){
        if(node_arr[index]->freq > node_arr[j]->freq) index = j;
    }
    return index;
}

//建立哈夫曼树
node* build_huffman_tree(node** node_arr,int n){
    for(int i=1;i<n;i++){
        int index1 = find_min_node(node_arr,n-i);
        swap_node(node_arr,index1,n-i);
        int index2 = find_min_node(node_arr,n-i-1);
        swap_node(node_arr,index2,n-1-i);
        int new_freq = node_arr[n-i]->freq + node_arr[n-i-1]->freq;
        node* new_node = get_new_node(new_freq,0);
        new_node->lchild = node_arr[n-i-1];
        new_node->rchild = node_arr[n-i];
        node_arr[n-1-i] = new_node;
    }
    return node_arr[0];
}

//提取编码信息
void extract_huffman_code(node* root,char* buff,int k){
    buff[k] = 0;
    if(root->lchild == nullptr and root->rchild == nullptr){
        printf("%c:%s\n",root->ch,buff);
        return;
    }
    if(root->lchild){
        buff[k] = '0';
        extract_huffman_code(root->lchild,buff,k+1);
    }
    if(root->rchild){
        buff[k] = '1';
        extract_huffman_code(root->rchild,buff,k+1);
    }
}



void clear(node* root){
    if(root==nullptr) return;
    clear(root->lchild);
    clear(root->rchild);
    free(root);
    return;
}

void test01(){
    int n;//多少个字符
    char s[10];
    int freq;
    scanf("%d",&n);
    node** node_arr = (node**)malloc(sizeof(node*)*n);
    for(int i=0;i<n;i++){
        scanf("%s%d",s,&freq);
        node_arr[i] = get_new_node(freq,s[0]);
    }
    for(int i=0;i<n;i++){
        printf("%c %d\n",node_arr[i]->ch,node_arr[i]->freq);
    }
    //建立哈夫曼树
    node* root = build_huffman_tree(node_arr,n);
    //提取相关的编码信息
    char buff[10000];
    extract_huffman_code(root,buff,0);
    clear(root);
    free(node_arr);
}
int main(void){
    srand(time(0));
    test01();
    system("pause");
    return 0;
}