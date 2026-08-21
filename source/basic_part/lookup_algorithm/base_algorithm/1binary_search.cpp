//二分查找算法
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <time.h>

using namespace std;
void output(int* arr,int n){
    int len = 0;
    for(int i=0;i<n;i++){
        len+= printf("%4d",i);
    }
    printf("\n");
    //for(int i = 0;i<n;i++) printf("-");
    //printf("\n");
    for(int i=0;i<n;i++){
        printf("%4d" ,arr[i]);
    }
    printf("\n");
    for(int i = 0;i<len;i++) printf("-");
    printf("\n");
    return;
}

void test_binary_search(int n){
    //生成随机的有序数组
    int* arr = (int*)malloc(sizeof(int) * n);
    arr[0] = rand()%10;
    for(int i = 1;i<n;i++) arr[i] = arr[i-1] + rand()%10;
    output(arr,n);

    //二分查找算法
    int target = 0;
    int pos = -1;
    while(~scanf("%d",&target)){
        if(target==-1) break;//如果查找目标为-1则退出，否则从arr数组中进行查找
        int left = 0;
        int right = n-1;
        while(left<right){
            int mid = right + (left-right)/2;
            if(target == arr[mid]){
                pos = mid;
                break;
            }
            if(target > arr[mid]){
                left = mid+1;
            }
            if(target < arr[mid]){
                right = mid-1;
            }
        }
        if(pos == -1) printf("没有在数组中找到%d\n",target);
        else printf("成功在%d位置找到%d\n",pos,target);
        pos = -1;
    }
    free(arr);
    return;
}

#define min(a,b) ((a) < (b) ? (a):(b))
//根据税前工资得到税后工资
double f(double x){
    if(x >= 0) x-= min(x,3000) * 0.03;
    if(x>3000) x-=(min(x,12000) - 3000)*0.1;
    if(x > 12000) x-=(min(x,25000) - 12000)*0.2;
    if(x > 25000) x-=(min(x,35000) - 25000)*0.25;
    if(x > 35000) x-=(min(x,55000) - 35000)*0.3;
    if(x > 55000) x-=(min(x,80000) - 55000)*0.35;
    if(x > 80000) x-=(x - 80000)*0.45;
    return x;
}


//二分算法
#define EXP 1e-4
double binary_algorithm(int y){

    double left = 0.0;
    double right = 100000000.0;
    double mid = 0.0;
    while(abs(left - right)>=EXP){
        mid = right + (left-right)/2;
        if(y == f(mid)){
            break;
        }
        if(y > f(mid)){
            left = mid+1;
        }
        if(y < f(mid)){
            right = mid-1;
        }
    }
    return mid;
}


//使用二分算法根据税后收入求解税前收入(根据y求解x)
void test_binary_algorithm(){
    double y;
    while(~scanf("%lf",&y)){
        if(y<0) break;
        double x = binary_algorithm(y);
        printf("f(%lf) = %lf\n",x,y);
    }
    return;
}

int main(void){
    srand(time(0));
    #define MAX_N 10
    //test_binary_search(MAX_N);
    test_binary_algorithm();//根据税后收入求解税前收入
    system("pause");
    return 0;
}