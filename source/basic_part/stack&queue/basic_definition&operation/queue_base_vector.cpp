#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
//顺序表结构定义
typedef struct vector{
    int size;
    int count;
    int* data;
}vector;

//队列结构定义
typedef struct queue{
    int size;
    int count;
    vector* data;
    int tail;
    int head;
}queue;

//顺序表数据结构的操作
vector *create_vector(int size){
    vector* v = (vector*)malloc(sizeof(*v));
    v->data = (int*)malloc(sizeof(int)*size);
    v->size = size;
    v->count = 0;
    return v;
}

int clear_vector(vector* v){
    if(v==nullptr) return 0;
    free(v->data);
    free(v);
    return 1;
}

int set(vector* v, int pos, int val) {
    if (v == nullptr or pos < 0 or pos >= v->size) return 0;
    v->data[pos] = val;
    return 1;
}

int seek(vector* v,int pos){
    if(v==nullptr or pos<0 or pos>=v->size) return -1;
    return v->data[pos];
}


//队列机构操作
queue* create_queue(int size){
    queue* q=(queue*)malloc(sizeof(queue));
    q->data = create_vector(size);
    q->size = size;
    q->count = 0;
    q->tail = 0;
    q->head = 0;
    return q;
}

int push(queue* q,int val){
    if(q==nullptr or q->size == q->count) return 0;
    if(set(q->data,q->tail,val) == 0) return 0;
    //循环队列
    q->tail = (q->tail+1)%q->size;
    q->count++;
    return 1;
}

int pop(queue* q){
    if(q==nullptr or q->count==0) return 0;
    q->head = (q->head+1)%q->size;
    q->count--;
    return 1;
}

int front(queue* q){
    if(q==nullptr or q->count==0) return -1;
    return seek(q->data,q->head);
}

int clear_queue(queue* q){
    if(q==nullptr) return 0;
    clear_vector(q->data);
    free(q);
    return 1;
}

void test01(){
    printf("==== queue test (vector backend) ====\n");

    queue* q = create_queue(3);
    if(q == nullptr){
        printf("create_queue failed\n");
        return;
    }

    printf("+------+----------------+----------+--------+-------+------+------+");
    printf("\n| Case | Operation      | Expected | Actual | Front | Head | Tail |");
    printf("\n+------+----------------+----------+--------+-------+------+------+\n");

    int ret = 0;

    ret = front(q);
    printf("| %-4d | %-14s | %-8d | %-6d | %-5d | %-4d | %-4d |\n", 1, "front empty", -1, ret, front(q), q->head, q->tail);

    ret = pop(q);
    printf("| %-4d | %-14s | %-8d | %-6d | %-5d | %-4d | %-4d |\n", 2, "pop empty", 0, ret, front(q), q->head, q->tail);

    ret = push(q, 10);
    printf("| %-4d | %-14s | %-8d | %-6d | %-5d | %-4d | %-4d |\n", 3, "push 10", 1, ret, front(q), q->head, q->tail);

    ret = push(q, 20);
    printf("| %-4d | %-14s | %-8d | %-6d | %-5d | %-4d | %-4d |\n", 4, "push 20", 1, ret, front(q), q->head, q->tail);

    ret = push(q, 30);
    printf("| %-4d | %-14s | %-8d | %-6d | %-5d | %-4d | %-4d |\n", 5, "push 30", 1, ret, front(q), q->head, q->tail);

    ret = push(q, 40);
    printf("| %-4d | %-14s | %-8d | %-6d | %-5d | %-4d | %-4d |\n", 6, "push full", 0, ret, front(q), q->head, q->tail);

    ret = pop(q);
    printf("| %-4d | %-14s | %-8d | %-6d | %-5d | %-4d | %-4d |\n", 7, "pop", 1, ret, front(q), q->head, q->tail);

    ret = push(q, 40);
    printf("| %-4d | %-14s | %-8d | %-6d | %-5d | %-4d | %-4d |\n", 8, "push 40", 1, ret, front(q), q->head, q->tail);

    ret = pop(q);
    printf("| %-4d | %-14s | %-8d | %-6d | %-5d | %-4d | %-4d |\n", 9, "pop", 1, ret, front(q), q->head, q->tail);

    ret = pop(q);
    printf("| %-4d | %-14s | %-8d | %-6d | %-5d | %-4d | %-4d |\n", 10, "pop", 1, ret, front(q), q->head, q->tail);

    ret = pop(q);
    printf("| %-4d | %-14s | %-8d | %-6d | %-5d | %-4d | %-4d |\n", 11, "pop", 1, ret, front(q), q->head, q->tail);

    ret = pop(q);
    printf("| %-4d | %-14s | %-8d | %-6d | %-5d | %-4d | %-4d |\n", 12, "pop empty", 0, ret, front(q), q->head, q->tail);

    printf("+------+----------------+----------+--------+-------+------+------+");
    printf("\n");

    clear_queue(q);
}
int main(void){
    test01();
    system("pause");
    return 0;
}