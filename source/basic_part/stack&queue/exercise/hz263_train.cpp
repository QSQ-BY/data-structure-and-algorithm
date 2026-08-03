/* 题目描述
? 有 n 列火车按 1 到 n 的顺序从东方左转进站，这个车站是南北方向的，它虽然无限长，
只可惜是一个死胡同，而且站台只有一条股道，火车只能倒着从西方出去，
而且每列火车必须进站，先进后出。
? 进站的火车编号顺序为 1?n，现在请你按火车编号从小到大的顺序，
输出前 20 种可能的出站方案。
输入
? 输入一行一个整数 n。（n≤20）
输出
? 输出前 20 种答案，每行一种，不要空格。
样例输入1
3
样例输出1
123
132
213
231
321
样例输入2
4
样例输出2
1234
1243
1324
1342
1432
2134
2143
2314
2341
2431
3214
3241
3421
4321 */

#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;
class Solution{
public:
    //判断一个数字的全排列是否是合法的出站序列
    bool is_true(vector<int> arr){ 
        vector<int> stack;
        int next_train = 1;
        int n = arr.size();

        for(int i = 0; i < n; i++){
            while(next_train <= n && (stack.empty() || stack.back() < arr[i])){
                stack.push_back(next_train);
                next_train++;
            }

            if(!stack.empty() && stack.back() == arr[i]){
                stack.pop_back();
            }else{
                return false;
            }
        }
        return true;
    }


    vector<int> arr;
    vector<int> flag;
    int count = 0;

    void print_oneline(vector<int> arr){
        for(size_t i=0;i<arr.size();i++){
            if(arr[i]){
                cout<<arr[i];
            }
        }
        cout<<endl;
        return;
    }

    void permutation(int pos , int min , int max , int len){
        if(pos == 0){
            arr.assign(len, 0);
            flag.assign(max + 1, 0);
            count = 0;
        }

        if(count >= 20) return;

        if(pos == len){
            if(is_true(arr)){
                print_oneline(arr);
                count++;
            }
            return;
        }

        for(int num=min;num<=max;num++){
            if(flag[num] == 1) continue;
            else{
                arr[pos] = num;
                flag[num] = 1;
                permutation(pos+1,min,max,len);
                flag[num] = 0;
            }
        }
        return;
    }

};
void test01(){
    Solution s;
    int n{};
    cin >> n;
    s.permutation(0, 1, n, n);
}

int main(void){
    test01();
    system("pause");
    return 0;
}