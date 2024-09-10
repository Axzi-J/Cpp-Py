#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main()
{
    int x;
    cin >> x;
    int y=2;
    int i=20000;
 
while (y<i)
{
    if (x % y == 0)
    {
    cout << y << endl;
    x = x/y; 

    }
    else{
    y++;
    }

}

    return 0;
}