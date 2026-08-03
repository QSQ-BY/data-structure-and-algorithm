//快速排序递归转为非递归

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
void swap(int* a,int* b){
    int temp = *a;
    *a = *b;
    *b = temp;
}

void quick_sort(int* arr,int l,int r);

struct Data{
    Data(int* arr,int l,int r){
        this->arr = arr;
        this->l = l;
        this->r = r;
        this->scode = 0;;
        this->left_index = this->l;
        this->right_index = this->r-1;
        this->base_number = 0;
    }
    int *arr;
    int l;
    int r;
    int left_index,right_index,base_number;
    int scode;
};

void non_quick_sort(int* arr,int l,int r){
    stack<Data> s;
    Data d(arr,l,r);
    s.push(d);
    while(!s.empty()){
        Data& cur_data = s.top();
        switch(cur_data.scode){
            case 0:{
                if(cur_data.arr==nullptr){
                    s.pop();
                    break;
                }
                if(cur_data.r - cur_data.l <=2){
                    if(cur_data.r - cur_data.l<=1) s.pop();
                    else{
                        if(cur_data.arr[cur_data.l] < cur_data.arr[cur_data.l+1]) s.pop();
                        else {
                            swap(&cur_data.arr[cur_data.l],&cur_data.arr[cur_data.l+1]);
                            s.pop();
                        }
                    }
                }else cur_data.scode = 1;
            };break;
            case 1:{
                cur_data.base_number = cur_data.arr[cur_data.l];
                while(cur_data.left_index != cur_data.right_index){
                    while(cur_data.left_index<cur_data.right_index and cur_data.base_number <= cur_data.arr[cur_data.right_index]) cur_data.right_index--;
                    if(cur_data.left_index < cur_data.right_index){
                        cur_data.arr[cur_data.left_index] = cur_data.arr[cur_data.right_index];
                        cur_data.left_index++;
                    }
                
                    while(cur_data.left_index < cur_data.right_index and cur_data.base_number>= cur_data.arr[cur_data.left_index]) cur_data.left_index++;
                    if(cur_data.left_index < cur_data.right_index){
                        cur_data.arr[cur_data.right_index] = cur_data.arr[cur_data.left_index];
                        cur_data.right_index--;
                    }
                }
                cur_data.arr[cur_data.left_index] = cur_data.base_number;
                cur_data.scode = 2;
            };break;
            case 2:{
                Data new_data(arr,cur_data.l,cur_data.left_index);
                s.push(new_data);
                cur_data.scode = 3;
            };break;
            case 3:{
                Data new_data(arr,cur_data.left_index+1,cur_data.r);
                s.push(new_data);
                cur_data.scode = 4;
            };break;
            case 4:{s.pop();};break;
        }
    }
}

void test01(){

}

int main(void){
    test01();
    system("pause");
    return 0;
}
//快速排序
void quick_sort(int* arr,int l,int r){
    //scode = 0
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

    //scode = 1
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

    //scode = 2
    quick_sort(arr,l,left_index);

    //scode = 3
    quick_sort(arr,left_index+1,r);

    //scode = 4
    return;
}