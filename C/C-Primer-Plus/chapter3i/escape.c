#include <stdio.h>

int main(void)
{
	char beep_oat = '\007';
	char beep_hex = '\x07';

	printf("%c %c", beep_oat, beep_hex);
	printf("Gramps, sez, \"a \\ is a blackslah.\"\n");

	return 0;
}

