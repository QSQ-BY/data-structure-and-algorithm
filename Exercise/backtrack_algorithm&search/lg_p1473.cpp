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
vector<string> ans;
int N;

void print_one_line(vector<string> ans){
    for(int i=0;i<N;i++){
        cout<<i+1;
        if(i!=N-1) cout<<ans[i]; 
    }
    cout<<endl;
    return ;
}

void dfs(int cnt,int last_number,int current_result){
    if(cnt == N and current_result == 0) {
        print_one_line(ans);
        return ;
    }else if(cnt==N and current_result != 0){
        return;
    }

    ans.push_back(" ");
    int j = ans.size()-2;
    while(j>=0 and ans[j] == " ") j--;
    if(j==-1 or ans[j] == "+"){
        dfs(cnt+1,last_number*10+cnt+1,current_result-last_number + last_number*10 +cnt+1);
    }else if(ans[j] == "-"){
        dfs(cnt+1,last_number*10+cnt+1,current_result+last_number -(last_number*10+cnt+1));
    }
    ans.pop_back();
    ans.push_back("+");
    dfs(cnt+1,cnt+1,current_result+cnt+1);
    ans.pop_back();

    ans.push_back("-");
    dfs(cnt+1,cnt+1,current_result - cnt-1);
    ans.pop_back();

    return ;
}
int main(void){
    cin>>N;
    dfs(1,1,1);
    //system("pause");
    return 0;
}