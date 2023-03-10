#include <stdio.h>
#include "gutz_math.h"

void runningNotes()
{
	/*
	THE FOLLOWING FOUR COMMANDS PREPARE AND RUN THIS PROGRAM
		gcc -c gutz_math.c;
		gcc -c 002_even_fibonacci_numbers.c;
		gcc -o 002_even_fibonacci_numbers 002_even_fibonacci_numbers.o gutz_math.o;
		./002_even_fibonacci_numbers;

	*/
}

void pe_002_notes()
{
	/*
	Even Fibonacci numbers
	002_even_fibonacci_numbers.c

	Each new term in the Fibonacci sequence is generated by adding 
	the previous two terms. By starting with 1 and 2, the first 10 
	terms will be:

	an: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
	n:  1, 2, 3, 4, 5,  6,  7,  8,  9, 10, ...

	By considering the terms in the Fibonacci sequence whose values 
	do not exceed four million, find the sum of the even-valued terms.
	*/
}

int main()
{
	printf("for 3 the answer is: %d\n",sumEvenFibonacciNumbers(3));
	printf("for 6 the answer is: %d\n",sumEvenFibonacciNumbers(6));
	printf("for 4000000 the answer is: %d\n",sumEvenFibonacciNumbers(4000000));
	return 0;
}
