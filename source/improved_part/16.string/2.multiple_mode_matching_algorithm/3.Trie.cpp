//标准字典树,单词查找树
#include <iostream>
#include <vector>
using namespace std;
#define int long long
#define BASE 26
typedef struct Node{
    struct Node* next[BASE];
    int flag;
}Node;

Node* get_new_node(){
    Node* p = (Node*)malloc(sizeof(Node));
    for(int i=0;i<BASE;i++) p->next[i] = nullptr;
    p->flag = 0;
    return p;
}

void insert(Node* root,const char* s){
    Node* p = root;
    for(int i=0;s[i];i++){
        char ch = s[i];
        int index = ch - 'a';
        if(p->next[index] == nullptr){
            p->next[index] = get_new_node();
        }
        p = p->next[index];
    }
    p->flag = 1;//代表当前节点独立成词
    return;
}

//返回值代表是否找到了这个单词
int find(Node* root,const char* s){
    Node* p = root;
    for(int i=0;s[i];i++){
        int index = s[i] - 'a';
        p = p->next[index];
        if(p == nullptr){
            return 0;//没有这个单词，表示没有找到
        }
    }
    if(p->flag == 0){
        return 0;
    }else{
        return 1;//只有最后找到的节点独立成词才代表最后找到了这个单词
    }
}

//进行字符串排序打印
//首先传入根节点然后是层数，最后传入一个缓冲数组来保存
void dfs_output(Node* root,int k,char* buffer){
    if(root == nullptr) return;
    if(root->flag){
        buffer[k] = '\0';
        printf("%s\n",buffer);
    }
    for(int i=0;i<BASE;i++){
        if(root->next[i] == nullptr) continue;
        buffer[k] = 'a' + i;
        dfs_output(root->next[i],k+1,buffer);
    }
}

void clear(Node* root){
    if(root == nullptr){
        return;
    }
    for(int i=0;i<BASE;i++){
        clear(root->next[i]);
    }
    free(root);
    return;
}

signed main(void){
    //树形结构的节点代表的是集合，边代表的是关系
    int op;
    char s[100];
    Node* root = get_new_node();
    do{
        cin>>op;
        if(op == 3){
            break;
        }
        cin>>s;
        switch(op){
            case 1:{
                printf("insert %s to trie\n",s);
                insert(root,s);
            }break;
            case 2:{
                printf("find %s from trie:%lld\n",s,find(root,s));
            }break;
        }
    }while(1);
    char buffer[100];
    dfs_output(root,0,buffer);//传入根节点和层数
    clear(root);
    system("pause");
    return 0;
}
