#include <iostream>
using namespace std;

void foo(int);

int main()
{
	int a = 2, b = 5;

	cout << "In main(), a = " << a << " and &a = " << &a << endl;
	cout << "In main(), b = " << b << " and &b = " << &b << endl;

	foo(a);

	return 0;
}

void foo(int b)
{
	int a = 10;

	cout << "In main(), a = " << a << " and &a = " << &a << endl;
	cout << "In main(), a = " << a << " and &a = " << &b << endl;
}
