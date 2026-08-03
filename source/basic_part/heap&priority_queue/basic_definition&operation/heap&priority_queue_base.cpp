/* #include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
typedef struct priority_queue{
    int *__data;//一个连续的数组
    int *data;
    int size;//队列空间的大小
    int n;//存储元素的个数
}priority_queue;

//大顶堆
#define cmp >
#define FATHER(i) ((i)/(2))
#define LEFT(i) ((i)*(2))
#define RIGHT(i) ((i)*(2)+(1))

//创建优先队列
priority_queue* initPQ(int size){
    priority_queue* p = (priority_queue*)malloc(sizeof(priority_queue));
    p->__data = (int *)malloc(sizeof(int)*size);
    p->data = p->__data-1;//下标偏移
    p->size = size;
    p->n=0;
    return p;
}

int empty(priority_queue*p){
    if(p==nullptr) return 0;
    return p->n==0;
}

int full(priority_queue*p){
    if(p==nullptr) return 0;
    return p->n==p->size;
}

int top(priority_queue *p){
    if(p==nullptr) return 0;
    if(p->data == nullptr) return 0;
    if(empty(p)) return 0;
    return p->data[1];
}

void swap(int *a , int *b){
    int temp = *a;
    *a = *b;
    *b = temp;
    return;
}
void  up_updata(int *data,int i){
    if(i==1) return;
    //递归的实现方法
    //if(data[i] cmp data[FATHER[i]]){
    //    swap(data[i],data[FATHER(i)]);
    //    up_update(data,FATHER(i));
    //} 
    while(i>1 and data[i] cmp data[FATHER(i)]){
        swap(&data[i],&data[FATHER(i)]);
        i = FATHER(i);
    }
    return ;
}

void down_update(int *data,int i,int n){
    //n为最大的下标
    int index = 0;
    while(LEFT(i)<=n){
        index = i;
        if(data[LEFT(i)] cmp data[index]) index = LEFT(i);
        if(RIGHT(i)<=n and data[RIGHT(i)] cmp data[index]) index = RIGHT(i);
        if(index == i) break;
        swap(&data[i],&data[index]);
        i = index;
    }
    return;
}

int push(priority_queue *p,int x){
    if(full(p)) return 0;
    if(p==nullptr) return 0;
    p->n ++;
    p->data[p->n] = x;
    up_updata(p->data, p->n);//数据空间以及要向上调整的元素的下标
    return 1;
}

int pop(priority_queue *p){
    if(p==nullptr) return 0;
    if(empty(p)) return 0;
    p->data[1] = p->data[p->n];
    p->n --;
    down_update(p->data,1,p->n);
    return 1;
}

void output(priority_queue* p){
    for(int i=0;i<p->n;i++){
        printf("%d ",p->data[i+1]);
    }
    printf("\n");
    return;
}

//堆排序
int* heap_sort(priority_queue* p){
    if(p==nullptr) return nullptr;
    if(p->data == nullptr or p->n==0) return nullptr;
    int* q = p->data;
    int n = p->n;
    for(int i=n;i>1;i--){
        swap(&q[1],&q[i]);
        down_update(p->data,1,i-1);
    }
    return q;
}


void clearPQ(priority_queue*p){
    if(p==nullptr) return;
    free(p->__data);
    free(p);
    return;
}


void test01(){
    const int max_op = 20;
    priority_queue *p = initPQ(10);

    printf("+------+--------+-------+--------+----------------------+\n");
    printf("| Step | Action | Value | Result | Priority Queue       |\n");
    printf("+------+--------+-------+--------+----------------------+\n");

    for(int i=1;i<=max_op;i++){
        int op = rand()%3;
        int value = rand()%100;
        int result = 0;

        if(op==0){
            result = push(p,value);
            printf("| %4d | push   | %5d | %6d | ",i,value,result);
            output(p);
        }else if(op==1){
            result = pop(p);
            printf("| %4d | pop    |     - | %6d | ",i,result);
            output(p);
        }else{
            result = top(p);
            printf("| %4d | top    |     - | %6d | ",i,result);
            output(p);
        }
    }

    printf("+------+--------+-------+--------+----------------------+\n");
    clearPQ(p);
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

//大顶堆
#define cmp >
#define FATHER(i) ((i)/(2))
#define LEFT(i) ((2)*(i))
#define RIGHT(i) ((2)*(i) + (1))

typedef struct priority_queue{
    int* data;
    int size;
    int cnt;
}priority_queue;

void swap(int* a,int* b){
    int temp = *a;
    *a = *b;
    *b = temp;
}


priority_queue* initPQ(int size){
    priority_queue* q = (priority_queue*)malloc(sizeof(priority_queue)*(1));
    q->size =size;
    q->cnt = 0;
    q->data = (int*)malloc(sizeof(int)*(size+1));
    return q;
}

int empty(priority_queue* q){
    if(q==nullptr) return 0;
    return q->cnt == 0;
}

int full(priority_queue* q){
    if(q==nullptr) return 0;
    return q->cnt == q->size;
}

int top(priority_queue* q){
    if(q==nullptr) return -1;
    if(q->data == nullptr) return -1;
    if(q->cnt == 0) return -1;
    return q->data[1];
}


//向下调整
void down_update(priority_queue* q,int pos,int cnt){
    if(q == nullptr or q->data==nullptr or pos<1 or cnt == 0) return;
    int index = pos;
    while(LEFT(pos)<=cnt){
        if(q->data[LEFT(pos)] cmp q->data[pos]){
            index = LEFT(pos);
        }
        if(RIGHT(pos) <= cnt and q->data[RIGHT(pos)] cmp q->data[index]){
            index = RIGHT(pos);
        }
        if(index == pos) break;
        swap(&q->data[pos],&q->data[index]);
        pos = index;
    }
    return ;
}

//优先队列的弹出操作（先进先出）
int pop(priority_queue* q){
    if(q==nullptr) return 0;
    if(empty(q)) return 0;
    swap(&q->data[1],&q->data[q->cnt]);
    q->cnt--;
    down_update(q,1,q->cnt);
    return 1;
}

//向上调整操纵
void up_update(int* data,int pos){
    if(data == nullptr) return;
    if(pos<1) return;
    while(pos >1){
        if(data[pos] cmp data[FATHER(pos)]) swap(&data[pos],&data[FATHER(pos)]);
        else break;
        pos = FATHER(pos);
    }
    return;
}


//优先队列的入队操作
int push(priority_queue* q,int val){
    if(q==nullptr) return 0;
    if(full(q)) return 0;
    q->cnt++;
    q->data[q->cnt] = val;
    int pos = q->cnt;
    up_update(q->data,pos);
    return 1;
}

void output(priority_queue* p){
    for(int i=0;i<p->cnt;i++){
        printf("%d ",p->data[i+1]);
    }
    printf("\n");
    return;
}

void clearPQ(priority_queue* q){
    if(q ==nullptr) return;
    free(q->data);
    free(q);
    return;
}

void test01(){
    const int max_op = 20;
    priority_queue *p = initPQ(10);

    printf("+------+--------+-------+--------+----------------------+\n");
    printf("| Step | Action | Value | Result | Priority Queue       |\n");
    printf("+------+--------+-------+--------+----------------------+\n");

    for(int i=1;i<=max_op;i++){
        int op = rand()%3;
        int value = rand()%100;
        int result = 0;

        if(op==0){
            result = push(p,value);
            printf("| %4d | push   | %5d | %6d | ",i,value,result);
            output(p);
        }else if(op==1){
            result = pop(p);
            printf("| %4d | pop    |     - | %6d | ",i,result);
            output(p);
        }else{
            result = top(p);
            printf("| %4d | top    |     - | %6d | ",i,result);
            output(p);
        }
    }

    printf("+------+--------+-------+--------+----------------------+\n");
    clearPQ(p);
}

int main(void){
    srand(time(0));
    test01();
    system("pause");
    return 0;
}

