/* 给你单链表的头节点 head ，
请你反转链表，并返回反转后的链表。
示例 1：
输入：head = [1,2,3,4,5]
输出：[5,4,3,2,1]
示例 2：
输入：head = [1,2]
输出：[2,1]
示例 3：
输入：head = []
输出：[]
  */
#include <iostream>
#include <vector>
#include <string>
#include <iomanip>
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
    ListNode* reverseList_head_insert(ListNode* head){
        ListNode *p = head;
        ListNode *temp = nullptr;
        ListNode *dummy = new ListNode();
        dummy->next = nullptr;
        while (p) {
            temp = p->next;
            p->next = dummy->next;
            dummy->next = p;
            p = temp;
        }
        return dummy->next;
    }

    ListNode* reverseList_triple_pointer(ListNode* head){
        ListNode* cur = head;
        ListNode* pre = nullptr;
        while(cur){
            ListNode* temp = cur ->next;
            cur-> next = pre;
            pre = cur;
            cur = temp;
        }
        return pre;
    }

    ListNode* reverseList_recursive_function(ListNode* head){
        if (head == nullptr || head->next == nullptr) {
            return head;
        }
        ListNode* tail = head->next;
        ListNode* new_head = reverseList_recursive_function(head->next);
        tail->next = head;
        head->next = nullptr;
        return new_head;
    }
};

void test01(){
    auto buildList = [](const vector<int>& values) {
        ListNode* dummy = new ListNode();
        ListNode* tail = dummy;
        for (int v : values) {
            tail->next = new ListNode(v);
            tail = tail->next;
        }
        ListNode* head = dummy->next;
        delete dummy;
        return head;
    };

    auto toVector = [](ListNode* head) {
        vector<int> out;
        while (head) {
            out.push_back(head->val);
            head = head->next;
        }
        return out;
    };

    auto freeList = [](ListNode* head) {
        while (head) {
            ListNode* next = head->next;
            delete head;
            head = next;
        }
    };

    auto vecToString = [](const vector<int>& v) {
        string s = "[";
        for (size_t i = 0; i < v.size(); ++i) {
            s += to_string(v[i]);
            if (i + 1 < v.size()) {
                s += ",";
            }
        }
        s += "]";
        return s;
    };

    auto printLine = []() {
        cout << string(86, '-') << "\n";
    };

    auto runCase = [&](const string& name,
                       const vector<int>& input,
                       const vector<int>& expected) {
        Solution s;
        string inputText = vecToString(input);
        {
            ListNode* head = buildList(input);
            ListNode* out = s.reverseList_head_insert(head);
            vector<int> got = toVector(out);
            cout << left << setw(8) << name
                 << left << setw(18) << "head_insert"
                 << left << setw(8) << (got == expected ? "PASS" : "FAIL")
                 << left << setw(18) << inputText
                 << left << setw(18) << vecToString(expected)
                 << left << setw(18) << vecToString(got) << "\n";
            freeList(out);
        }
        {
            ListNode* head = buildList(input);
            ListNode* out = s.reverseList_triple_pointer(head);
            vector<int> got = toVector(out);
            cout << left << setw(8) << name
                 << left << setw(18) << "triple_pointer"
                 << left << setw(8) << (got == expected ? "PASS" : "FAIL")
                 << left << setw(18) << inputText
                 << left << setw(18) << vecToString(expected)
                 << left << setw(18) << vecToString(got) << "\n";
            freeList(out);
        }
        {
            ListNode* head = buildList(input);
            ListNode* out = s.reverseList_recursive_function(head);
            vector<int> got = toVector(out);
            cout << left << setw(8) << name
                 << left << setw(18) << "recursive"
                 << left << setw(8) << (got == expected ? "PASS" : "FAIL")
                 << left << setw(18) << inputText
                 << left << setw(18) << vecToString(expected)
                 << left << setw(18) << vecToString(got) << "\n";
            freeList(out);
        }
    };
    printLine();
    cout << left << setw(8) << "Case"
         << left << setw(18) << "Method"
         << left << setw(8) << "Result"
         << left << setw(18) << "Input"
         << left << setw(18) << "Expected"
         << left << setw(18) << "Got" << "\n";
    printLine();
    runCase("case1", {1, 2, 3, 4, 5}, {5, 4, 3, 2, 1});
    runCase("case2", {1, 2}, {2, 1});
    runCase("case3", {}, {});
    runCase("case4", {7}, {7});
    runCase("case5", {-1, 0, -2}, {-2, 0, -1});
    printLine();
}

int main(void){
    test01();
    system("pause");
    return 0;
}