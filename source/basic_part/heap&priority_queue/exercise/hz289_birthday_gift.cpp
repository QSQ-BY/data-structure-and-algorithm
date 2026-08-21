/* 题目描述
? 李华 18 岁生日的时候，
小明给她看了一个神奇的序列 A1,A2,...,AN。 
她被允许选择不超过 M 个连续的部分作为自己的生日礼物。
自然地，李华想要知道选择元素之和的最大值。你能帮助她吗？
输入
? 第一行，两个整数 N(1≤N≤105) 和 M(0≤M≤105)，
序列的长度和可以选择的部分。
? 第二行， N 个整数 A1,A2,...,AN(0≤|Ai|≤104)，序列。
输出
? 输出一个整数，表示最大的和。
样例输入
5 2
2 -3 2 -1 2
样例输出
5 */
//序列中有五个元素最多可以选择两个连续的部分，选择2和2 -1 2得到的和为5

#include <iostream>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;
typedef pair<int,int> PII;


void test01(){
    int n = 0;
    int m = 0;
    cin>>n;//数组大小为5
    cin>>m;//可以选择两个连续的部分
    vector<int> __arr(n);
    for(int i =0 ;i<n;i++){
        cin>>__arr[i];
    }

    if(m<=0){
        int ans = 0;
        cout<<ans;
        return;
    }

    //把连续的正数和负数进行合并,得到的序列等价
    vector<int> arr;
    for(int i=0;i<n;i++){
        int number = 0;
        if(__arr[i]>=0){
            while(i<n and __arr[i]>=0){
                number+=__arr[i];
                i++;
            }
            arr.push_back(number);
            number = 0;
            i--;
        }else if(__arr[i] < 0){
            while(i<n and __arr[i]<0){
                number+=__arr[i];
                i++;
            }
            arr.push_back(number);
            number = 0;
            i--;
        }
    }
    vector<int> clean;
    for(int x : arr){
        if(x == 0) continue;
        if(!clean.empty() && ((clean.back() > 0) == (x > 0))){
            clean.back() += x;
        }else{
            clean.push_back(x);
        }
    }
    arr = clean;
    int cnt = 0;
    for(int i=0;i<arr.size();i++){
        if(arr[i]>0){
            cnt++;
        }
    }
    if(cnt == 0){
        int ans = 0;
        cout<<ans;
    }else if(cnt<=m){
        int ans = 0;
        for(int i=0;i<arr.size();i++){
            if(arr[i]>0){
                ans += arr[i];
            }
        }
        cout<<ans;
    }else if(cnt>m){
        vector<int> array(arr.size()+5);
        for(int i = 0;i<arr.size();i++){                          
            array[i+1] = arr[i];
        }
        vector<int> l(array.size()+5);
        vector<int> r(array.size()+5);
        int n = arr.size();
        int pos_sum = 0;
        set<PII> s;
        for(int i = 1;i<= n;i++){
            l[i] = i-1;
            r[i] = i+1;
            s.insert(PII(abs(array[i]),i));
            if(array[i] > 0){
                pos_sum += array[i];
            }
        }
        vector<int> st(array.size()+5);//节点已经删除标记
        while(cnt > m){
            while(st[s.begin()->second] == 1) s.erase(s.begin());
            int index = s.begin()->second;
            s.erase(s.begin());
            int left = l[index];
            int right = r[index];
            if((left >0 and right<=n) or array[index]>0){
                pos_sum -= abs(array[index]);
                cnt--;
                if(left > 0){
                    array[index] += array[left];
                }
                if(right <= n){
                    array[index] += array[right];
                }   
                s.insert(PII(abs(array[index]),index));
                
                if(left > 0){
                    st[left] = 1;
                    // 修改链表
                    r[l[left]] = r[left];
                    l[r[left]] = l[left];
                }
                if(right <= n){
                    st[right] = 1;
                    // 修改链表
                    r[l[right]] = r[right];
                    l[r[right]] = l[right];
                }
            }
        }
        cout<<pos_sum<<endl;
    }
}

int main(void){
    test01();
    system("pause");
    return 0;
}