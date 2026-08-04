/* 设计一个找到数据流中第 k 大元素的类（class）。
注意是排序后的第 k 大元素，不是第 k 个不同的元素。
请实现 KthLargest 类：
KthLargest(int k, int[] nums) 使用整数 k 和整数流 nums 初始化对象。
int add(int val) 将 val 插入数据流 nums 后，返回当前数据流中第 k 大的元素。
示例 1：
输入：
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
输出：[null, 4, 5, 5, 8, 8]
解释：
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3); // 返回 4
kthLargest.add(5); // 返回 5
kthLargest.add(10); // 返回 5
kthLargest.add(9); // 返回 8
kthLargest.add(4); // 返回 8
示例 2：
输入：
["KthLargest", "add", "add", "add", "add"]
[[4, [7, 7, 7, 7, 8, 3]], [2], [10], [9], [9]]
输出：[null, 7, 7, 7, 8]
解释：
KthLargest kthLargest = new KthLargest(4, [7, 7, 7, 7, 8, 3]);
kthLargest.add(2); // 返回 7
kthLargest.add(10); // 返回 7
kthLargest.add(9); // 返回 7
kthLargest.add(9); // 返回 8
 */

#include <iostream>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;
class KthLargest {
public:
    typedef pair<int,int> PII;
    int tot = 0;
    set<PII> s;
    int k = 0;
    KthLargest(int k, vector<int>& nums) {
        this->k = k;
        for(auto x:nums){
            add(x);
        }
        return ;
    }
    
    int add(int val) {
        if(s.size()<k){
            s.insert(PII(val,tot++));
        }else{
            if(s.begin()->first < val){
                s.insert(PII(val,tot++));
            }
        }
        if(s.size()>k){
            s.erase(s.begin());
        }
        return s.begin()->first;
    } 
};


class KthLargest2{
public:
    typedef pair<int,int> PII;
    set<PII> s;
    int tot = 0;
    int k =0;
    KthLargest2(int k,vector<int>& nums){
        this->k = k;
        for(auto x:nums){
            add(x);
        }
        return;
    }

    int add(int val){
        if(s.size()<k){
            s.insert(PII(val,tot++));
        }else{
            if(s.begin()->first<val){
                s.insert(PII(val,tot++));
            }
        }
        if(s.size()>k){
            s.erase(s.begin());
        }
        return s.begin()->first;
    }
};

void test01(){

}

int main(void){
    test01();
    system("pause");
    return 0;
}