/* 题目描述
任何一个大于 1 的自然数 n，总可以拆分成若干个小于 n 的自然数之和。
现在给你一个自然数 n，要求你求出 n 的拆分成一些数字的和。
每个拆分后的序列中的数字从小到大排序。
然后你需要输出这些序列，
其中字典序小的序列需要优先输出。
输入格式
输入：待拆分的自然数 n。
输出格式
输出：若干数的加法
输入输出样例
输入 #1复制
7
输出 #1复制
1+1+1+1+1+1+1
1+1+1+1+1+2
1+1+1+1+3
1+1+1+2+2
1+1+1+4
1+1+2+3
1+1+5
1+2+2+2
1+2+4
1+3+3
1+6
2+2+3
2+5
3+4 */
#include <iostream>
#include <vector>
using namespace std;
int n;
vector<int> arr;

void printf_one_line(vector<int>& arr){
    for(int i=0;i<arr.size();i++){
        if(i>0) printf("+");
        printf("%d",arr[i]);
    }
    printf("\n");
    return;
}

void dfs(int min,int cur_sum,int& target){
    if(cur_sum == target){
        if(arr.size()>=2) printf_one_line(arr);
        return;
    }
    for(int i=min;i<=target-cur_sum;i++){
        arr.push_back(i);
        dfs(i,cur_sum+i,target);
        arr.pop_back();
    }
    return;
}

//数字个数，可以加入的最小的数字,还剩多少没有被拆分
void dfs2(int min,int target){
    if(target == 0){
        if(arr.size()>=2) printf_one_line(arr);
        return;
    }
    if(min > target) return;
    for(int i=min;i<=target;i++){
        arr.push_back(i);
        dfs2(i,target-i);
        arr.pop_back();
    }
    return;
}



int main(void){
    cin>>n;
    //dfs2(1,n);
    dfs(1,0,n);
    //system("pause");
    return 0;
}