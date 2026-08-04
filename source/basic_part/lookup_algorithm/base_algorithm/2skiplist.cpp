//跳跃表
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <stdbool.h>
#include <inttypes.h>


typedef struct node{
    int key;
    struct node* next;//横向指针
    struct node* down;//向下的指针
    struct node* up;//向上的指针
    int level;//层数
}node;

#define MAX_LEVEL 50

typedef struct skiplist{
    struct node* head;
    struct node* tail;
    int max_level;
}skiplist;

node* get_new_node(int key,int n){
    if(n<=0) return nullptr;
    node* nodes = (node*)malloc(sizeof(node)*n);//开辟节点数组
    for(int i = 0;i<n;i++){
        nodes[i].level = i;
        nodes[i].key = key;
        nodes[i].next = nullptr;
        if(i >= 1) nodes[i].down = &nodes[i-1];
        else nodes[i].down = nullptr;
        if(i <= n-2) nodes[i].up = &nodes[i+1];
        else nodes[i].up = nullptr;
    }
    return &nodes[n-1];
}

void clear_node(node* p){
    if(p == nullptr) return;
    free(p);
    return;
}

//在跳跃表中查找值为s的节点
node* find(skiplist* s,int x){
    if(s==nullptr) return nullptr;
    node* p = s->head;
    while(p!=nullptr and p->key!=x){
        if(p->next!=nullptr and p->next->key <= x) p = p->next;
        else p = p->down;
    }
    return p;
}

int rand_level(int max_level){
    int level = 1;
    while(level < max_level and rand() % 2) level+=1;
    return level;
}

//跳跃表的插入操作
void insert(skiplist* s,int x){
    if(s==nullptr) return;
    int level = rand_level(s->max_level);
    node* new_node = get_new_node(x,level);
    node* p = s->head;
    while(p->level != new_node->level) p=p->down;
    while(p){
        while(p->next != nullptr and p->next->key <= new_node->key) p = p->next;
        new_node->next = p->next;
        p->next = new_node;
        p = p->down;
        new_node = new_node->down;
    }
    return;
}

skiplist* get_new_skiplist(int n){
    if(n<=0) return nullptr;
    skiplist* p = (skiplist*)malloc(sizeof(skiplist));
    p->head = get_new_node(INT32_MIN,n);
    p->tail = get_new_node(INT32_MAX,n);
    p->max_level = n;
    node* p1 = p->head;
    node* p2 = p->tail;
    while(p1 and p2){
        p1->next = p2;
        p1 = p1->down;
        p2 = p2->down;
    }
    return p;
}



void clear_skiplist(skiplist* s){
    if(s==nullptr) return;
    node* p = s->head;
    while(p->level != 0) p = p->down;
    node* temp = nullptr;
    while(p != nullptr){
        temp = p->next;
        clear_node(p);
        p = temp;
    }
    free(s);
    return;
}

void output(skiplist* s){
    if(s == nullptr) return;
    node* p = s->head;
    node* tail = s->tail;
    while(p != nullptr and tail != nullptr){
        printf("Level %d: HEAD",p->level);
        for(node* q = p->next;q != nullptr and q != tail;q=q->next){
            printf(" -> %d",q->key);
        }
        printf(" -> TAIL\n");
        p = p->down;
        tail = tail->down;
    }
    return;
}


void test01(){
    int x=0;
    skiplist* s = get_new_skiplist(MAX_LEVEL);

    while(~scanf("%d",&x)){
        if(x<=-1) break;
        insert(s,x);
    }
    output(s);
    //测试查找算法
    while(~scanf("%d",&x)){
        node* p = find(s,x);
        if(p!=nullptr){
            printf("成功找到%d在%d层\n",x,p->level);
        }else {
            printf("没有找到%d\n",x);
        }
    }
    clear_skiplist(s);
}
int main(void){
    srand(time(0));
    test01();
    system("pause");
    return 0;
}