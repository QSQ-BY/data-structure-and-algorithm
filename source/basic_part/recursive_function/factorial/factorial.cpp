#include <iostream>
using namespace std;
int factorial(int n)
{
    if (n == 0 || n == 1)
    {
        return 1;
    }
    return n * factorial(n - 1);
}
int main(void)
{
    cout << "5µÄ½×³ËÎª" << factorial(5) << endl;
    system("pause");
    return 0;
}