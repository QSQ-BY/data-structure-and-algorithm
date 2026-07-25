//哈希表与布隆过滤器
//哈希函数-> val%size
/* 哈希表冲突处理方法：
1.开放定址法
    如果通过哈希函数发生了冲突，按照一定规律根据当前地址计算下一个地址
2.再哈希法（不常用）
    使用多个哈希函数
    val%num1->val%num2->val%num3
3.建立公共溢出区
    如果发生了冲突则把冲突元素放入到一个另外的用于查找的数据结构中去
    溢出缓冲区可能没有哈希表查找效率高
4.拉链地址法/拉链法（重点、常用）
    每个位置维护成一个链表/红黑树，发生冲突也能存储到相同的位置 */
/* 传统哈希表，与元素数量强相关
布隆过滤器，与元素数量弱相关->搜索引擎的爬虫场景用于记录爬取的网页地址
布隆过滤器：
底层是一个只存储0和1的数组，存储1的位置代表被标记过，存储0则是没标记过
一个元素通过三个哈希函数得到三个位置观察三个位置是否都是1
只要出现0则代表该元素“一定”没有出现过，都是1则代表该元素“大概率”出现过
布隆过滤器判断的出现是一个概率性事件，判断的不出现则是确定性事件
降低误判得概率则需要增加布隆过滤器底层数组的长度 */


//使用拉链法（链表）
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <stdbool.h>
#include <limits.h>

#define MAX_N 4

//链表节点
typedef struct node{
    char* s;
    struct node* next;
}node;

//哈希表
typedef struct hash_table{
    struct node* data;//node数组
    int cnt;//当前哈希表中存储的元素
    int size;//当前哈希表的总大小
}hash_table;

bool insert(hash_table* h,const char* s);
bool expand(hash_table* h);

node* get_new_node(const char* s){
    node* p = (node*)malloc(sizeof(node));
    p->s = strdup(s);
    p->next = nullptr;
    return p;
}

hash_table* get_new_hash_table(int n){
    hash_table* h = (hash_table*)malloc(sizeof(hash_table));
    h->data = (node*)malloc(sizeof(node)*n);
    h->size = n;
    h->cnt = 0;
    for (int i = 0; i < n; i++) {
        h->data[i].s = nullptr;
        h->data[i].next = nullptr;
    }   
    return h;
}

//哈希函数
int hash_func(const char* s){
//字符串哈希算法
    int seed = 131;
    int h = 0;
    for(int i=0;s[i];i++){
        h = h*seed + s[i];
    }
    return h & 0x7fffffff;
}

//扩容操作
bool expand(hash_table* h){
    if(h==nullptr || h->data==nullptr ||
        h->size<=0 || h->size>INT_MAX/2){
        return false;
    }

    int old_size = h->size;
    int new_size = old_size*2;
    node* old_data = h->data;
    node* new_data = (node*)malloc(sizeof(node)*new_size);
    if(new_data==nullptr) return false;

    for(int i=0;i<new_size;i++){
        new_data[i].s = nullptr;
        new_data[i].next = nullptr;
    }

    for(int i=0;i<old_size;i++){
        node* p = old_data[i].next;
        while(p!=nullptr){
            node* next = p->next;
            int index = hash_func(p->s)%new_size;
            p->next = new_data[index].next;
            new_data[index].next = p;
            p = next;
        }
    }

    free(old_data);
    h->data = new_data;
    h->size = new_size;
    return true;
}

//插入操作
bool insert(hash_table* h,const char* s){
    //哈希表的扩容操作
    if(h->size>0 && h->cnt/h->size>=2){
        if(expand(h)==false) return false;
    }
    int hcode = hash_func(s);
    int index = hcode%h->size;
    //冲突处理(拉链法)
    node* new_node = get_new_node(s);
    //把新节点插入到对应位置链表的第一个元素
    new_node->next = h->data[index].next;
    h->data[index].next = new_node;
    h->cnt++;
    return true;
}

//查找操作
bool find(hash_table* h,const char* s){
    int hcode = hash_func(s);
    int index = hcode%h->size;
    node* p = h->data[index].next;
    while(p!=nullptr){
        if(strcmp(p->s,s) == 0) return true;
        p =p->next;
    }
    return false;
}


void clear_node(node* p){
    if(p==nullptr) return;
    if(p->s!=nullptr) free(p->s);
    free(p);
    return;
}

void clear_hash_table(hash_table* h){
    if(h==nullptr) return;
    for(int i=0;i<h->size;i++){
        node* p = h->data[i].next;
        node* temp = nullptr;
        while(p){
            temp = p->next;
            clear_node(p);
            p = temp;
        }
    }
    free(h->data);
    free(h);
    return;
}

void output(hash_table* h){
    printf("\n\nhash_table(%d/%d):\n",h->cnt,h->size);
    for(int i = 0;i<h->size;i++){
        printf("%d : ",i);
        node* p = h->data[i].next;
        while(p!=nullptr){
            printf("%s->",p->s);
            p = p->next;
        }
        printf("end");
        printf("\n");
    }
    return;
}

void test01(){
    char s[1000];
    hash_table* h = get_new_hash_table(MAX_N);
    while(~scanf("%999s",s)){
        if(strcmp(s,"end") == 0) break;
        insert(h,s);
    }
    output(h);
    while(~scanf("%999s",s)){
        if(find(h,s) == true) printf("成功找到%s\n",s);
    }
    clear_hash_table(h);
    return;
}

int main(void){
    srand(time(0));
    test01();
    system("pause");
    return 0;
}