/* 题目描述
在大学期间，经常需要租借教室。大到院系举办活动，小到学习小组自习讨论，都需要向学校申请借教室。教室的大小功能不同，借教室人的身份不同，借教室的手续也不一样。

面对海量租借教室的信息，我们自然希望编程解决这个问题。

我们需要处理接下来 n 天的借教室信息，其中第 i 天学校有 r
i
?
  个教室可供租借。共有 m 份订单，每份订单用三个正整数描述，分别为 d
j
?
 ,s
j
?
 ,t
j
?
 ，表示某租借者需要从第 s
j
?
  天到第 t
j
?
  天租借教室（包括第 s
j
?
  天和第 t
j
?
  天），每天需要租借 d
j
?
  个教室。

我们假定，租借者对教室的大小、地点没有要求。即对于每份订单，我们只需要每天提供 d
j
?
  个教室，而它们具体是哪些教室，每天是否是相同的教室则不用考虑。

借教室的原则是先到先得，也就是说我们要按照订单的先后顺序依次为每份订单分配教室。如果在分配的过程中遇到一份订单无法完全满足，则需要停止教室的分配，通知当前申请人修改订单。这里的无法满足指从第 s
j
?
  天到第 t
j
?
  天中有至少一天剩余的教室数量不足 d
j
?
  个。

现在我们需要知道，是否会有订单无法完全满足。如果有，需要通知哪一个申请人修改订单。

输入格式
第一行包含两个正整数 n,m，表示天数和订单的数量。

第二行包含 n 个正整数，其中第 i 个数为 r
i
?
 ，表示第 i 天可用于租借的教室数量。

接下来有 m 行，每行包含三个正整数 d
j
?
 ,s
j
?
 ,t
j
?
 ，表示租借的数量，租借开始、结束分别在第几天。

每行相邻的两个数之间均用一个空格隔开。天数与订单均用从 1 开始的整数编号。

输出格式
如果所有订单均可满足，则输出只有一行，包含一个整数 0。

否则（订单无法完全满足）输出两行，第一行输出一个负整数 ?1，第二行输出需要修改订单的申请人编号。

输入输出样例
输入 #1复制

4 3
2 5 4 3
2 1 3
3 2 4
4 2 4
输出 #1复制

-1
2 */
//利用二分模型
//前i个订单能否都满足
#include <iostream>
#include <vector>
#include <climits>
#include <algorithm>
using namespace std;

struct Data{
    long long  d,s,t;
};
long long  n;//天数
long long  m;//订单数
vector<long long > classroom(1000005);
vector<long long > diff(1000005);
vector<Data> orders(1000005);

//检查前x个订单能否被满足
long long  check(long long  x){
    diff[1] = classroom[1];
    for(long long  i=2;i<=n;i++){
        diff[i] = classroom[i] - classroom[i-1];
    }
    for(long long  i=1;i<=x;i++){
        long long  day = orders[i].d;
        long long  start = orders[i].s;
        long long  end = orders[i].t;
        diff[start] -= day;
        diff[end+1] += day;
    }
    vector<long long > cur;
    for(long long  i=1;i<=n;i++){
        if(i==1) cur.push_back(diff[1]);
        else{
            cur.push_back(cur[cur.size()-1] + diff[i]);
        }
        if(cur[i-1] < 0) return 1;
    }
    return 0;
}

int main(void){
    //数据读入
    cin>>n>>m;
    for(long long  i=1;i<=n;i++){
        scanf("%lld",&classroom[i]);
    }
    for(long long  i=1;i<=m;i++){
        scanf("%lld %lld %lld",&orders[i].d,&orders[i].s,&orders[i].t);
    }

    long long  left = 1;
    long long  right = m+1;
    while(left<right){
        long long  mid = (left + right)/2;
        if(check(mid) == 0) left = mid+1;
        else right = mid;
    }

    if(left == m+1){
        cout<<0<<endl;
    }else{
        cout<<-1<<endl;
        cout<<left<<endl;
    }
    return 0;
}