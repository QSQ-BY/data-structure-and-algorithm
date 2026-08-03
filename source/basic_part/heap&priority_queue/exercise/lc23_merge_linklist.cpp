/* 给你一个链表数组，每个链表都已经按升序排列。
请你将所有链表合并到一个升序链表中，返回合并后的链表。
示例 1：
输入：lists = [[1,4,5],[1,3,4],[2,6]]
输出：[1,1,2,3,4,4,5,6]
解释：链表数组如下：
[
1->4->5,
1->3->4,
2->6
]
将它们合并到一个有序链表中得到。
1->1->2->3->4->4->5->6
示例 2：
输入：lists = []
输出：[]
示例 3：
输入：lists = [[]]
输出：[] */
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
using namespace std;
//Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution{
public:
//用小顶堆维护的是集合中的最小值
    
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        typedef pair<int,int> PII;
        set<PII> s;
        
        int n = lists.size();
        if(n==0) return nullptr;
        for(int i=0;i<n;i++){
            if(lists[i] == nullptr) continue;
            s.insert(PII(lists[i]->val,i));
        }
        ListNode new_head;
        ListNode* p = &new_head;//P指向结果链表的最后一位
        ListNode* q;
        while(s.size()){
            //把堆顶元素接到结果链表中
            PII a = *s.begin();
            s.erase(s.begin());
            q = lists[a.second];
            lists[a.second] = lists[a.second]->next;
            p->next = q;
            q->next = nullptr;
            p=q;

            //向堆中添加一个元素
            if(lists[a.second]){
                s.insert(PII(lists[a.second]->val,a.second));
            }
        }
        return new_head.next;
    }
};


class Solution2{
public:
    ListNode* mergeKLists(vector<ListNode*>& lists){
        if(lists.empty()) return nullptr;
        typedef pair<int,int> PII;
        set<PII> s;
        int n = lists.size();

        //把每个链表的第一个节点压入到堆中
        for(int i = 0;i<n;i++){
            if(lists[i] == nullptr) continue;
            s.insert(PII(lists[i]->val,i));
        }
        //虚拟头节点
        ListNode dummy_head;
        //指针p始终指向的是结果链表的最后一个节点
        ListNode *p = &dummy_head;
        while(s.size()){
            PII a = *s.begin();
            s.erase(s.begin());
            p->next = lists[a.second];
            p = p->next;
            lists[a.second] = lists[a.second] ->next;
            p->next = nullptr;
            if(lists[a.second]){
                s.insert(PII(lists[a.second]->val,a.second));
            }
        }
        
        return dummy_head.next;
    }
};
void test01(){
    Solution s;
}

int main(void){
    test01();
    system("pause");
    return 0;
}