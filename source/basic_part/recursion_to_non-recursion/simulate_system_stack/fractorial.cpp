//使用系统栈模拟法把阶乘递归函数转为非递归
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <unordered_map>
#include <unordered_set>
#include <stack>

using namespace std;

class Data{
public:
    Data(int n,int* pre_ret){
        this->n = n;
        this->pre_ret = pre_ret;
        scode = 0;
    }
    int n;
    int ret;
    int* pre_ret;
    int scode;
};

//递归版本
int f(int n){
    if(n==0 or n==1) return 1; 
    return n*f(n-1);            
}

//非递归版本（系统栈模拟法）
int non_f(int n){
    int ans;
    Data d(n,&ans);
    stack<Data> s;
    s.push(d);
    while(!s.empty()){
        Data& cur_data = s.top();
        switch(cur_data.scode){
            case 0:{
                if(cur_data.n==1 or cur_data.n==0){
                    *(cur_data.pre_ret) = 1;
                    s.pop();
                }
                else{
                    cur_data.scode = 1;
                }
            };break;
            case 1:{
                Data new_data(cur_data.n-1,&(cur_data.ret));
                s.push(new_data);
                cur_data.scode = 2;
            };break;
            case 2:{
                *(cur_data.pre_ret) = cur_data.n*cur_data.ret;
                s.pop();
            };break;
        }
    }
    return ans;
}

void test01(){
    int n = 5;
    while(~scanf("%d",&n)){
        cout<<f(n)<<endl;
        cout<<non_f(n)<<endl;
    }
}

int main(void){
    test01();
    system("pause");
    return 0;
}