#include <stdio.h>

int main(void)
{
	char ch;

	printf("Enter a character.\n");
	scanf("%c", &ch);  /* read a char from input and assign to var ch */
	printf("The code for %c is %d.\n", ch, ch);

	return 0;
}
