#include <stdio.h>
int main(void)
{
	int num;  /* define a var called num */
	num = 1;  /* assign a value to var */ 

	printf("I am a simple ");
	printf("computer.\n");
	printf("My favorite number is %d because it is first.\n", num);

	getchar();  /* prevent close automatically */

	return 0;
}
