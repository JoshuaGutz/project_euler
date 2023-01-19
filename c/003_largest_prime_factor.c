#include <stdio.h>
#include "gutz_math.h"

void runningNotes()
{
	/*
	THE FOLLOWING FOUR COMMANDS PREPARE AND RUN THIS PROGRAM
		gcc -c gutz_math.c;
		gcc -c 003_largest_prime_factor.c;
		gcc -o 003_largest_prime_factor 003_largest_prime_factor.o gutz_math.o;
		./003_largest_prime_factor;

	*/
}

void pe_003_notes()
{
	/*
	Largest prime factor
	003_largest_prime_factor.c

	The prime factors of 13195 are 5, 7, 13 and 29.

	What is the largest prime factor of the number 600851475143 ?
	*/
}

int main()
{
	int test1 = 1;
	int test2 = 2;
	int test3 = 3;
	int test4 = 4;
	int test5 = 5;
	int test6 = 6;
	int test7 = 7;
	int testx = 13195;
//	signed long long int testz = 600851475143;
    printf("for %d: %d\n",test1, largestPrimeFactor(test1));
    printf("for %d: %d\n",test2, largestPrimeFactor(test2));
    printf("for %d: %d\n",test3, largestPrimeFactor(test3));
    printf("for %d: %d\n",test4, largestPrimeFactor(test4));
    printf("for %d: %d\n",test5, largestPrimeFactor(test5));
    printf("for %d: %d\n",test6, largestPrimeFactor(test6));
    printf("for %d: %d\n",test7, largestPrimeFactor(test7));
    printf("for %d: %d\n",testx, largestPrimeFactor(testx));
//	printf("for %lli: %d\n",testz, largestPrimeFactor(testz));
	return 0;
}
