/* 给你链表的头结点 head ，请将其按 升序
排列并返回 排序后的链表 。
示例 1：
输入：head = [4,2,1,3]
输出：[1,2,3,4]
示例 2：
输入：head = [-1,5,3,4,0]
输出：[-1,0,3,4,5]
示例 3：
输入：head = []
输出：[]
 */
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

//对链表进行排序
//只能从前向后进行访问->选择排序/冒泡排序/快速排序/归并排序
class Solution {
public:
//使用快速排序完成链表的排序
    ListNode* sortList1(ListNode* head) {
        //边界条件
        if(head == nullptr or head->next == nullptr) return head;

        //寻找中间基准值
        int l = head->val;
        int r = head->val;
        ListNode* p = head;
        while(p){
            l = min(p->val,l);
            r = max(p->val,r);
            p = p->next;
        }
        if(l == r) return head;
        int base_number = (l+r)>>1;

        //分区操作
        ListNode* h1 = nullptr;
        ListNode* h2 = nullptr;
        ListNode* temp = nullptr;
        p = head;
        while(p){
            temp = p->next;
            if(p->val <= base_number){
                p->next = h1;
                h1 = p;
            }else{
                p->next = h2;
                h2 = p;
            }
            p = temp;
        }

        //分别对两个区进行排序
        h1 = sortList1(h1);
        h2 = sortList1(h2);
        p = h1;
        while(p->next) p = p->next;
        p->next = h2;
        return h1;
    }

//使用归并排序完成链表排序

    ListNode* merge_sort(ListNode* head,int n){
        if(head == nullptr or n==1) return head;
        int l = n/2;
        int r = n-l;
        ListNode* h1 = nullptr;
        ListNode* h2 = nullptr;
        ListNode* p = nullptr;
        p=head;
        for(int i = 0;i<l-1;i++) p = p->next;
        h1 = head;
        h2 = p->next;
        p->next = nullptr;
        h1 = merge_sort(h1,l);
        h2 = merge_sort(h2,r);

        ListNode* ans =nullptr;
        ListNode* p1 = h1;
        ListNode* p2 = h2;

        while(p1!=nullptr or p2!=nullptr){
            if((p1!=nullptr and p2!=nullptr and p1->val < p2->val) or p2 == nullptr){
                ListNode* temp = p1->next;
                p1->next = ans;
                ans = p1;
                p1 = temp;
            }else{
                ListNode* temp = p2->next;
                p2->next = ans;
                ans = p2;
                p2 = temp;
            }
        }

        ListNode* prev = nullptr;
        while(ans!=nullptr){
            ListNode* temp = ans->next;
            ans->next = prev;
            prev = ans;
            ans = temp;
        }
        return prev;
    }
    ListNode* sortList2(ListNode* head){
        if(head == nullptr or head->next == nullptr) return head;
        //获取链表长度n
        ListNode* p = nullptr;
        p = head;
        int n = 0;
        while(p){
            n++;
            p=p->next;
        }
        return merge_sort(head,n);
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