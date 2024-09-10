#include <iostream>
#include <vector>
#include <string>
#include <math.h>
using namespace std;

int main()
{
    int i=0;
    int n;
    cin >> n;
    float a=0;

while (i<=n-1){
double z = (pow(-1,i))/(2*i+1);
 cout << z << endl;
a=z+a;
i++;
}
a=a*4;
 cout << a << endl;
}