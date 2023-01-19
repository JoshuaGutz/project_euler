#include <stdio.h>
#include "gutz_math.h"

void runningNotes()
{
	/*
	THE FOLLOWING FOUR COMMANDS PREPARE AND RUN THIS PROGRAM
		gcc -c gutz_math.c;
		gcc -c 010_summation_of_primes.c;
		gcc -o 010_summation_of_primes 010_summation_of_primes.o gutz_math.o;
		./010_summation_of_primes;

	*/
}

void pe_010_notes()
{
	/*
	Summation of primes
	010_summation_of_primes

	The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

	Find the sum of all the primes below two million.
	*/
}

int main()
{
	display(sumPrimesBelow(10));
//	display(sumPrimesBelow(2000000));
	return 0;
}
