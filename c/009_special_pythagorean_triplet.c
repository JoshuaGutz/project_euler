#include <stdio.h>
#include "gutz_math.h"

void runningNotes()
{
	/*
	THE FOLLOWING FOUR COMMANDS PREPARE AND RUN THIS PROGRAM
		gcc -c gutz_math.c;
		gcc -c 009_special_pythagorean_triplet.c;
		gcc -o 009_special_pythagorean_triplet 009_special_pythagorean_triplet.o gutz_math.o;
		./009_special_pythagorean_triplet;

	*/
}

void pe_009_notes()
{
	/*
	Special Pythagorean triplet
	009_special_pythagorean_triplet

	A Pythagorean triplet is a set of three natural numbers, a < b < c, 
	for which, a^2 + b^2 = c^2
	For example, 32 + 42 = 9 + 16 = 25 = 52.

	There exists exactly one Pythagorean triplet for which a + b + c = 1000
	Find the product abc.
	*/
}

int main()
{
	display(specialPythagoreanTriplet());
	return 0;
}
