/* As is well known, Nikita loves reading. Today, he made a mess in his room and arranged his books long longo n
 stacks in a row, numbered from 1
 to n
 from left to right. The i
-th stack contains ai
 books. This arrangement is called neat if, in every stack except the rightmost one, the number of books is strictly less than in the stack to its right; that is, the array a
 is strictly increasing.

Yura wants to make the arrangement neat by performing the following operation any number of times:

Choose a stack i
 such that 1¡Üi<n
 and ai>1
.
Take 1
 book from the top of stack i
, so ai
 decreases by 1
.
Put this book on top of stack i+1
, so ai+1
 increases by 1
.
Determine whether Yura can make the arrangement neat.

Input
The first line contains a single long longeger t
 (1¡Üt¡Ü104
) ¡ª the number of test cases.

The first line of each test case contains a single long longeger n
 (1¡Ün¡Ü2?105
) ¡ª the number of stacks.

The second line of each test case contains n
 long longegers ai
 (1¡Üai¡Ü109
) ¡ª the initial number of books in each stack.

It is guaranteed that the sum of n
 over all test cases does not exceed 2?105
.

Output
For each test case, output "YES" if Yura can make the arrangement neat, and "NO" otherwise.

You may output each letter in any case (lowercase or uppercase). For example, the strings "yEs", "yes", "Yes", and "YES" will be accepted.

Example
InputCopy
7
3
1 2 3
3
1 1 2
3
10 1 1
3
2 2 2
4
1 4 2 2
5
8 2 8 1 8
4
1 1 3 5
OutputCopy
YES
NO
YES
YES
NO
YES
NO */


#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <unordered_map>
#include <unordered_set>
#include <stack>
#include <queue>

using namespace std;

long long is_clean(vector<long long> books){
    for(long long i=0;i<books.size()-1;i++){
        if(books[i] >= books[i+1]) return 0;
    }
    return 1;
}

string f(vector<long long> books,long long len){
    if(is_clean(books) == 1) return "YES";
    long long sum = 0;
    for(long long i=0;i<books.size();i++){
        long long min = 0;
        min = ((i+1)*(i+2))/2;
        //cout<<"min:"<<min<<endl;
        sum = sum+books[i];
        if(sum >= min) continue;
        else return "NO";
    }
    return "YES";
}

void test01(){
    long long t;//²âÊÔÓÃÀýÊýÁ¿
    cin>>t;
    vector<long long> count;
    vector<vector<long long>> books(t);
    for(long long i=0;i<t;i++){
        long long cnt;
        cin>>cnt;
        count.push_back(cnt);
        for(long long j=0;j<cnt;j++){
            long long number;
            cin>>number;
            books[i].push_back(number);
        }
    }
    for(long long i=0;i<t;i++){
        string s = f(books[i],count[i]);
        cout<<s<<endl;
    }
}

int main(void){
    test01();
    //system("pause");
    return 0;
}