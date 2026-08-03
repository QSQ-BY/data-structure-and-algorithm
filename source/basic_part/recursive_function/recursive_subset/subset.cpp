// 递归实现子集型枚举(subset)
//如果对3进行枚举
// 1
// 1 2
// 1 3
// 1 2 3
// 2
// 2 3
// 3

#include <iostream>
#include <vector>
using namespace std;
vector<int> arr(10);
void print_oneline(vector<int> &arr ,int pos)
{
    for (int i = 0; i <= pos; i++)
    {
        if (arr[i])
        {
            cout << arr[i] << " ";
        }
    }
    cout << endl;
}

void enumeration(int pos, int min, int max);
// pos表示当前填入数字的位置，该行枚举最小值为min，最大值为max
int main(void)
{
    int pos{0};
    int min{1};
    int max{};
    cout << "请输入枚举的最大值" << endl;
    cin >> max;
    enumeration(pos, min, max);
    system("pause");
    return 0;
}

void enumeration(int pos, int min, int max)
{
    if (min > max) return; //当最小值大于最大值时，说明没有数字可选了，直接返回
    
    for(int num = min; num <= max;num++){
        arr[pos] = num;
        print_oneline(arr,pos);
        enumeration(pos + 1, num + 1, max);
    }
}