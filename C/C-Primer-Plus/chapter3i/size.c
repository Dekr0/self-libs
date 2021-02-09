#include <stdio.h>

int main(void)
{
	/*
	 * unit: bytes
	 * return type of sizeof - size_t
	 */

	printf("int %zd bytes.\n", sizeof(int));
	printf("char %zd bytes.\n", sizeof(char));
	printf("long %zd bytes.\n", sizeof(long));
	printf("float %zd bytes.\n", sizeof(float));
	printf("double %zd bytes.\n", sizeof(double));

	return 0;
}
