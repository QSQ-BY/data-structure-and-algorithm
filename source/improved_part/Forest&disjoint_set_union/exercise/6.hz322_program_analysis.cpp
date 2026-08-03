/* 题目描述
? 在实现程序自动分析的过程中,常常需要判定一些约束条件是否能被同时满足。
? 考虑一个约束满足问题的简化版本：假设 x1,x2,x3,… 代表程序中出现的变量，
给定n个形如xi=xj或xi≠xj 的变量相等/不等的约束条件，
请判定是否可以分别为每一个变量赋予恰当的值，使得上述所有约束条件同时被满足。
? 例如，一个问题中的约束条件为：x1=x2，x2=x3，x3=x4，x1≠x4，
这些约束条件显然是不可能同时被满足的，
因此这个问题应判定为不可被满足。
? 现在给出一些约束满足问题，请分别对它们进行判定。
输入
? 输入文件的第1行包含1个正整数t，表示需要判定的问题个数。
注意这些问题之间是相互独立的。
? 对于每个问题，包含若干行：
? 第1行包含1个正整数n，表示该问题中需要被满足的约束条件个数。
? 接下来n行，每行包括3个整数i,j,e，描述1个相等/不等的约束条件，
相邻整数之间用单个空格隔开。
若e=1，则该约束条件为xi=xj；若e=0，则该约束条件为xi≠xj。
输出
? 输出文件包括t行。
? 输出文件的第1行输出一个字符串“YES”或者“NO”
（不包含引号，字母全部大写），
“YES”表示当前问题判定为可以被满足，“NO”表示不可被满足。
输入样例1
2
2
1 2 1
1 2 0
2
1 2 1
2 1 1
输出样例1
NO
YES */
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <unordered_map>
#include <unordered_set>
#include <stack>
#include <queue>
#include <climits>

using namespace std;

class UnionSet{
public:
    UnionSet(int n){
        for(int i=0;i<n;i++){
            father.push_back(i);
            size.push_back(1);
        }
        this->element_num = n;
        this->collection_num = n;
    }

    int find(int x){
        if(father[x] == x) return x;
        return father[x] = find(father[x]);
    }

    int merge(int a,int b){
        int set_a = find(a);
        int set_b = find(b);
        if(set_a == set_b) return 0;
        if(size[set_a] < size[set_b]){
            father[set_a] = set_b;
            size[set_b] += size[set_a];
        }else{
            father[set_b] = set_a;
            size[set_a] += size[set_b];
        }
        collection_num--;
        return 1;
    }

    int merge(const vector<int>& nums){
        int merged = 0;
        for(vector<int>::size_type i = 1;i < nums.size();i++){
            if(merge(nums[0],nums[i])) merged = 1;
        }
        return merged;
    }

    void insert(){
        father.push_back(element_num);
        size.push_back(1);
        element_num++;
        collection_num++;
    }

    int restore(int index){
        int root = find(index);
        if(size[root] == 1) return 0;

        vector<int> members;
        for(int i = 0;i < element_num;i++){
            if(i != index && find(i) == root){
                members.push_back(i);
            }
        }

        int new_root = members[0];
        for(int member:members){
            father[member] = new_root;
            size[member] = 1;
        }
        size[new_root] = static_cast<int>(members.size());
        father[index] = index;
        size[index] = 1;
        collection_num++;
        return 1;
    }

    int is_connected(int a,int b){
        return find(a) == find(b);
    }

    int all_connected(const vector<int>& nodes) {
        if (nodes.empty()) return 1;
        int root = find(nodes[0]);
        for (vector<int>::size_type i = 1; i < nodes.size(); i++) {
            if (find(nodes[i]) != root) {
                return 0;
            }
        }
        return 1;
    }

    int get_size(int index){
        return size[find(index)];
    }

    vector<int> father;//father[i]表示i的父亲节点
    vector<int> size;
    int element_num;
    int collection_num;
};

string f(vector<int>& a,vector<int>& b,vector<int>& e){
    unordered_map<int,int> id;
    id.max_load_factor(0.7f);
    id.reserve(a.size() * 2);
    int index = 0;
    for(int i = 0; i < a.size(); i++){
        if(id.find(a[i]) == id.end()){
            id[a[i]] = index;
            index++;
        }

        if(id.find(b[i]) == id.end()){
            id[b[i]] = index;
            index++;
        }
    }
    //若e=1，则该约束条件为xi=xj；若e=0，则该约束条件为xi≠xj
    UnionSet u(index);
    for(int i=0;i<a.size();i++){
        if(e[i] == 1) u.merge(id.at(a[i]),id.at(b[i]));
    }
    for(int i=0;i<a.size();i++){
        if(e[i] == 0){
            if(u.is_connected(id.at(a[i]),id.at(b[i])) == 1) return "NO";
        }
    }
    return "YES";
}

void test01(){
    int t;
    cin>>t;
    for(int i=0;i<t;i++){
        int n;
        cin>>n;
        vector<int> a(n);
        vector<int> b(n);
        vector<int> e(n);
        for(int j=0;j<n;j++){
            cin>>a[j];
            cin>>b[j];
            cin>>e[j];
        }
        cout<<f(a,b,e)<<"\n";
    }
    return;
}

int main(void){
    test01();
    //system("pause");
    return 0;
}