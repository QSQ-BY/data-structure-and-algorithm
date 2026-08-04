#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <unordered_map>
#include <unordered_set>
#include <stack>
#include <queue>
using namespace std;

void merge_sort(int* arr,int l,int r){//×ó±ÕÓÒ¿ªÇø¼ä
    int n = r-l;
    if(r - l <=1) return;
    int mid = (l+r)/2;
    merge_sort(arr,l,mid);
    merge_sort(arr,mid,r);
    int* temp = (int*)malloc(sizeof(int)*(r-l));
    int p1 = l;
    int p2 = mid;
    int p = 0;
    while(p1<mid or p2<r){
        if((p2<r and p1<mid and arr[p1] <= arr[p2]) or p2==r){
            temp[p] = arr[p1];
            p++;
            p1++;
        }else{
            temp[p] = arr[p2];
            p++;
            p2++;
        }
    }
    for(int i = l;i<r;i++) arr[i] = temp[i-l];
    free(temp);
    return ;
}

class Data{
public:
    Data(int l,int r){
        this->l = l;
        this->r = r;
    }
    int l;
    int r;
};

void merge_sort_once(int* arr,int l,int r){
    int mid = (l+r)/2;
    int* temp = (int*)malloc(sizeof(int)*(r-l+1));
    int p1 = l;
    int p2 = mid;
    int p = 0;
    while(p1<mid or p2<r){
        if((p2<r and p1<mid and arr[p1] <= arr[p2]) or p2==r){
            temp[p] = arr[p1];
            p++;
            p1++;
        }else{
            temp[p] = arr[p2];
            p++;
            p2++;
        }
    }
    for(int i = l;i<r;i++) arr[i] = temp[i-l];
    free(temp);
    return;
} 

void non_merge_sort(int* arr,int l,int r){
    Data init_data(l,r);
    vector<Data> datas;
    datas.push_back(init_data);
    for(int i=0;i<datas.size();i++){
        int mid = (datas[i].l+datas[i].r)/2;
        if(mid-datas[i].l>=2){
            Data new_data(datas[i].l,mid);
            datas.push_back(new_data);
        }
        if(datas[i].r-mid>=2){
            Data new_data(mid,datas[i].r);
            datas.push_back(new_data);
        }
    }
    for(int i=datas.size()-1;i>=0;i--){
        merge_sort_once(arr,datas[i].l,datas[i].r);
    }
    return;
}

void test01(){
    
}

int main(void){
    test01();
    system("pause");
    return 0;
}