/* Stepan found a permutation p
 of length n
. Of course, he decided to sort it. To make the process more interesting, he chose two positive integers x
 and y
 (x+y¡Ün)
 and defined a rule for swapping elements.

In one move, Stepan can choose two indices i
 and j
 (1¡Üi,j¡Ün)
 and swap the elements pi
 and pj
 if at least one of the following conditions holds:

|i?j|=x
|i?j|=y
Stepan wants to know whether it is possible to sort the permutation in ascending order using any number of such operations. Help him answer this question.

Input
The first line contains a single integer t
 (1¡Üt¡Ü104)
 ¡ª the number of test cases.

The first line of each test case contains three integers n
, x
, and y
 (1¡Üx,y¡Ün¡Ü2?105
, x+y¡Ün)
 ¡ª the length of the array and the numbers chosen by Stepan.

The second line of each test case contains n
 integers pi
 (1¡Üpi¡Ün)
 ¡ª the array p
; it is guaranteed that p
 is a permutation.

It is guaranteed that the sum of n
 over all test cases does not exceed 2?105
.

Output
For each test case, output "YES" if it is possible to sort the permutation with the given x
 and y
, and "NO" otherwise.

You may output each letter in any case (lowercase or uppercase). For example, the strings "yEs", "yes", "Yes", and "YES" will be accepted.

Example
InputCopy
4
5 2 3
5 4 3 2 1
6 2 4
2 1 4 3 6 5
4 2 2
1 2 3 4
5 2 3
1 2 3 5 4
OutputCopy
YES
NO
YES
YES */
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <unordered_map>
#include <unordered_set>
#include <stack>
#include <queue>
#include <numeric>
using namespace std;

string f(const vector<int>& arr, int x, int y){
    int g = gcd(x, y);
    for (int i = 0; i < (int)arr.size(); i++){
        if (arr[i] % g != (i + 1) % g)
            return "NO";
    }
    return "YES";
}

void test01(){
    int t;
    cin>>t;
    vector<int> n;
    vector<int> x;
    vector<int> y;
    vector<vector<int>> arr(t);
    for(int i = 0;i<t;i++){
        int temp_n;
        int temp_x;
        int temp_y;
        cin>>temp_n>>temp_x>>temp_y;
        n.push_back(temp_n);
        x.push_back(temp_x);
        y.push_back(temp_y);
        for(int j=0;j<temp_n;j++){
            int number;
            cin>>number;
            arr[i].push_back(number);
        }
    }
    for(int i=0;i<t;i++){
        string ans = f(arr[i],x[i],y[i]);
        cout<<ans<<endl;
    }
}

int main(void){
    test01();
    //system("pause");
    return 0;
}