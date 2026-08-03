/* 给你一个链表的头节点 head ，旋转链表，将链表每个节点向右移动 k 个位置。
示例
输入：head = [1,2,3,4,5], k = 2
输出：[4,5,1,2,3] */
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution{
public:
    ListNode* rotateRight_recursive_function(ListNode* head,int k){
        if(head == nullptr or head->next == nullptr) return head;
        ListNode* new_head = head->next;
        int len = 0;
        for(ListNode* p =head;p;p=p->next){
            len ++;
        }
        k = k%len;
        if(k<=0) return head;
        for(ListNode* p =head;p;p=p->next){
            if(p->next->next == nullptr){
                p->next->next = head;
                new_head = p->next;
                p->next = nullptr;
            }
        }
        return rotateRight(new_head,k-1);
    }

    ListNode* rotateRight(ListNode* head,int k){
        //使用等距离k的双指针同时向后移动，当后面的指针指向空的时候，前指针就是在倒数地K个位置
        if(head==nullptr or head->next==nullptr) return head;
        int len = 0;
        for(ListNode* p = head;p;p=p->next){
            len++;
        }
        k=k%len;
        if(k == 0) return head;
        ListNode* pre_index = head;
        ListNode* latter_index = head;
        for(int i = 0;i<k+1;i++) pre_index = pre_index->next;
        while(pre_index){
            pre_index = pre_index->next;
            latter_index = latter_index->next;
            //前后指针同时向后移动
        }
        
        //移动过后，后指针指向即将要分割的位置
        ListNode* new_head = latter_index->next;
        latter_index->next = nullptr;
        pre_index = new_head;
        while(pre_index->next !=nullptr) pre_index = pre_index->next;
        pre_index->next = head;
        return new_head;
    }
};


ListNode* buildList(const vector<int>& values){
    ListNode dummy;
    ListNode* tail = &dummy;
    for(int v : values){
        tail->next = new ListNode(v);
        tail = tail->next;
    }
    return dummy.next;
}

void printList(ListNode* head){
    cout << "[";
    for(ListNode* p = head; p; p = p->next){
        cout << p->val;
        if(p->next) cout << ", ";
    }
    cout << "]";
}

void freeList(ListNode* head){
    while(head){
        ListNode* next = head->next;
        delete head;
        head = next;
    }
}
void test01(){
    Solution s;
    vector<int> values = {1, 2, 3, 4, 5};
    int k = 2;
    ListNode* head = buildList(values);

    cout << "Original : ";
    printList(head);
    cout << "\n";
    cout << "k        : " << k << "\n";

    ListNode* rotated = s.rotateRight(head, k);
    cout << "Rotated  : ";
    printList(rotated);
    cout << "\n";

    freeList(rotated);
}

int main(void){
    test01();
    system("pause");
    return 0;
}