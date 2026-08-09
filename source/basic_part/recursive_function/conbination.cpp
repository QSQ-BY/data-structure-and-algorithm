//递归实现组合型枚举（combination）
//假设枚举长度为3，枚举最大值为5，则枚举输出如下
//1 2 3
//1 2 4
//1 2 5
//1 3 4
//1 3 5
//1 4 5
//2 3 4
//2 3 5
//2 4 5
//3 4 5

#include <iostream>
#include <vector>
using namespace std;
vector<int> arr(10);
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

    if(min > max) return;//当最小值大于最大值时，说明没有数字可选了，直接返回
    //num表示填入当前pos位置的数字，枚举范围为min到max，且剩余位置数不能超过剩余数字数,即len-1-pos<=max-num
    for (int num = min; num <= max && len-1-pos<=max-num; num++)
    {
        arr[pos] = num;
        enumeration(pos + 1, num + 1, max, len);
    }
}