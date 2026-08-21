/* 题目描述
? 约翰打算建一个围栏来圈养他的奶牛。作为最挑剔的兽类，
奶牛们要求这个围栏必须是正方形的，
而且围栏里至少要有 C (1≤C≤500) 个草场，来供应她们的午餐。
? 约翰的土地上共有 N (C≤N≤500) 个草场，
每个草场在一块1x1的方格内，而且这个方格的 坐标不会超过 10000。
有时候，会有多个草场在同一个方格内，那他们的坐标就会相同。
? 现求围栏的最小边长为多少。
输入
? 第一行输入两个数 C,N。
? 接下来 N 行每行两个数，表示每个草场的坐标 Xi,Yi。
输出
? 输出围栏的最小边长。
样例输入
3 4
1 2
2 1
4 1
5 2
样例输出
4 */
/* 
原问题：至少包含C个草场的最小正方形边长
显然正方形边长越长，包含的草场数量越多
新问题：边长为L的正方形，包含的草场的数量是否>=C
正方形边长L 0 1 2 ...... L-1 L ...... N
是否>=C     0 0 0 ...... 0   1 ...... 1   
 */
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <unordered_map>
#include <unordered_set>

using namespace std;
#define MAX_N 500
struct Point{
    int x;
    int y;
};
Point arr[MAX_N+5];

bool cmp(Point& a,Point& b){
    if(a.x!=b.x) return a.x<b.x;
    return a.y<b.y;
}

//二维扫描线法
int check_y(Point* arr,int n,int c,int begin,int end,int l){
    vector<int> temp;
    int cnt;
    for(int i=begin;i<=end;i++){
        temp.push_back(arr[i].y);
        cnt++;
    }
    sort(temp.begin(),temp.end());
    for(int i = c-1;i<cnt;i++){
        //连续c个点的y坐标差值小于l
        if(temp[i] - temp[i-c+1] < l) return 1;
    }
    return 0;
}

int check(Point* arr,int n,int c,int l){
    int j=0;
    for(int i=0;i<n;i++){
        while((arr[i].x - arr[j].x)>=l) j++;
        //此时从第j个点到第i个点都在区间范围之内
        if(i-j+1 < c) continue;
        //开始对y坐标线进行扫描
        if(check_y(arr,n,c,j,i,l)==1) return 1;
    }
    return 0;
}

int binary_search(int left,int right,Point* arr,int n,int C){
    int mid = 0;
    while(left<right){
        mid = left+(right-left)/2;
        if(check(arr,n,C,mid) == 1) right = mid;
        else left = mid+1;
    }
    return left;
}

//二维扫描线法
void test01(){
    int C=0;
    int n=0;
    cin>>C>>n;
    for(int i=0;i<n;i++){
        cin>>arr[i].x>>arr[i].y;
    }
    sort(arr,arr+n,cmp);
    cout<<binary_search(0,10000,arr,n,C)<<endl;
    return;
}

int main(void){
    test01();
    //system("pause");
    return 0;
}