#include <iostream>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;
typedef pair<int,int> PII;

#define MAX_N 100000
long long arr[MAX_N + 5];
int l[MAX_N+5];
int r[MAX_N+5];

void test01(){
    int n = 0;
    int m = 0;
    cin>>n;
    cin>>m;
    int k = 1;
    cin>>arr[1];
    for(int i = 1;i<n;i++){
        int number;
        scanf("%d",&number);
        if(arr[k]*number <0){
            k++;
            arr[k] = number;
        }else{
            arr[k] += number;
        }
    }

    //构建链表和小顶堆
    n = k;//压缩后的数组长度
    int cnt = 0;//正数的个数cnt
    long long sum = 0;//正数的和值sum
    set<PII> s;
    for(int i = 1;i<=n;i++){
        if(arr[i] > 0){
            cnt++;
            sum +=arr[i];
        }
        s.insert(PII(abs(arr[i]),i));
        l[i] = i-1;
        r[i] = i+1;
    }

    int st[MAX_N+5] = {0};
    while(cnt>m){
        while(st[s.begin()->second] == 1) s.erase(s.begin());
        int index = s.begin()->second;
        int left = l[index];
        int right = r[index];
        s.erase(s.begin());
        if((left > 0 and right <=n) or arr[index] > 0){
            sum -= abs(arr[index]);
            cnt--;
            if(left>0){
                arr[index] += arr[left];
                r[l[left]] = r[left];
                l[r[left]] = l[left];
                st[left] = 1;
            }
            if(right <=n){
                arr[index] += arr[right];
                r[l[right]] = r[right];
                l[r[right]] = l[right];
                st[right] = 1;
            }
            s.insert(PII(abs(arr[index]),index));
        }
    }
    cout<<sum<<endl;
}

int main(void){
    test01();
    system("pause");
    return 0;
}