#include <stdio.h>
#include "gutz_math.h"

// ./run 028_number_spiral_diagonals

void runningNotes()
{
	/*
	THE FOLLOWING FOUR COMMANDS PREPARE AND RUN THIS PROGRAM
		gcc -c gutz_math.c;
		gcc -c 028_number_spiral_diagonals.c;
		gcc -o 028_number_spiral_diagonals 028_number_spiral_diagonals.o gutz_math.o;
		./028_number_spiral_diagonals;

	*/
}

void pe_028_notes()
{
	/*
	Number spiral diagonals
	028_number_spiral_diagonals.c
	Starting with the number 1 and moving to the right in a clockwise 
	direction a 5 by 5 spiral is formed as follows:

	21 22 23 24 25
	20  7  8  9 10
	19  6  1  2 11
	18  5  4  3 12
	17 16 15 14 13

	It can be verified that the sum of the numbers on the diagonals is 101

	What is the sum of the numbers on the diagonals in a 1001 by 1001 
	spiral formed in the same way?
	*/
}

int main()
{
	display(sumDiagNumSpiral(5));
	display(sumDiagNumSpiral(1001));
	return 0;
}
