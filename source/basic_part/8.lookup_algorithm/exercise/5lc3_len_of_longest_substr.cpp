/* 给定一个字符串s，请你找出其中不含有重复字符的最长子串的长度。
示例 1:
输入: s = "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3
注意 "bca" 和 "cab" 也是正确答案。
示例 2:
输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:
输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。 */


//01二分算法,查找最后一个1的位置
//x->长度1 2 3 ....... l l+1 l+2 ....... n
//y->能否1 1 1 ....... 1  0   0  ....... n
//f:给出相关字串的长度，判断是否包含重复字符
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <unordered_map>
#include <unordered_set>

using namespace std;
class Solution{
public:
//传入一个字符串和一个长度len，判断是否存在长度为len的不含重复字符的字串
    int check(string& s,int len){
        vector<int> cnt(256);//统计窗口中每一种字符出现的次数
        int k = 0;//统计窗口内不同字符的数量
        for(int i=0;i<s.size();i++){
            cnt[s[i]]++;
            if(cnt[s[i]] == 1) k++;
            if(i>=len) {
                cnt[s[i-len]]--;
                if(cnt[s[i-len]] == 0) k--;
            }
            if(len == k) return 1;
        }
        return 0;
    }
    int lengthOfLongestSubstring(string s) {
        int head = 0;
        int tail = s.size();
        int mid = head + (tail-head+1)/2;
        while(head<tail){
            mid = head + (tail-head+1)/2;
            if(check(s,mid) == 1) head = mid;
            else tail = mid-1;
        }
        return head;
    }
};

void test01(){
    Solution s;
}

int main(void){
    test01();
    system("pause");
    return 0;
}