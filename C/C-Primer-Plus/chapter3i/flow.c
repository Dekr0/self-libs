#include <stdio.h>
#include <math.h>  // pass -lm when using gcc to compile

int main(void)
{
	float a = 3.4E38 * 100.0f;
	float b = 0.1234E-10 / 2.0f;
	float c = asin(2.0f);  // arcsin

	printf("%e\n", a);
	printf("%e\n", b);
	printf("%e\n", c);

	return 0;
}

