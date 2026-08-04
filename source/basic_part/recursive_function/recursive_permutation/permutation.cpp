// 递归实现排列型枚举(permutation)
// 假设对3进行排列型枚举，则枚举输出如下
// 1 2 3
// 1 3 2
// 2 1 3
// 2 3 1
// 3 1 2
// 3 2 1
#include <iostream>
#include <vector>
using namespace std;
vector<int> arr(10);
vector<int> flag(10, 0); // flag数组用来标记数字是否被使用过，0表示未使用，1表示已使用

void print_oneline(vector<int> &arr)
{
    for (int i = 0; i < arr.size(); i++)
    {
        if (arr[i])
        {
            cout << arr[i] << " ";
        }
    }
    cout << endl;
}

void enumeration(int pos, int min, int max, int len);
// pos表示当前填入数字的位置，该行枚举最小值为min，最大值为max,排列长度为len
int main(void)
{
    int pos{0};
    int min{1};
    int max{};
    int len{};

    cout << "请输入排列长度" << endl;
    cin >> len;
    cout << "请输入排列的最大值" << endl;
    cin >> max;
    enumeration(pos, min, max, len);
    system("pause");
    return 0;
}

void enumeration(int pos, int min, int max, int len)
{
    if (pos == len)
    {
        print_oneline(arr);
        return;
    }

    for (int i = min; i <= max; i++)
    {
        if (flag[i])
            continue;
        else
        {
            arr[pos] = i;
            flag[i] = 1;
            enumeration(pos + 1, min, max, len);
            flag[i] = 0;
        }
    }

    return;
}

