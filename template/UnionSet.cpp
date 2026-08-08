#include <iostream>
#include <vector>
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


class WeightedUnionSet{
public:
    WeightedUnionSet(int n){
        for(int i=0;i<n;i++){
            father.push_back(i);
            size.push_back(1);
            val.push_back(0);
        }
        this->element_num = n;
        this->collection_num = n;
    }

    int find(int x){
        if(father[x] == x) return x;
        int parent = father[x];
        int root = find(parent);
        val[x] += val[parent];
        father[x] = root;
        return root;
    }

    int merge(int a,int b,long long t){
        int set_a = find(a);
        int set_b = find(b);
        if(set_a == set_b) return 0;

        long long root_difference = t - val[a] + val[b];
        if(size[set_a] < size[set_b]){
            father[set_a] = set_b;
            val[set_a] = root_difference;
            size[set_b] += size[set_a];
        }else{
            father[set_b] = set_a;
            val[set_b] = -root_difference;
            size[set_a] += size[set_b];
        }
        collection_num--;
        return 1;
    }

    int merge(const vector<int>& nums){
        int merged = 0;
        for(vector<int>::size_type i = 1;i < nums.size();i++){
            if(merge(nums[0],nums[i],0)) merged = 1;
        }
        return merged;
    }

    void insert(){
        father.push_back(element_num);
        size.push_back(1);
        val.push_back(0);
        element_num++;
        collection_num++;
    }

    int restore(int index){
        int old_root = find(index);
        if(size[old_root] == 1) return 0;

        vector<int> members;
        for(int i = 0;i < element_num;i++){
            if(i != index && find(i) == old_root){
                members.push_back(i);
            }
        }

        if(index != old_root){
            father[index] = index;
            val[index] = 0;
            size[index] = 1;
            size[old_root]--;
        }else{
            int new_root = members[0];
            long long base = val[new_root];

            for(int member:members){
                val[member] -= base;
                father[member] = new_root;
                size[member] = 1;
            }

            father[new_root] = new_root;
            val[new_root] = 0;
            size[new_root] = static_cast<int>(members.size());
            father[index] = index;
            val[index] = 0;
            size[index] = 1;
        }

        collection_num++;
        return 1;
    }

    int is_connected(int a,int b){
        return find(a) == find(b);
    }

    int all_connected(const vector<int>& nodes){
        if(nodes.empty()) return 1;
        int root = find(nodes[0]);
        for(vector<int>::size_type i = 1;i < nodes.size();i++){
            if(find(nodes[i]) != root) return 0;
        }
        return 1;
    }

    int get_size(int index){
        return size[find(index)];
    }

    int get_difference(int a,int b,long long& result){
        int set_a = find(a);
        int set_b = find(b);
        if(set_a != set_b) return 0;
        result = val[a] - val[b];
        return 1;
    }

    vector<long long> val;//val[i]表示i节点与father[i]节点的权值差
    vector<int> father;
    vector<int> size;
    int element_num;
    int collection_num;
};

int main(void){
    return 0;
}
