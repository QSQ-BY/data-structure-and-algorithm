#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <stdbool.h>

#define SMALL_DATA_N 5000
#define BIG_DATA_N 100000

bool check(int *arr,int l,int r){
    for(int i=l+1;i<r;i++){
        if(arr[i] < arr[i-1]) return false;
    }
    return true;
}

#define TEST(func,arr,n){ \
    printf("Test %s :",#func); \
    int *temp = (int*)malloc(sizeof(int)*n); \
    memcpy(temp,arr,sizeof(int)*n); \
    long long begin = clock(); \
    func(temp,0,n); \
    long long end = clock(); \
    if(check(temp,0,n)){ \
        printf("\tOK "); \
    }else { \
        printf("\tFailed"); \
    } \
    printf("%d items %lld ms\n",n,(end - begin)*1000/CLOCKS_PER_SEC); \
    free(temp); \
}

int* get_rand_data(int n){
    int *ret = (int*)malloc(sizeof(int)*n);
    for(int i = 0;i<n;i++){
        ret[i] = rand()%1000;
    }
    return ret;
}

void swap(int* a,int* b){
    int temp = *a;
    *a = *b;
    *b = temp;
    return;
}

//插入排序
void insert_sort(int* arr,int l,int r){
    for(int i = l+1;i<r;i++){
        int j = i;
        while(j>l and arr[j]<arr[j-1]){
            swap(&arr[j],&arr[j-1]);
            j--;
        }
    }
    return;
}


//无监督的 插入排序
void unsupervised_insert_sort(int* arr,int l,int r){
    //把全局最小值先放到第一个位置上来
    //可以去掉j>l的判断条件
    int index = l;
    for(int i = l+1;i<r;i++){
        if(arr[i] <arr[index]) index = i;
    }
    //swap(&arr[l],&arr[index]);
    while(index > l){
        swap(&arr[index],&arr[index-1]);
        index--;
    }
    for(int i = l+1;i<r;i++){
        int j = i;
        while(arr[j]<arr[j-1]){
            swap(&arr[j],&arr[j-1]);
            j--;
        }
    }
}

void test01(){
    int* arr = get_rand_data(SMALL_DATA_N);
    TEST(insert_sort,arr,SMALL_DATA_N);
    TEST(unsupervised_insert_sort,arr,SMALL_DATA_N);
    free(arr);
    return;
}

void test02(){
    int* arr = get_rand_data(BIG_DATA_N);
    TEST(insert_sort,arr,BIG_DATA_N);
    TEST(unsupervised_insert_sort,arr,BIG_DATA_N);
    free(arr);
    return;
}


int main(void){
    srand(time(0));
    test01();
    test02();
    system("pause");
    return 0;
}