/* 给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

示例 1：
输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]

示例 2：
输入：head = [1], n = 1
输出：[]

示例 3：
输入：head = [1,2], n = 1
输出：[1] */

#include <iostream>
#include <iomanip>
#include <sstream>
#include <vector>
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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        if(head==nullptr) return head;
        ListNode* pre_index = head->next;
        ListNode* latter_index = head;
        int len = 0;
        for(ListNode* p=head;p;p=p->next) len++;
        if(n<=0 or n>len) return head;
        if(n==len){
            ListNode* temp = head->next;
            delete head;
            head = nullptr;
            ListNode* new_head = temp;
            return new_head;
        }
        for(int i = 0;i<len-n-1;i++){
            pre_index = pre_index->next;
            latter_index = latter_index->next;
        }
        ListNode* temp = pre_index->next;
        delete pre_index;
        pre_index = nullptr;
        latter_index->next = temp;
        
        return head;
    }

    ListNode* removeNthFromEnd_dummy_head(ListNode* head,int n){
        if(n <= 0) return head;
        ListNode dummy_head(0);
        dummy_head.next = head;
        ListNode* fast = &dummy_head;
        ListNode* slow = &dummy_head;
        for(int i = 0; i < n + 1; ++i){
            if(!fast) return head;
            fast = fast->next;
        }
        while(fast){
            fast = fast->next;
            slow = slow->next;
        }
        ListNode* target = slow->next;
        if(!target) return head;
        slow->next = target->next;
        delete target;
        return dummy_head.next;
    }
};

static ListNode* buildList(const vector<int>& vals){
    ListNode dummy(0);
    ListNode* tail = &dummy;
    for(int v : vals){
        tail->next = new ListNode(v);
        tail = tail->next;
    }
    return dummy.next;
}

static string listToString(ListNode* head){
    ostringstream oss;
    oss << "[";
    for(ListNode* p = head; p; p = p->next){
        oss << p->val;
        if(p->next) oss << ",";
    }
    oss << "]";
    return oss.str();
}

static string valsToString(const vector<int>& vals){
    ostringstream oss;
    oss << "[";
    for(size_t i = 0; i < vals.size(); ++i){
        oss << vals[i];
        if(i + 1 < vals.size()) oss << ",";
    }
    oss << "]";
    return oss.str();
}

static void freeList(ListNode* head){
    while(head){
        ListNode* next = head->next;
        delete head;
        head = next;
    }
}

void test01(){
    Solution s;
    struct Case {
        vector<int> vals;
        int n;
    };
    vector<Case> cases = {
        {{1,2,3,4,5}, 2},
        {{1}, 1},
        {{1,2}, 1},
        {{1,2}, 2}
    };

    vector<string> inputs;
    vector<string> outputs;
    size_t inputWidth = 5;
    size_t outputWidth = 6;
    size_t nWidth = 1;

    for(const auto& c : cases){
        inputs.push_back(valsToString(c.vals));
        inputWidth = max(inputWidth, inputs.back().size());

        ListNode* head = buildList(c.vals);
        ListNode* out = s.removeNthFromEnd(head, c.n);
        outputs.push_back(listToString(out));
        outputWidth = max(outputWidth, outputs.back().size());

        nWidth = max(nWidth, to_string(c.n).size());
        freeList(out);
    }

    const size_t caseWidth = 4;
    ostringstream header;
    header << left << setw(caseWidth) << "Case" << " | "
           << left << setw(inputWidth) << "input" << " | "
           << right << setw(nWidth) << "n" << " | "
           << left << setw(outputWidth) << "output";

    string headerStr = header.str();
    cout << headerStr << "\n";
    cout << string(headerStr.size(), '-') << "\n";

    for(size_t i = 0; i < cases.size(); ++i){
        cout << left << setw(caseWidth) << (i + 1) << " | "
             << left << setw(inputWidth) << inputs[i] << " | "
             << right << setw(nWidth) << cases[i].n << " | "
             << left << setw(outputWidth) << outputs[i] << "\n";
    }
}

int main(void){
    test01();
    system("pause");
    return 0;
}