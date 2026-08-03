/* 给你单链表的头指针 head 和两个整数 left 和 right ，其中 left <= right 。
请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表 。

示例 1：
输入：head = [1,2,3,4,5], left = 2, right = 4
输出：[1,4,3,2,5]

示例 2：
输入：head = [5], left = 1, right = 1
输出：[5] */
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
class Solution{
public:
    ListNode* reverse_between_recursive_function(ListNode* head,int left,int right){
        if(head == nullptr or head->next == nullptr) return head;
        int len = 0;
        for(ListNode* p = head;p;p=p->next) len++;
        if(left<=0 or right>len or left>=right) return head;
        ListNode* new_head = reverse_between_recursive_function(head,left,right-1);
        ListNode* right_index = new_head;
        ListNode* left_index = new_head;
        if(left==1){
            for(int i=0;i<right-2;i++) right_index = right_index->next;
            ListNode* temp = right_index->next->next;
            right_index->next->next = new_head;
            new_head = right_index->next;
            right_index->next = temp;
            return new_head;
        }
        for(int i=0;i<left-2;i++) left_index = left_index->next;
        for(int i=0;i<right-2;i++) right_index = right_index->next;
        ListNode* temp = right_index->next->next;
        right_index->next->next = left_index->next;
        left_index->next = right_index->next;
        right_index->next = temp;
        return new_head;
    }

    ListNode* reverseBetween(ListNode* head,int left,int right){
        if(left == 1 and right == 1) return head;
        if(left!=1){
            head->next = reverse(head->next, left-1, right-);
            return new_head;
        }else if(left==1){
            ListNode* tail = head->next;
            ListNode* new_head = reverseBetween(head->next,1,right-1);
            heat->next = tail->next;
            tail->next = head;
            return new_head;
        }
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