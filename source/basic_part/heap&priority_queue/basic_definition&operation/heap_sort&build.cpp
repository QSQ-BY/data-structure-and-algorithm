//堆排序与线性建堆法
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
//#include <bool.h>
#define cmp >
#define ROOT 1
#define FATHER(i) ((i)/(2))
#define LEFT(i) ((i)*(2))
#define RIGHT(i) ((i)*(2)+(1))

#define TEST(func,arr,n){ \
    printf("TEST:%s\n",#func); \
    int *temp = (int *)malloc(sizeof(int)*n); \
    memcpy(temp ,arr , sizeof(int)*n); \
    long long begin =clock(); \
    func(temp ,n); \
    long long end =clock(); \
    if(check(temp , n)){ \
        printf("OK\t"); \
    }else { \
        printf("FAIL\t"); \
    } \
    printf("%lld ms\n",1000*(end - begin)/CLOCKS_PER_SEC); \
    free(temp); \
} \


void swap(int *a,int *b){
    int temp = *a;
    *a = *b;
    *b = temp;
    return;
}

int* getRandData(int n){
    int *arr = (int*)malloc(sizeof(int)*n);
    for(int i=0;i<n;i++){
        arr[i] = rand()%1000;
    }
    return arr;
}

bool check(int *arr,int n){
    for(int i=1;i<n;i++){
        if(arr[i]<arr[i-1]) return false;
    }
    return true;
}

inline void up_update(int *data,int i){
    while(i>1 and data[i] cmp data[FATHER(i)]){
        swap(&data[i],&data[FATHER(i)]);
        i = FATHER(i);
    }
    return;
}

inline void down_update(int *data, int i, int n){
    int index = i;
    while(LEFT(i) <= n){
        index = i;
        if(data[LEFT(i)] cmp data[index]){
            index = LEFT(i);
        }
        if(RIGHT(i) <= n && data[RIGHT(i)] cmp data[index]){
            index = RIGHT(i);
        }
        if(index == i) break;
        swap(&data[i], &data[index]);
        i = index;
    }
}

inline void normal_heap_build(int* data,int n){
    for(int i = 2;i<=n;i++){
        up_update(data,i);
    }
    return;
}

inline void linear_heap_build(int *data,int n){
    for(int i = n/2;i>=1;i--){
        down_update(data,i,n);
    }
    return ;
}

//堆排序
void heap_sort_final(int* data,int n){
    for(int i=n;i>=1;i--){
        swap(&data[i],&data[1]);
        down_update(data,1,i-1);
    }
    return;
}

void normal_heap(int* arr,int n){
    int* data =arr-1;
    normal_heap_build(data,n);
    heap_sort_final(data,n);
    return;
}


void linear_heap(int* arr,int n){
    int* data = arr-1;
    linear_heap_build(data,n);
    heap_sort_final(data,n);
    return;
}

void test01(){
    #define MAX_N 10000000
    int* arr = getRandData(MAX_N);
    TEST(normal_heap,arr,MAX_N);
    TEST(linear_heap,arr,MAX_N);
}
int main(void){
    srand(time(0));
    test01();
    system("pause");
    return 0;
}




/* #include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#define ROOT 1
#define FATHER(i) ((i)/(2))
#define LEFT(i) ((2)*(i))
#define RIGHT(i) ((i)*(2) + (1))
#define cmp >
void swap(int* a,int* b){
    int temp = *a;
    *a = *b;
    *b = temp;
}

void down_update(int* data,int pos,int n){
    int index = pos;
    while(LEFT(pos)<=n){
        index = pos;
        if(data[LEFT(pos)] cmp data[pos]) index = LEFT(pos);
        if(RIGHT(pos) <= n and data[RIGHT(pos)] cmp data[index]) index = RIGHT(pos);
        if(index == pos) break;
        swap(&data[pos],&data[index]);
        pos = index;
    }
    return;
}
void up_update(int* data,int pos){
    while(pos>1){
        if(data[pos] cmp data[FATHER(pos)]){
            swap(&data[pos] , &data[FATHER(pos)]);
        }else break;
        pos = FATHER(pos);
    }
    return;
}

void heap_sort(int* data,int n){
    for(int i = n;i>=1;i--){
        swap(&data[i],&data[1]);
        down_update(data,1,i-1);
    }
    return;
}

void normal_heap_build(int* data,int n){
    for(int i = 0;i<n;i++){
        up_update(data,i+1);
    }
    return;
}

void linear_heap_build(int* data,int n){
    for(int i =n/2 ; i>=1;i--){
        down_update(data,i,n);
    }
    return;
}

void normal_heap(int* arr,int n){
    int* data = arr-1;
    normal_heap_build(data,n);
    heap_sort(data,n);
    return;
}

void linear_heap(int* arr,int n){
    int* data = arr-1;
    linear_heap_build(data,n);
    heap_sort(data,n);
    return;
}
void test01(){
    return;
}

int main(void){
    srand(time(0));
    test01();
    system("pause");
    return 0;
} */