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
#include <cmath>

using namespace std;
void test01(){
    int n;
    cin>>n;
    double max_result = 0;
    int ans = -1;
    for(int i = 1;i<=n;i++){
        int price;
        int s;
        cin>>price>>s;
        double result;
        result = (double)((double)s/(double)price);
        if(result > max_result) {
            max_result = result;
            ans = i;
        }
    }
    cout<<ans<<endl;
    return;
}

int main(void){
    test01();
    //system("pause");
    return 0;
}