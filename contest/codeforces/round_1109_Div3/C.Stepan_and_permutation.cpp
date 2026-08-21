/* Stepan found a permutation p
 of length n
. Of course, he decided to sort it. To make the process more interesting, he chose two positive integers x
 and y
 (x+y≤n)
 and defined a rule for swapping elements.

In one move, Stepan can choose two indices i
 and j
 (1≤i,j≤n)
 and swap the elements pi
 and pj
 if at least one of the following conditions holds:

|i?j|=x
|i?j|=y
Stepan wants to know whether it is possible to sort the permutation in ascending order using any number of such operations. Help him answer this question.

Input
The first line contains a single integer t
 (1≤t≤104)
 — the number of test cases.

The first line of each test case contains three integers n
, x
, and y
 (1≤x,y≤n≤2?105
, x+y≤n)
 — the length of the array and the numbers chosen by Stepan.

The second line of each test case contains n
 integers pi
 (1≤pi≤n)
 — the array p
; it is guaranteed that p
 is a permutation.

It is guaranteed that the sum of n
 over all test cases does not exceed 2?105
.

Output
For each test case, output "YES" if it is possible to sort the permutation with the given x
 and y
, and "NO" otherwise.

You may output each letter in any case (lowercase or uppercase). For example, the strings "yEs", "yes", "Yes", and "YES" will be accepted.

Example
InputCopy
4
5 2 3
5 4 3 2 1
6 2 4
2 1 4 3 6 5
4 2 2
1 2 3 4
5 2 3
1 2 3 5 4
OutputCopy
YES
NO
YES
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
#include <numeric>
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


string f(const vector<int>& arr, int x, int y){
    UnionSet u(arr.size()+1);
    int i=0;
    while(i<arr.size()){
        if(i+x<arr.size()) u.merge(arr[i],arr[i+x]);
        if(i+y<arr.size()) u.merge(arr[i],arr[i+y]);
        i++;
    }
    for(int i=0;i<arr.size();i++){
        if(u.is_connected(arr[i],i+1) == 0) return "NO";
    }
    return "YES";
}

void test01(){
    int t;
    cin>>t;
    vector<int> n;
    vector<int> x;
    vector<int> y;
    vector<vector<int>> arr(t);
    for(int i = 0;i<t;i++){
        int temp_n;
        int temp_x;
        int temp_y;
        cin>>temp_n>>temp_x>>temp_y;
        n.push_back(temp_n);
        x.push_back(temp_x);
        y.push_back(temp_y);
        for(int j=0;j<temp_n;j++){
            int number;
            cin>>number;
            arr[i].push_back(number);
        }
    }
    for(int i=0;i<t;i++){
        string ans = f(arr[i],x[i],y[i]);
        cout<<ans<<endl;
    }
}

int main(void){
    test01();
    system("pause");
    return 0;
}