#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <stdbool.h>

#define SMALL_DATA_N 5000
#define BIG_DATA_N 100000000

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

//快速排序
void quick_sort(int* arr,int l,int r){
    if(arr == nullptr) return;
    if(r-l <= 2){
        if(r-l<=1) return;
        else{
            if(arr[l] <= arr[l+1]) return;
            else {
                swap(&arr[l],&arr[l+1]);
                return;
            }
        }
    }

    //分区过程 partition
    int left_index = l;
    int right_index = r-1;
    int base_number = arr[left_index];
    while(left_index != right_index){
        while(left_index<right_index and base_number <= arr[right_index]) right_index--;
        if(left_index < right_index){
            arr[left_index] = arr[right_index];
            left_index++;
        }

        while(left_index < right_index and base_number>= arr[left_index]) left_index++;
        if(left_index < right_index){
            arr[right_index] = arr[left_index];
            right_index--;
        }
    }
    arr[left_index] = base_number;
    quick_sort(arr,l,left_index);
    quick_sort(arr,left_index+1,r);
    return;
}

//快速排序的优化
void quick_sort_v1(int* arr,int l,int r){
    //每次左右指针找到一对元素对他们进行交换操作
    if(arr==nullptr) return;
    if(r==l) return;
    if(r-1 == l) return;
    else if(r-2 == l){
        if(arr[l]>arr[l+1]) {
            swap(&arr[l],&arr[l+1]);
            return;
        }
        else return;
    }

    //分区操作
    int left_index = l;
    int right_index = r-1;
    int base_number = arr[l];
    do{
        while(arr[left_index] < base_number) left_index++;
        while(arr[right_index] > base_number) right_index--;
        if(left_index <= right_index){
            swap(&arr[left_index],&arr[right_index]);
            left_index++;
            right_index--;
        }
    }while(left_index <= right_index);
    quick_sort_v1(arr,l,left_index);
    quick_sort_v1(arr,left_index,r);
    return;
}


void three_point_sort(int* arr, int l, int r){
    int mid = l + (r - l) / 2;

    if(arr[l] > arr[mid]) swap(&arr[l], &arr[mid]);
    if(arr[l] > arr[r - 1]) swap(&arr[l], &arr[r - 1]);
    if(arr[mid] > arr[r - 1]) swap(&arr[mid], &arr[r - 1]);
}

void quick_sort_v2(int* arr,int l,int r){
    //优化基准值的选择（三点取中法）
    if(arr==nullptr) return;
    if(r - l <= 1) return;
    if(r-1 == l) return;
    else if(r-2 == l){
        if(arr[l]>arr[l+1]) {
            swap(&arr[l],&arr[l+1]);
            return;
        }
        else return;
    }
    //分区操作
    int left_index = l;
    int right_index = r-1;
    three_point_sort(arr, l, r);
    int base_number = arr[l + (r - l) / 2];
    do{
        while(arr[left_index] < base_number) left_index++;
        while(arr[right_index] > base_number) right_index--;
        if(left_index <= right_index){
            swap(&arr[left_index],&arr[right_index]);
            left_index++;
            right_index--;
        }
    }while(left_index <= right_index);
    quick_sort_v2(arr,l,left_index);
    quick_sort_v2(arr,left_index,r);
    return;
}

void quick_sort_v3(int* arr,int l,int r){
    //减少递归次数（单边递归法）
    
    if(arr==nullptr) return;
    if(r-1 == l) return;
    else if(r-2 == l){
        if(arr[l]>arr[l+1]) {
            swap(&arr[l],&arr[l+1]);
            return;
        }
        else return;
    }

    //分区操作
    while(l<r){
        int left_index = l;
        int right_index = r-1;
        three_point_sort(arr, l, r);
        int base_number = arr[l + (r - l) / 2];
        //int base_number = arr[l];
        do{
            while(arr[left_index] < base_number) left_index++;
            while(arr[right_index] > base_number) right_index--;
            if(left_index <= right_index){
                swap(&arr[left_index],&arr[right_index]);
                left_index++;
                right_index--;
            }
        }while(left_index <= right_index);
        quick_sort_v3(arr,l,left_index);//左半区间的递归操作
        //quick_sort_v3(arr,left_index,r);//右半区间的递归
        l = left_index;
        
    }
    return;
}
#define threshold 16
void __quick_sort_v4(int* arr,int l,int r){
    //在小数据量的时候更改为插入排序

    
    if(arr==nullptr) return;
    if(r-1 == l) return;
    else if(r-2 == l){
        if(arr[l]>arr[l+1]) {
            swap(&arr[l],&arr[l+1]);
            return;
        }
        else return;
    }

    //分区操作
    while(r-l >threshold){
        int left_index = l;
        int right_index = r-1;
        three_point_sort(arr, l, r);
        int base_number = arr[l + (r - l) / 2];
        //int base_number = arr[l];
        do{
            while(arr[left_index] < base_number) left_index++;
            while(arr[right_index] > base_number) right_index--;
            if(left_index <= right_index){
                swap(&arr[left_index],&arr[right_index]);
                left_index++;
                right_index--;
            }
        }while(left_index <= right_index);
        __quick_sort_v4(arr,l,left_index);//左半区间的递归操作
        //quick_sort_v3(arr,left_index,r);//右半区间的递归
        l = left_index;
        
    }
    return;
}

void unsupervised_insert_sort(int* arr,int l,int r){
    if(arr == nullptr) return;
    if(r - l <= 1) return;
    int index = l;
    for(int i = l;i<r;i++){
        if(arr[i] < arr[index]) index = i;
    }
    swap(&arr[l],&arr[index]);
    for(int i = l+2;i<r;i++){
        int j = i;
        while(arr[j]<arr[j-1]){
            swap(&arr[j],&arr[j-1]);
            j--;
        }
    }
}

void quick_sort_v4(int* arr,int l,int r){
    if(arr == nullptr) return;
    if(r - l <= 1) return;
    __quick_sort_v4(arr,l,r);
    unsupervised_insert_sort(arr,l,r);
    return;
}

void test01(){
    int* arr = get_rand_data(SMALL_DATA_N);
    TEST(quick_sort,arr,SMALL_DATA_N);
    TEST(quick_sort,arr,SMALL_DATA_N);
    TEST(quick_sort,arr,SMALL_DATA_N);
    TEST(quick_sort,arr,SMALL_DATA_N);
    TEST(quick_sort,arr,SMALL_DATA_N);
    free(arr);
    return;
}

void test02(){
    int* arr = get_rand_data(BIG_DATA_N);
    //TEST(quick_sort,arr,BIG_DATA_N);
    TEST(quick_sort_v1,arr,BIG_DATA_N);
    TEST(quick_sort_v2,arr,BIG_DATA_N);
    TEST(quick_sort_v3,arr,BIG_DATA_N);
    TEST(quick_sort_v4,arr,BIG_DATA_N);
    free(arr);
    return;
}


int main(void){
    srand(time(0));
    //test01();
    test02();
    system("pause");
    return 0;
}