/* 题目描述
? 公司有 M
M
 个任务需要完成，每个任务有一个难度系数 Yi
Y
i
 并且需要一定的时间 Xi
X
i
 完成。现在有 N
N
 台机器，每台机器有最大工作时间和最大工作难度，只有当机器的最大工作时间和最大工作难度大于等于任务的时间和任务的难度时，机器才能完成这个任务。每天机器每天只能完成一个任务，一个任务只能被一台机器完成。当完成一个任务时，公司能获得 500?Xi+2?Yi
500
?
X
i
+
2
?
Y
i
 的报酬。求今天公司最多能获得的报酬。

输入
? 第一行输入两个整数 N,M
N
,
M
。

? 接下来 N
N
 行，每行两个数，表示机器的最大工作时间和最大工作难度。

? 接下来 M
M
 行，每行两个数，表示任务需要的时间和任务的难度。

输出
? 输出一行两个数，第一个数为能完成的最大任务数，第二个数为今天能获取的最高报酬。

样例输入
1 2
100 3
100 2
100 1
样例输出
1 50004
 */

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
typedef pair<long long ,long long > PII;
bool cmp(const PII& a,const PII& b){
    return (a.first*500+a.second*2) > (b.first*500+b.second*2);
}

int main(void){
    long long  N;
    long long  M;
    cin>>N>>M;
    vector<PII> machine;
    vector<PII> mission;

    for(long long  i=0;i<N;i++){
        long long  x;
        long long  y;
        cin>>x>>y;
        machine.push_back(PII(x,y));
    }
    for(long long  j=0;j<M;j++){
        long long  x;
        long long  y;
        cin>>x>>y;
        mission.push_back(PII(x,y));
    }
    sort(machine.begin(),machine.end(),cmp);
    sort(mission.begin(),mission.end(),cmp);

    long long  cnt = 0;
    long long  wage = 0;
    // level[k] 表示候选机器中，难度等级为 k 的机器数量
    vector<long long> level(101, 0);

    long long j = 0;

    for (long long i = 0; i < M; i++) {
        long long task_time = mission[i].first;
        long long task_level = mission[i].second;

        // 把所有工作时间足够的机器加入候选集合
        while (j < N and machine[j].first >= task_time) {
            level[machine[j].second]++;
            j++;
        }

        // 选择难度刚好够用的最低等级机器
        for (long long k = task_level; k <= 100; k++) {
            if (level[k] > 0) {
                level[k]--;
                cnt++;
                wage += 500LL * task_time + 2LL * task_level;
                break;
            }
        }
    }
    cout<<cnt<<" ";
    cout<<wage<<endl;
    //system("pause");
    return 0;
}