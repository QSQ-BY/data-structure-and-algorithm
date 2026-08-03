/* 中位数是有序整数列表中的中间值。如果列表的大小是偶数，
则没有中间值，中位数是两个中间值的平均值。
例如 arr = [2,3,4] 的中位数是 3 。
例如 arr = [2,3] 的中位数是 (2 + 3) / 2 = 2.5 。
实现 MedianFinder 类:
MedianFinder() 初始化 MedianFinder 对象。
void addNum(int num) 将数据流中的整数 num 添加到数据结构中。
double findMedian() 返回到目前为止所有元素的中位数。
与实际答案相差 10-5 以内的答案将被接受。
示例 1
输入
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
输出
[null, null, null, 1.5, null, 2.0]
解释
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // 返回 1.5 ((1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0
 */

#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
using namespace std;
//双堆法，对顶堆

class MedianFinder {
public:
    typedef pair<int,int> PII;
    int tot = 0;
    set<PII> s1,s2;
    //s1大顶堆 s2小顶堆

    MedianFinder() {
        
    }
    
    void addNum(int num) {
        if(s1.size() == 0 or num<-s1.begin()->first){
            s1.insert(PII(-num,tot++));
        }else{
            s2.insert(PII(num,tot++));
        }
        int n1 = (s1.size()+ s2.size()+1)/2;//理论元素数量
        if(n1 == s1.size()) return;
        if(s1.size() < n1){
            s1.insert(PII(-s2.begin()->first,tot++));
            s2.erase(s2.begin());
        }else{
            s2.insert(PII(-s1.begin()->first,tot++));
            s1.erase(s1.begin());
        }
        return;
    }
    
    double findMedian() {
        if((s1.size() + s2.size())%2 == 1){
            return -s1.begin()->first;
        }
        else{
            double a = -s1.begin()->first;
            double b = s2.begin()->first;
            return (a+b)/2.0;
        }
    }
};


class MedianFinder2{
public:
    typedef pair<int,int> PII;
    set<PII> s1;
    set<PII> s2;
    int tot = 0;
    MedianFinder2(){
        tot = 0;
    }
    void addNum(int num){
        if(s1.size() == 0 or -s1.begin()->first > num){
            s1.insert(PII(-num,tot++));
        }else{
            s2.insert(PII(num,tot++));
        }

        int n1 = (s1.size()+s2.size()+1)/2;
        if(n1==s1.size()) return;
        if(s1.size()>n1){
            //实际数量比理论数量大，就要给一个元素到s2
            PII temp = PII(-s1.begin()->first,tot++);
            s2.insert(temp);
            s1.erase(s1.begin());
        }else if(s1.size()<n1){
            //实际数量比理论数量下，s2要给一个元素到s1
            PII temp = PII(-s2.begin()->first,tot++);
            s1.insert(temp);
            s2.erase(s2.begin());
        }
        return;
    }

    double findMedian(){
        int n = s1.size()+s2.size();
        if(n%2 == 0){
            return ((-s1.begin()->first)+(s2.begin()->first))/2.0;
        }else if(n%2 == 1){
            return -s1.begin()->first;
        }
        return 0.0;
    }
};
void test01(){
}

int main(void){
    test01();
    system("pause");
    return 0;
}