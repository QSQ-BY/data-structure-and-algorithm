//基数排序
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <stdbool.h>

#define SMALL_DATA_N 5000
#define BIG_DATA_N 1000000000

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

void radix_sort(int* arr,int l,int r){
    #define K 100
    int* cnt = (int*)malloc(sizeof(int) * K);
    int* temp = (int*)malloc(sizeof(int) * (r-l));

    //第一轮排序，按照后位进行排序
    memset(cnt,0,sizeof(int) * K);
    for(int i=l;i<r;i++){
        cnt[arr[i] % K] += 1;
    }
    for(int i = 1;i<K;i++) cnt[i] += cnt[i-1];
    for(int i = r-1;i>=l;i--) temp[--cnt[arr[i] % K]] = arr[i];
    memcpy(arr + l,temp,sizeof(int) * (r-l));

    //第二轮排序，按照前位进行排序
    memset(cnt,0,sizeof(int) * K);
    for(int i=l;i<r;i++){
        cnt[arr[i] / K] += 1;
    }
    for(int i = 1;i<K;i++) cnt[i] += cnt[i-1];
    for(int i = r-1;i>=l;i--) temp[--cnt[arr[i] / K]] = arr[i];
    memcpy(arr + l,temp,sizeof(int) * (r-l));

    free(temp);
    free(cnt);
    return;
}

void test01(){
    int* arr = get_rand_data(SMALL_DATA_N);
    TEST(radix_sort,arr,SMALL_DATA_N);
    free(arr);
    return;
}

void test02(){
    int* arr = get_rand_data(BIG_DATA_N);
    TEST(radix_sort,arr,BIG_DATA_N);
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