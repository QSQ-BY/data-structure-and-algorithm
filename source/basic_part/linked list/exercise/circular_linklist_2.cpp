/* 给定一个链表的头节点 head ，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。
为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。
如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。 */
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
    ListNode *detectCycle(ListNode *head) {
        // 快慢指针先判断是否有环；相遇后从头节点和相遇点同时出发，交点就是入环节点。
        ListNode* fast = head;
        ListNode* slow = head;
        while(fast!=nullptr and fast->next!=nullptr){
            fast = fast->next->next;
            slow = slow->next;
            if(fast == slow){
                ListNode* p = head;
                while(p!=slow){
                    p = p->next;
                    slow = slow->next;
                }
                return slow;
            }
        }
        return nullptr;
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
        cout << string(92, '-') << "\n";
    };

    auto runCase = [&](const string& name,
                       const vector<int>& values,
                       int pos,
                       int expectedIndex) {
        ListNode* tail = nullptr;
        ListNode* head = buildListWithCycle(values, pos, tail);
        ListNode* got = s.detectCycle(head);

        int actualIndex = -1;
        ListNode* cur = head;
        for (int i = 0; cur && i < static_cast<int>(values.size()); ++i) {
            if (cur == got) {
                actualIndex = i;
                break;
            }
            cur = cur->next;
        }

        cout << left << setw(8) << name
             << left << setw(18) << vecToString(values)
             << left << setw(6) << pos
             << left << setw(10) << expectedIndex
             << left << setw(8) << actualIndex
             << left << setw(12) << (got ? got->val : -1)
             << left << setw(8) << (actualIndex == expectedIndex ? "PASS" : "FAIL")
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
         << left << setw(12) << "EntryVal"
         << left << setw(8) << "Result" << "\n";
    printLine();

    runCase("case1", {3, 2, 0, -4}, 1, 1);
    runCase("case2", {1, 2}, 0, 0);
    runCase("case3", {1}, -1, -1);
    runCase("case4", {}, -1, -1);
    runCase("case5", {1, 2, 3, 4, 5}, -1, -1);
    runCase("case6", {1, 2, 3, 4, 5}, 4, 4);

    printLine();
}

int main(void){
    test01();
    system("pause");
    return 0;
}
