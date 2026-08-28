/* 给定一个未排序的整数数组 nums ，
找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
请你设计并实现时间复杂度为 O(n) 的算法解决此问题。
示例 1：
输入：nums = [100,4,200,1,3,2]
输出：4
解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。
示例 2：
输入：nums = [0,3,7,2,5,8,4,6,0,1]
输出：9
示例 3：
输入：nums = [1,0,1,2]
输出：3
 */
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
class Solution1{
public:
    int longestConsecutive1(vector<int>& nums) {
        if(nums.size() == 0) return 0;
        else if(nums.size()==1) return 1;
        set<int> s;
        for(auto x:nums) s.insert(x);
        int ans = 0;
        int temp_ans = 0;
        vector<int> arr;
        arr.push_back(*s.begin());
        s.erase(s.begin());
        while(!s.empty()){
            int temp = *s.begin();
            if(temp == arr[arr.size()-1]+1){
                temp_ans++;
                ans = max(ans,temp_ans);
            }else temp_ans = 0;
            arr.push_back(*s.begin());
            s.erase(s.begin());
        }
        return ans+1;
    }
};


class UnionSet{
public:
    UnionSet(int n){
        for(int i=0;i<=n;i++){
            father.push_back(i);
            size.push_back(1);
        }
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

        return 1;
    }

    int is_connected(int a,int b){
        if(find(a) == find(b)) return 1;
        else if(find(a) != find(b)) return 0;
    }

    int all_connected(const vector<int>& nodes) {
        if (nodes.empty()) return 1;
        int root = find(nodes[0]);
        for (int i = 1; i < nodes.size(); i++) {
            if (find(nodes[i]) != root) {
                return 0;
            }
        }
        return 1;
    }

    vector<int> father;
    vector<int> size;
};

class Solution{
public:
    int longestConsecutive(vector<int>& nums){
        if(nums.size()==0) return 0;
        else if(nums.size()==1) return 1;

        int n = nums.size();
        unordered_map<int,int> h;
        UnionSet u(n);
        int index = 0;
        for(int i=0;i<n;i++){
            int x = nums[i];
            //如果在哈希表中找到了当前数字，说明重复出现了
            if(h.find(x) != h.end()) continue;

            //没有在哈希表中找到当前数字，把当前数字加入到哈希表
            h[x] = index;
            index++;
            if(h.find(x+1) != h.end()){
                u.merge(h[x],h[x+1]);
            }//在哈希表中找到了x+1
            if(h.find(x-1) != h.end()){
                u.merge(h[x],h[x-1]);
            }//在哈希表中找到了x-1
        }
        int ans = 0;
        for(int i=0;i<n;i++){
            ans = max(ans,u.size[u.find(i)]);
        }
        return ans;
    }
};
void test01(){

}

int main(void){
    test01();
    system("pause");
    return 0;
}