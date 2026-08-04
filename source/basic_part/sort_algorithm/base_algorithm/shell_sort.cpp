#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <stdbool.h>

#define SMALL_DATA_N 5000
#define BIG_DATA_N 1000000

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

void unsupervised_insert_sort(int* arr,int l,int r,int step){
    int index = l;
    for(int i = l+step;i<r;i += step){
        if(arr[i] < arr[index]) index = i;
    }
    while(index > l){
        swap(&arr[index],&arr[index-step]);
        index-= step;
    }
    for(int i = l+step;i<r;i+=step){
        int j = i;
        while(arr[j]<arr[j-step]){
            swap(&arr[j],&arr[j-step]);
            j-=step;
        }
    }
}

//Ï£¶ûÅÅÐò
void shell_sort(int* arr,int l,int r){
    int k = 2;
    int n = r-l;
    int step = n/k;
    
    do{
        if(step == 0) step = 1;
        else step = n/k;
        int len = l+step;
        for(int i = l;i<len;i++){
            unsupervised_insert_sort(arr,i,r,step);
        }
        k = k*2;
    }while(step != 1);
    return;

}

void shell_sort_hibbard(int *arr,int l,int r){
    int step = 1;
    int n = r-l;
    while(step<=n/2) step = step*2+1;
    do{
        step = step/2;
        int len = l+step;
        for(int i = l;i<len;i++){
            unsupervised_insert_sort(arr,i,r,step);
        }
        
    }while(step>1);
    return;
}

void test01(){
    int* arr = get_rand_data(SMALL_DATA_N);
    TEST(shell_sort_hibbard,arr,SMALL_DATA_N);
    TEST(shell_sort,arr,SMALL_DATA_N);
    free(arr);
    return;
}

void test02(){
    int* arr = get_rand_data(BIG_DATA_N);
    TEST(shell_sort_hibbard,arr,BIG_DATA_N);
    TEST(shell_sort,arr,BIG_DATA_N);
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