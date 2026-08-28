/* 将两个升序链表合并为一个新的 升序 链表并返回。
新链表是通过拼接给定的两个链表的所有节点组成的。
示例 1：
输入：l1 = [1,2,4], l2 = [1,3,4]
输出：[1,1,2,3,4,4]
示例 2：
输入：l1 = [], l2 = []
输出：[]
示例 3：
输入：l1 = [], l2 = [0]
输出：[0] */


#include <iostream>
#include <vector>
#include <algorithm>
#include <set>

//Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

using namespace std;
class Solution{
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode* ans = nullptr;
        ListNode* p1 = list1;
        ListNode* p2 = list2;
        while(p1!=nullptr or p2!=nullptr){
            if((p1!=nullptr and p2!=nullptr and p1->val <p2->val) or p2 == nullptr){
                ListNode* temp = p1->next;
                p1->next = ans;
                ans = p1;
                p1 = temp;
            } else {
                ListNode* temp = p2->next;
                p2->next = ans;
                ans = p2;
                p2 = temp;
            }
        }
        ListNode* prev = nullptr;
        while(ans){
            ListNode* temp = ans->next;
            ans->next = prev;
            prev = ans;
            ans = temp;
        }
        return prev;
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