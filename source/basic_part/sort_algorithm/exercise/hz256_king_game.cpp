/* 题目描述
? 恰逢 H 国国庆,国王邀请 n 位大臣来玩一个有奖游戏。
首先,他让每个大臣在左、右手上面分别写下一个整数，
国王自己也在左、右手上各写一个整数。
然后，让这 n 位大臣排成一排，国王站在队伍的最前面。
排好队后，所有的大臣都会获得国王奖赏的若干金币，
每位大臣获得的金币数分别是：
排在该大臣前面的所有人的左手上的数的乘积除以他自己右手上的数,
然后向下取整得到的结果。
? 国王不希望某一个大臣获得特别多的奖赏，
所以他想请你帮他重新安排一下队伍的顺序，
使得获得奖赏最多的大臣，所获奖赏尽可能的少。
注意，国王的位置始终在队伍的最前面。
输入
? 第一行包含一个整数 n，表示大臣的人数。
? 第二行包含两个整数 a 和 b，
之间用一个空格隔开,分别表示国王左手和右手上的整数。（均小于 10000）
? 接下来 n 行，每行包含两个整数 a 和 b，
之间用一个空格隔开，分别表示每个大臣左手和右手上的整数。（均小于 10000）
输出
? 输出一个整数，表示重新排列后的队伍中获奖赏最多的大臣所获得的金币数。
样例输入
3
1 1
2 3
7 4
4 6
样例输出
2 */
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;

class BigInt : public vector<int> {
public:
    void process_digit(){
        for(size_t i = 0;i<size();i++){
            if(at(i) < 10) continue;
            if(i+1 == size()) this->push_back(0);
            at(i+1) += at(i)/10;
            at(i) %= 10;
        }
        while(size()>1 and at(size()-1) == 0) this->pop_back();
    }

    BigInt &operator *= (int x){
        for(size_t i=0;i<size();i++) at(i) *= x;
        process_digit();
        return *this;
    }

    bool operator > (const BigInt &a) const {
        if(size() != a.size()) return size()>a.size();
        for(size_t i = size();i-- > 0;){
            if(at(i) != a[i]) return at(i) > a[i];
        }
        return false;
    }

    BigInt operator / (int x) const {
        BigInt ret(*this);
        int y = 0;
        for(size_t i=size();i-- > 0;){
            y=y*10 + at(i);
            ret[i] = y/x;
            y %= x;
        }
        ret.process_digit();
        return ret;
    }
    BigInt(int x){
        this->push_back(x);
        process_digit();
        return;
    }
};

ostream &operator << (ostream &out , const BigInt &a){
    for(size_t i = a.size();i-- > 0;){
        out<<a[i];
    }
    return out;
}

void test01(){
    int n = 0;
    cin>>n;
    vector<int> left(n+1);
    vector<int> right(n+1);
    vector<int> index(n+1);//对下标数组排序
    for(int i=0;i<n+1;i++){
        cin>>left[i]>>right[i];
        index[i] = i;
    }
    sort(index.begin()+1,index.end(),[&](int i,int j)->bool{
        return left[i]*right[i] < left[j]*right[j];
    });

    int p = left[0];
    int ans = 0;
    for(int i = 1;i<n+1;i++){
        if(p / right[index[i]] > ans) ans = p/right[index[i]];
        p *= left[index[i]];
    }
    cout<<ans;
    return;
}

//大整数实现
void test02(){
    int n = 0;
    cin>>n;
    vector<int> left(n+1);
    vector<int> right(n+1);
    //对下标进行排序
    vector<int> index(n+1);
    for(int i=0;i<n+1;i++){
        cin>>left[i]>>right[i];
        index[i] = i;
    }
    sort(index.begin()+1,index.end(),[&](int i,int j)->bool{
        return left[i]*right[i] < left[j]*right[j];
    });

    BigInt p = left[0];
    BigInt ans = 0;
    BigInt temp = 0;
    for(int i = 1;i<n+1;i++){
        temp = p/right[index[i]];
        if(temp > ans) ans = temp;
        p *= left[index[i]];
    }
    cout<<ans;
    return;
}
int main(void){
    test02();
    return 0;
}