#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

//链表的结构定义和结构操作
typedef struct node {
    int data;
    struct node* next;
}node;

typedef struct linklist{
    //node head;//有头链表
    node* head;//无头链表
    node* tail;
    int count;
}linklist;

linklist* create_linklist(){
    linklist* l = (linklist*)malloc(sizeof(*l));
    if(l==nullptr) return nullptr;
    l->head = nullptr;
    l->tail = nullptr;
    l->count = 0;
    return l;
}

int front_list(linklist* l){
    if(l==nullptr or l->count == 0) return -1;
    return l->head->data;
}

int insertTail(linklist* l,int val){
    if(l == nullptr) return 0;

    node* new_node = (node*)malloc(sizeof(node));
    if(new_node == nullptr) return 0;

    new_node->data = val;
    new_node->next = nullptr;

    if(l->count == 0){
        l->head = new_node;
        l->tail = new_node;
    }else{
        l->tail->next = new_node;
        l->tail = new_node;
    }

    l->count++;
    return 1;
}
int erase_head(linklist* l){
    if(l == nullptr || l->count == 0) return 0;

    node* temp = l->head;
    l->head = l->head->next;
    free(temp);

    l->count--;

    if(l->count == 0){
        l->tail = nullptr;
    }

    return 1;
}
void clear_linklist(linklist* l){
    if(l==nullptr) return;

    node* p = l->head;
    node* temp;
    while(p){
        temp = p->next;
        free(p);
        p = temp;
    }
    free(l);
    return;
}
//队列的结构定义和结构操作
typedef struct queue{
    linklist* data;
    int count;
}queue;

int empty(queue* q){
    return q == nullptr || q->count == 0;
}
int front(queue* q){
    if(empty(q)) return -1;
    return front_list(q->data);
}
int push(queue* q,int val){
    if(q == nullptr) return 0;

    if(insertTail(q->data,val) == 0) return 0;

    q->count++;
    return 1;
}
int pop(queue* q){
    if(q == nullptr || q->count == 0) return 0;

    if(erase_head(q->data) == 0) return 0;

    q->count--;
    return 1;
}
queue* create_queue(){
    queue* q = (queue*)malloc(sizeof(queue));
    q->data = create_linklist();
    q->count = 0;
    return q;
}

void clear_queue(queue* q){
    if(q == nullptr) return;
    clear_linklist(q->data);
    free(q);
    return;
}
void test01(){
    printf("==== queue test (linklist backend) ====\n");

    queue* q = create_queue();
    if(q == nullptr || q->data == nullptr){
        printf("create_queue failed\n");
        clear_queue(q);
        return;
    }

    printf("+------+----------------+----------+--------+-------+--------+--------+------+------+\n");
    printf("| Case | Operation      | Expected | Actual | Front | QCount | LCount | Head | Tail |\n");
    printf("+------+----------------+----------+--------+-------+--------+--------+------+------+\n");

    int ret = 0;

    ret = front(q);
    printf("| %-4d | %-14s | %-8d | %-6d | %-5d | %-6d | %-6d | %-4d | %-4d |\n",
           1, "front empty", -1, ret, front(q), q->count, q->data->count,
           q->data->head ? q->data->head->data : -1,
           q->data->tail ? q->data->tail->data : -1);

    ret = pop(q);
    printf("| %-4d | %-14s | %-8d | %-6d | %-5d | %-6d | %-6d | %-4d | %-4d |\n",
           2, "pop empty", 0, ret, front(q), q->count, q->data->count,
           q->data->head ? q->data->head->data : -1,
           q->data->tail ? q->data->tail->data : -1);

    ret = push(q, 10);
    printf("| %-4d | %-14s | %-8d | %-6d | %-5d | %-6d | %-6d | %-4d | %-4d |\n",
           3, "push 10", 1, ret, front(q), q->count, q->data->count,
           q->data->head ? q->data->head->data : -1,
           q->data->tail ? q->data->tail->data : -1);

    ret = push(q, 20);
    printf("| %-4d | %-14s | %-8d | %-6d | %-5d | %-6d | %-6d | %-4d | %-4d |\n",
           4, "push 20", 1, ret, front(q), q->count, q->data->count,
           q->data->head ? q->data->head->data : -1,
           q->data->tail ? q->data->tail->data : -1);

    ret = pop(q);
    printf("| %-4d | %-14s | %-8d | %-6d | %-5d | %-6d | %-6d | %-4d | %-4d |\n",
           5, "pop", 1, ret, front(q), q->count, q->data->count,
           q->data->head ? q->data->head->data : -1,
           q->data->tail ? q->data->tail->data : -1);

    ret = push(q, 30);
    printf("| %-4d | %-14s | %-8d | %-6d | %-5d | %-6d | %-6d | %-4d | %-4d |\n",
           6, "push 30", 1, ret, front(q), q->count, q->data->count,
           q->data->head ? q->data->head->data : -1,
           q->data->tail ? q->data->tail->data : -1);

    ret = pop(q);
    printf("| %-4d | %-14s | %-8d | %-6d | %-5d | %-6d | %-6d | %-4d | %-4d |\n",
           7, "pop", 1, ret, front(q), q->count, q->data->count,
           q->data->head ? q->data->head->data : -1,
           q->data->tail ? q->data->tail->data : -1);

    ret = pop(q);
    printf("| %-4d | %-14s | %-8d | %-6d | %-5d | %-6d | %-6d | %-4d | %-4d |\n",
           8, "pop", 1, ret, front(q), q->count, q->data->count,
           q->data->head ? q->data->head->data : -1,
           q->data->tail ? q->data->tail->data : -1);

    ret = pop(q);
    printf("| %-4d | %-14s | %-8d | %-6d | %-5d | %-6d | %-6d | %-4d | %-4d |\n",
           9, "pop empty", 0, ret, front(q), q->count, q->data->count,
           q->data->head ? q->data->head->data : -1,
           q->data->tail ? q->data->tail->data : -1);

    printf("+------+----------------+----------+--------+-------+--------+--------+------+------+\n");

    clear_queue(q);
}
int main(void){
    test01();
    system("pause");
    return 0;
}