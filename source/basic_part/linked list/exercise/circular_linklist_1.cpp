/* 给你一个链表的头节点 head ，判断链表中是否有环。
如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 
为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。
注意：pos 不作为参数进行传递 。仅仅是为了标识链表的实际情况。
如果链表中存在环 ，则返回 true 。 否则，返回 false 。 */

#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip>
#include <string>
using namespace std;
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};
class Solution{
public:
    bool hasCycle(ListNode* head){
        //快慢指针法
        //如果链表中没有环那么快指针永远无法遇到慢指针，如果有环则二者一定会相遇
        ListNode* fast = head;
        ListNode* slow = head;
        while(fast!=nullptr and fast->next!=nullptr){
            slow = slow->next;
            fast = fast->next->next;
            if(fast == slow) return true;
        }
        return false;
    }
};
void test01(){
    Solution s;

    auto buildListWithCycle = [](const vector<int>& values, int pos,
                                 ListNode*& tail) {
        ListNode* head = nullptr;
        ListNode* cur = nullptr;
        vector<ListNode*> nodes;
        for (int v : values) {
            ListNode* node = new ListNode(v);
            nodes.push_back(node);
            if (!head) {
                head = node;
            } else {
                cur->next = node;
            }
            cur = node;
        }
        tail = cur;
        if (pos >= 0 && pos < static_cast<int>(nodes.size()) && tail) {
            tail->next = nodes[pos];
        }
        return head;
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
        cout << string(78, '-') << "\n";
    };

    auto runCase = [&](const string& name,
                       const vector<int>& values,
                       int pos,
                       bool expected) {
        ListNode* tail = nullptr;
        ListNode* head = buildListWithCycle(values, pos, tail);
        bool got = s.hasCycle(head);
        cout << left << setw(8) << name
             << left << setw(18) << vecToString(values)
             << left << setw(6) << pos
             << left << setw(10) << (expected ? "true" : "false")
             << left << setw(8) << (got ? "true" : "false")
             << left << setw(8) << (got == expected ? "PASS" : "FAIL")
             << "\n";

        if (tail) {
            tail->next = nullptr;
        }
        freeList(head);
    };

    printLine();
    cout << left << setw(8) << "Case"
         << left << setw(18) << "List"
         << left << setw(6) << "Pos"
         << left << setw(10) << "Expected"
         << left << setw(8) << "Got"
         << left << setw(8) << "Result" << "\n";
    printLine();

    runCase("case1", {3, 2, 0, -4}, 1, true);
    runCase("case2", {1, 2}, 0, true);
    runCase("case3", {1}, -1, false);
    runCase("case4", {}, -1, false);
    runCase("case5", {1, 2, 3, 4, 5}, -1, false);

    printLine();
}

int main(void){
    test01();
    system("pause");
    return 0;
}
