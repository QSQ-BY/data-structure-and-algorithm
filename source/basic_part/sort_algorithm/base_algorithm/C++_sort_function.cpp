//C++中sort方法的使用和使用技巧
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <stdlib.h>
#include <time.h>

using namespace std;

int* get_rand_data(int n){
    int *ret = (int*)malloc(sizeof(int)*n);
    for(int i = 0;i<n;i++){
        ret[i] = rand()%1000;
    }
    return ret;
}

void output(int* arr , int n){
    printf("arr[%d] = ",n);
    for(int i=0;i<n;i++){
        printf("%d ",arr[i]);
    }
    printf("\n");
    return;
}

void output(vector<int> &arr){
    printf("arr[%d] = ",arr.size());
    for(int i=0;i<arr.size();i++){
        printf("%d ",arr[i]);
    }
    printf("\n");
    return;
}



//sort的基础使用,对于原生数组
void test01(){
    printf("\ntest array :\n");
    int* arr = get_rand_data(10);
    output(arr,10);
    //std::sort()
    sort(arr,arr+10);//区间为左闭右开
    output(arr,10);//默认为从小到大的排序规则
    //从大到小进行排序
    sort(arr,arr+10,greater<int>());
    output(arr,10);
    free(arr);
    return;
}

//sort方法对vector进行排序
void test02(){
    printf("\ntest vector :\n");
    vector<int> arr;
    for(int i = 0;i<10;i++) arr.push_back(rand() % 1000);
    output(arr);
    sort(arr.begin(), arr.end());
    output(arr);
    sort(arr.begin(),arr.end(),greater<int>());
    output(arr);
    return;
}

class Data{
public:
    int x;
    int y;
};

//比较规则函数
bool cmp(Data a, Data b){
    if(a.x != b.x) return a.x<b.x;
    return a.y < b.y;
}

void output(vector<Data> arr){
    for(int i = 0;i<arr.size();i++){
        printf("(%d,%d) ", arr[i].x,arr[i].y);
    }
    printf("\n");
    return;
}

//自定义数据类型的比较、排序
void test03(){
    printf("\ntest my data structure :\n");
    vector<Data> arr;
    for(int i = 0;i<10;i++){
        Data d;
        d.x = rand()%10;
        d.y = rand()%10;
        arr.push_back(d);
    }
    output(arr);
    sort(arr.begin(),arr.end(),cmp);//使用自定义的函数，返回值是布尔类型
    output(arr);
    return;
}

void output(int* arr,int n,const char* s){
    printf("%s[%d] = ",s,n);
    for(int i=0;i<n;i++){
        printf("%d ",arr[i]);
    }
    printf("\n");
    return;
}
//排序不改变原数组，对数组的下标进行排序
void test04(){
    printf("\ntest sort index :\n");
    int* arr = get_rand_data(10);
    int* index = get_rand_data(10);
    for(int i = 0;i<10;i++) index[i] = i;
    output(arr,10);
    //lambda表达式实现比较规则
    sort(index, index + 10, [&](int i, int j)->bool {
        return arr[i] < arr[j];
    });
    output(arr,10);
    output(index,10,"index");
    return;
}

int main(void){
    srand(time(0));
    test01();
    test02();
    test03();
    test04();
    system("pause");
    return 0;
}