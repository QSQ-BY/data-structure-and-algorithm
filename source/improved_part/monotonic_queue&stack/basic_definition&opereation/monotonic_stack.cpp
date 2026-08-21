#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <unordered_map>
#include <unordered_set>
#include <stack>
#include <queue>
#include <deque>
#include <climits>

using namespace std;

void output(vector<int>& arr){
    int n = arr.size();
    int len = 0;
    for(int i=0;i<n;i++){
        len+=printf("%3d",i);
    }
    printf("\n");
    for(int i=0;i<n;i++){
        printf("%3d",arr[i]);
    }
    printf("\n");
    for(int i=0;i<len;i++) printf("-");
    printf("\n\n");
    return;
}

void test01(){
    int n;//??????????
    cin>>n;
    vector<int> arr;
    arr.push_back(-1);
    for(int i=0;i<n;i++){
        int a;
        cin>>a;
        arr.push_back(a);
    }
    arr.push_back(-1);
    output(arr);

    stack<int> s;
    vector<int> l(arr.size()+1);//?????????????????С?????
    vector<int> r(arr.size()+1);//?????????????????С?????

    //??????
    for(int i=0;i<arr.size();i++){
        while(!s.empty() and arr[s.top()] > arr[i]){
            r[s.top()] = i;
            s.pop();
        }
        s.push(i);
    }

    while(!s.empty()) s.pop();

    //??????
    for(int i = arr.size()-1;i>=0;i--){
        while(!s.empty() and arr[s.top()] > arr[i]){
            l[s.top()] = i;
            s.pop();
        }
        s.push(i);
    }

    //???
    for(int i=0;i<=n;i++){
        printf("arr[%d] = %d, right:arr[%d] = %d, left:arr[%d] = %d\n",
        i,arr[i],r[i],arr[r[i]],l[i],arr[l[i]]);
    }
    return;
}

int main(void){
    test01();
    system("pause");
    return 0;
}

//?????->??????????????????С??/????????????
//????????->????????????????????С/??????