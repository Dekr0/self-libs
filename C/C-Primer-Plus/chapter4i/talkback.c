#include <stdio.h>
#include <string.h>  // provide strlen() function prototype
#define DENSITY 62.4  // human density

int main()
{
	float weight, volume;
	int size, letters;
	char name[40];  // name is a array that can storage 40 chars

	printf("Hi, What's your first name?\n");
	scanf("%s", name);
	printf("%s, what's your weight in pounds?\n", name);
	scanf("%f", &weight);
	size = sizeof(name);  // the bytes size of the array
	letters = strlen(name);  // the number of char currently stored in the char array "name"
	volume = weight / DENSITY;
	printf("Well, %s, your volume is %2.2f cubic feet.\n", name, volume);
	printf("Also, your first name has %d letters, \n", letters);
	printf("and we have %d bytes to store it.\n", size);

	return 0;
}

