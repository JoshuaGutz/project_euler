#include <stdio.h>
#include "gutz_math.h"

void runningNotes()
{
	/*
	THE FOLLOWING FOUR COMMANDS PREPARE AND RUN THIS PROGRAM
		gcc -c gutz_math.c;
		gcc -c 006_sum_square_difference.c;
		gcc -o 006_sum_square_difference 006_sum_square_difference.o gutz_math.o;
		./006_sum_square_difference;

	*/
}

void pe_006_notes()
{
	/*
	Sum square difference
	006_sum_square_difference.c

	The sum of the squares of the first ten natural numbers is,
	1^2 + 2^2 + ... + 10^2 = 385

	The square of the sum of the first ten natural numbers is,
	(1 + 2 + ... + 10)^2 = 552 = 3025

	Hence the difference between the sum of the squares of the first ten 
	natural numbers and the square of the sum is 3025 − 385 = 2640.

	Find the difference between the sum of the squares of the first one 
	hundred natural numbers and the square of the sum.
	*/
}

int main()
{
	display(sumSquareDifference(100));
	return 0;
}
