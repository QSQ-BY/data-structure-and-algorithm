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

//快速排序
void quick_sort(int* arr,int l,int r){
    if(arr == nullptr) return;
    if(r-l <= 2){
        if(r-l<=1) return;
        else{
            if(arr[l] <= arr[l+1]) return;
            else swap(&arr[l],&arr[l+1]);
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


void test01(){
    int* arr = get_rand_data(SMALL_DATA_N);
    TEST(quick_sort,arr,SMALL_DATA_N);
    free(arr);
    return;
}

void test02(){
    int* arr = get_rand_data(BIG_DATA_N);
    TEST(quick_sort,arr,BIG_DATA_N);
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