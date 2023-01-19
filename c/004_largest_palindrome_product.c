#include <stdio.h>
#include "gutz_math.h"

void runningNotes()
{
	/*
	THE FOLLOWING FOUR COMMANDS PREPARE AND RUN THIS PROGRAM
		gcc -c gutz_math.c;
		gcc -c 004_largest_palindrome_product.c;
		gcc -o 004_largest_palindrome_product 004_largest_palindrome_product.o gutz_math.o;
		./004_largest_palindrome_product;

	*/
}

void pe_004_notes()
{
	/*
	Largest palindrome product
	004_largest_palindrome_product.c

	A palindromic number reads the same both ways. The largest palindrome 
	made from the product of two 2-digit numbers is 9009 = 91 × 99.
	Find the largest palindrome made from the product of two 3-digit 
	numbers.
	*/
}

int main()
{
	display(largestPalindrome());
	return 0;
}
