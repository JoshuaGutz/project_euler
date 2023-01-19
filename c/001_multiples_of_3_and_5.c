#include <stdio.h>
#include "gutz_math.h"

void runningNotes()
{
	/*
	THE FOLLOWING FOUR COMMANDS PREPARE AND RUN THIS PROGRAM
		gcc -c gutz_math.c;
		gcc -c 001_multiples_of_3_and_5.c;
		gcc -o 001_multiples_of_3_and_5 001_multiples_of_3_and_5.o gutz_math.o;
		./001_multiples_of_3_and_5;

	*/
}

void pe_001_notes()
{
	/*
	Multiples of 3 and 5
	001_multiples_of_3_and_5.c

	If we list all the natural numbers below 10 that are multiples of 
	3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

	Find the sum of all the multiples of 3 or 5 below 1000.
	*/
}

int main()
{
	printf("for 10 the answer is: %d\n",sumMultiples3Or5(10));
	printf("for 1000 the answer is: %d\n",sumMultiples3Or5(1000));
	return 0;
}
