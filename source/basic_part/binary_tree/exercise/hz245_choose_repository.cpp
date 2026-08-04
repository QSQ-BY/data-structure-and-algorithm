/* ? 在一条数轴上有 N 家商店，他们的坐标分别为 A[1]?A[N]。
现在需要在数轴上建立一家货仓，每天清晨，从货仓到每家商店都要运送一车商品。
为了提高效率，求把货仓建在何处，可以使得货仓到每家商店的距离之和最小，
输出最短距离之和。
输入
? 第一行输入一个数 N。（1≤N≤100000）
? 接下来一行，输入 N 个数，表示商店的坐标。
输出
? 输出最短距离之和。
样例输入
5
1 3 5 6 10
样例输出
12 */
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(void){
    long long ans = 0;
    int N;
    cin>>N;
    vector<int> arr(N);
    for(int i =0;i<N;i++){
        cin>>arr[i];
    }
    sort(arr.begin(),arr.end());
    if(N==1){
        ans = 0;
        cout<<ans<<endl;
        return 0;
    };
    int left;
    int right;
    if(N%2 == 1){
        int pos = N/2;
        left = pos,
        right = pos;
        for(int i =0;i<N/2;i++){
            left--;
            right++;
            ans += abs(arr[left] - arr[right]);
        }
    }else if(N%2 == 0){
        left = N/2-1;
        right = (N/2);
        for(int i =0;i<N/2;i++){
            ans += abs(arr[left] - arr[right]);
            left--;
            right++;
        }
    }
    cout<<ans<<endl;
    system("pause");
    return 0;
}