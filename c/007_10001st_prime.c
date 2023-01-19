#include <stdio.h>
#include "gutz_math.h"

void runningNotes()
{
	/*
	THE FOLLOWING FOUR COMMANDS PREPARE AND RUN THIS PROGRAM
		gcc -c gutz_math.c;
		gcc -c 007_10001st_prime.c;
		gcc -o 007_10001st_prime 007_10001st_prime.o gutz_math.o;
		./007_10001st_prime;

	*/
}

void pe_007_notes()
{
	/*
	10001st prime
	007_10001st_prime.c

	By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
	we can see that the 6th prime is 13.

	What is the 10,001st prime number?
	*/
}

int main()
{
	display(nthPrime(10001));
	return 0;
}
