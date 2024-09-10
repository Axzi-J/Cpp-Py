#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main()
{
    double a;
    cin >> a;
    double b;
    cin >> b;
    double c;
    cin >> c;

    const double result =a+b;
    const double result2 =result - c;
    cout << result2 << endl;

}