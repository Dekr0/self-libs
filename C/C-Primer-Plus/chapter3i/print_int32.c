#include <stdio.h>
#include <inttypes.h>

int main(void)
{
	int32_t i32;

	i32 = 4536827;
	
	printf("i32 = %d\n", i32);  /* assume i32 is int */
	printf("i32 = %" PRId32 "\n", i32);  /* use a macro from head */

	return 0;
}
