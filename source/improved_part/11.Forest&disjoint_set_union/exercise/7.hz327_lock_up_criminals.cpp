/* 题目描述
? S 城现有两座监狱，一共关押着N 名罪犯，编号分别为1~N。
他们之间的关系自然也极不和谐。很多罪犯之间甚至积怨已久，
如果客观条件具备则随时可能爆发冲突。
我们用“怨气值”（一个正整数值）来表示某两名罪犯之间的仇恨程度，
怨气值越大，则这两名罪犯之间的积怨越多。
如果两名怨气值为c 的罪犯被关押在同一监狱，
他们俩之间会发生摩擦，并造成影响力为c 的冲突事件。
?每年年末，警察局会将本年内监狱中的所有冲突事件按影响力从大到小排成一个列表，
然后上报到S 城Z 市长那里。
公务繁忙的Z 市长只会去看列表中的第一个事件的影响力，
如果影响很坏，他就会考虑撤换警察局长。
? 在详细考察了N 名罪犯间的矛盾关系后，
警察局长觉得压力巨大。他准备将罪犯们在两座监狱内重新分配，
以求产生的冲突事件影响力都较小，从而保住自己的乌纱帽。
假设只要处于同一监狱内的某两个罪犯间有仇恨，
那么他们一定会在每年的某个时候发生摩擦。
那么，应如何分配罪犯，
才能使Z 市长看到的那个冲突事件的影响力最小？
这个最小值是多少？
输入
? 第一行为两个正整数N(N≤20000) 和M(M≤100000)，
分别表示罪犯的数目以及存在仇恨的罪犯对数。
? 接下来的M 行每行为三个正整数aj，bj，cj，
表示aj 号和bj 号罪犯之间存在仇恨，
其怨气值为cj。数据保证1≤aj<bj<N,0<cj≤1,000,000,000
且每对罪犯组合只出现一次。
输出
输出共1行，为Z 市长看到的那个冲突事件的影响力。
如果本年内监狱中未发生任何冲突事件，请输出0。
输入样例1
4 6
1 4 2534
2 3 3512
1 2 28351
1 3 6618
2 4 1805
3 4 12884
输出样例1
3512 */
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <unordered_map>
#include <unordered_set>
#include <stack>
#include <queue>

using namespace std;

class UnionSet{
public:
    UnionSet(int n){
        for(int i=0;i<n;i++){
            father.push_back(i);
            val.push_back(0);
        }
    }

    int find(int x){
        if(father[x] == x) return x;
        int root = find(father[x]);
        val[x] += val[father[x]];
        father[x] = root;
        return root;
    }

    void merge(int a,int b,int t){
        int set_a = find(a);
        int set_b = find(b);
        if(set_a == set_b) return;
        val[set_a] = t + val[b] - val[a];
        father[set_a] = set_b;
        return;
    }
    vector<int> father;
    vector<int> val;
};

struct Data{
    int a;//囚犯
    int b;//囚犯
    int c;//冲突值
};

void test01(){
    int n;//n个罪犯
    int m;//m个关系
    int ans = 0;
    scanf("%d %d",&n,&m);
    UnionSet u(n);
    vector<Data> arr(m);
    for(int i=0;i<m;i++){
        scanf("%d%d%d",&arr[i].a,&arr[i].b,&arr[i].c);
    }

    sort(arr.begin(),arr.end(),[&](Data& i,Data& j)->bool{
        return i.c > j.c;
    });

    for(int i=0;i<m;i++){
        int a = arr[i].a;
        int b = arr[i].b;
        int anger = arr[i].c;
        //1/0表示两个人在相同/不同的监狱 加权并查集
        if(u.find(a) == u.find(b)){
            if((u.val[a]%2 + u.val[b]%2 + 2)%2 == 0){
                ans = anger;
                break;
            }
        }else{
            u.merge(a,b,1);
        }
    }
    printf("%d\n",ans);
    return;
}

int main(void){
    test01();
    system("pause");
    return 0;
}