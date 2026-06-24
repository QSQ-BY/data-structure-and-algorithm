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

//Ã°ÅÝÅÅÐò
void bubble_sort(int* arr,int l,int r){
    for(int i = r-1;i>=l+1;i--){
        for(int j = l;j<i;j++){
            if(arr[j] > arr[j+1]) swap(&arr[j],&arr[j+1]);
        }
    }
    return;
}

//Ã°ÅÝÅÅÐòµÄÓÅ»¯
void better_bubble_sort(int* arr,int l,int r){
    for(int i = r-1;i>=l+1;i--){
        int flag = 0;
        for(int j = l;j<i;j++){
            if(arr[j]>arr[j+1]){
                swap(&arr[j],&arr[j+1]);
                if(flag == 0){
                    flag = 1;
                }
            }
        }
        if(flag == 0) return;
    }
}

void test01(){
    int* arr = get_rand_data(SMALL_DATA_N);
    TEST(bubble_sort,arr,SMALL_DATA_N);
    TEST(better_bubble_sort,arr,SMALL_DATA_N);
    free(arr);
    return;
}

void test02(){
    int* arr = get_rand_data(BIG_DATA_N);
    TEST(bubble_sort,arr,BIG_DATA_N);
    TEST(better_bubble_sort,arr,BIG_DATA_N);
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