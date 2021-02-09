#include <stdio.h>

int main(void)
{
	float salary;

	printf("\aEnter your desired monthly salary:");
	printf(" $_______\b\b\b\b\b\b\b");
	scanf("%f", &salary);
	printf("\t$%.2f a month is $%.2f a year.\n", salary, salary * 12.0);
	
	return 0;
}
