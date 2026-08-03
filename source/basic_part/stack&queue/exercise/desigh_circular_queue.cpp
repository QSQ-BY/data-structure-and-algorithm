/* 设计你的循环队列实现。 循环队列是一种线性数据结构，
其操作表现基于 FIFO（先进先出）原则并且队尾被连接在队首之后以形成一个循环。它也被称为“环形缓冲器”。

循环队列的一个好处是我们可以利用这个队列之前用过的空间。在一个普通队列里，
一旦一个队列满了，我们就不能插入下一个元素，即使在队列前面仍有空间。
但是使用循环队列，我们能使用这些空间去存储新的值。

你的实现应该支持如下操作：

MyCircularQueue(k): 构造器，设置队列长度为 k 。
Front: 从队首获取元素。如果队列为空，返回 -1 。
Rear: 获取队尾元素。如果队列为空，返回 -1 。
enQueue(value): 向循环队列插入一个元素。如果成功插入则返回真。
deQueue(): 从循环队列中删除一个元素。如果成功删除则返回真。
isEmpty(): 检查循环队列是否为空。
isFull(): 检查循环队列是否已满。

示例：
MyCircularQueue circularQueue = new MyCircularQueue(3); // 设置长度为 3
circularQueue.enQueue(1);  // 返回 true
circularQueue.enQueue(2);  // 返回 true
circularQueue.enQueue(3);  // 返回 true
circularQueue.enQueue(4);  // 返回 false，队列已满
circularQueue.Rear();  // 返回 3
circularQueue.isFull();  // 返回 true
circularQueue.deQueue();  // 返回 true
circularQueue.enQueue(4);  // 返回 true
circularQueue.Rear();  // 返回 4
 */

//循环队列的设计
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;
class MyCircularQueue {
public:
    //使用循环链表实现循环队列
    class Node{
    public:
        int data;
        Node* next;
    };
    Node* head;
    Node* tail;
    int count;
    int size;
    MyCircularQueue(int k) {
        //左闭右闭区间，tail指针初始创建时在head指针的前一位
        count = 0;
        size = k;
        head = new Node();
        Node* p =head;
        for(int i = 0;i<k-1;i++){
            p->next = new Node();
            p=p->next;
        }
        tail = p;
        tail->next = head;
    }
    
    bool enQueue(int value) {
        if(count == size) return false;
        tail->next->data = value;
        tail = tail->next;
        count++;
        return true;
    }
    
    bool deQueue() {
        if(count==0) return false;
        head = head->next;
        count--;
        return true;
    }
    
    int Front() {
        if(isEmpty()) return -1;
        else return head->data;
    }
    
    int Rear() {
        if(isEmpty()) return -1;
        else return tail->data;
    }
    
    bool isEmpty() {
        if(count == 0) return true;
        else return false;
    }
    
    bool isFull() {
        if(count == size) return true;
        else return false;
    }
};
void test01(){
    MyCircularQueue circularQueue(3);
    cout << boolalpha;
    cout << circularQueue.enQueue(1) << endl;
    cout << circularQueue.enQueue(2) << endl;
    cout << circularQueue.enQueue(3) << endl;
    cout << circularQueue.enQueue(4) << endl;
    cout << circularQueue.Rear() << endl;
    cout << circularQueue.isFull() << endl;
    cout << circularQueue.deQueue() << endl;
    cout << circularQueue.enQueue(4) << endl;
    cout << circularQueue.Rear() << endl;
}

int main(void){
    test01();
    system("pause");
    return 0;
}