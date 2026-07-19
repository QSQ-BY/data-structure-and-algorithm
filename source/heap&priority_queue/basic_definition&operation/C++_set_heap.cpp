//set模拟堆的操作
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;
void test01(){
    
    cout<<"set基础使用:"<<endl;
    set<int> s;
    cout<<s.size()<<endl;
    s.insert(3);//3
    cout<<s.size()<<endl;
    s.insert(4);//3 4
    cout<<s.size()<<endl;
    s.insert(2);//3 4 2
    cout<<s.size()<<endl;
    cout<<endl;
    return;
}


//集合的特征
void test02(){
    set<int> s;
    cout<<s.size()<<endl;
    s.insert(3);
    cout<<s.size()<<endl;
    s.insert(4);
    cout<<s.size()<<endl;
    s.insert(4);
    cout<<s.size()<<endl;
    cout<<endl;
    return;
}

void test03(){
    //消除去重特性
    typedef pair<int,int> PII;
    set<PII> s;
    int tot = 0;
    cout<<s.size()<<endl;
    s.insert(PII(3,tot++));
    cout<<s.size()<<endl;
    s.insert(PII(4,tot++));
    cout<<s.size()<<endl;
    s.insert(PII(4,tot++));
    cout<<s.size()<<endl;
    cout<<endl;
    return;
}

void test04(){
    //遍历集合中的元素
    //按照从小到大顺序输出
    typedef pair<int,int> PII;
    set<PII> s;
    int tot = 0;
    s.insert(PII(4,tot++));
    s.insert(PII(3,tot++));
    s.insert(PII(4,tot++));
    for(auto x:s){
        cout<<x.first<<" "<<x.second<<endl;
    }
    cout<<endl;
    return;
}


void test05(){
    //模拟一个小顶堆
    //模拟大顶堆，就给每个元素取反
    typedef pair<int,int> PII;
    set<PII> s;
    int tot=0;
    for(int i =0;i<10;i++){
        s.insert(PII(rand()%20,tot++));//堆的push操作
    }
    for(int i =0;i<4;i++){
        cout<<s.begin()->first<<endl;//查看堆顶元素
        s.erase(s.begin());//pop
    }
    cout<<endl;
    return;
}

int main(void){
    test01();
    test02();
    test03();
    test04();
    test05();
    system("pause");
    return 0;
}