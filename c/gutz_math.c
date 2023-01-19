#include <stdio.h>
#include <string.h> // needed for strtok()
#include <stdlib.h> // needed for atoi()


/*
WHEN ADDING HERE, MUST ADD TO "gutz_math.h" AND SAVE IT !!!!!
*/

int sumMultiples3Or5(int n)
{
	// Find the sum of all the multiples of 3 or 5 below n
	int number = 1;
	int sum = 0;
	while(number < n)
	{
		if((number % 3 == 0) || (number % 5 == 0))
		{
			sum = sum + number;
		}
		number++;
	}
	return sum;
}

void display(int n)
{
	// simply display an integer
	printf("%d\n", n);
}

int isPrime(int number)
{
	if(number == 1)
	{
		return 0;
	}
	int increment = 2;
	int max = number / 2;
	while(increment <= max)
	{
		if(number % increment == 0)
		{
			return 0;
		}
		increment++;
	}
	return 1;
}

int sumEvenFibonacciNumbers(int max)
{
	// Return sum of even valued Fibonacci numbers not exceeding max
	int an_minus_2 = 0;
	int an_minus_1 = 1;
	int an = 0;
	int n = 0;
	int sum_of_even = 0;
	while(an <= max)
	{
		n++;
		an = an_minus_1 + an_minus_2;
		an_minus_2 = an_minus_1;
		an_minus_1 = an;
		if(an % 2 == 0)
		{
			sum_of_even = sum_of_even + an;
		}
	}
	return sum_of_even;
}

int largestPrimeFactor(int number)
{
	//Return largest prime factor of number
	if(isPrime(number))
	{
		return 1;
	}
	int increment = number / 2;
	while(increment)
	{
		if(isPrime(increment))
		{
			if(number / increment * increment == number)
			{
				return increment;
			}
		}
		increment = increment - 1;
	}
}

int numDigits(int n)
{
	// Return number of digits a number has
	// NOTE: integer 0 has 1 digit by design
	if(n == 0)
	{
		return 1;
	}
	int count = 0;
	int temp = n;
	while(temp != 0)
	{
		temp = temp / 10;
		count++;
	}
	return count;
}

void displayArray(int length, int array[])
{
	// Display an array of length length
	/*
	Setup to use numToArray() & displayArray()
	int variable = 246897531;
	int variable_as_array[numDigits(variable)];
	numToArray(variable, variable_as_array);
	displayArray(numDigits(variable),variable_as_array);
	*/

	int i;
	for(i = 0; i < length; i++)
	{
		display(array[i]);
	}
}

void numToArray(int n, int num[])
{
	// Make an array from a number (index is 10^i)
	// meaning zero index is 10^0=1's place
	// n is number, num[] is empty array with length of n
	// ex n = 12,345  --> {5, 4, 3, 2, 1}
	// so that index 10^i= 0, 1, 2, 3, 4
	// 12345 == 5*10^0 + 4*10^1 + 3*10^2 + 2*10^3 + 1*10^4
	/*
	Setup to use numToArray() & displayArray()
	int variable = 246897531;
	int variable_as_array[numDigits(variable)];
	numToArray(variable, variable_as_array);
	displayArray(numDigits(variable),variable_as_array);
	*/

	int temp = n;
	int num_digits;
	num_digits = numDigits(n);
	int i;
	for(i = 0; i < num_digits; i++)
	{
		num[i] = temp % 10;
		temp = temp / 10;
	}
}

int isPalindromic(int n)
{
	// Return if an integer is a palindromic number
	int num_digits;
	num_digits = numDigits(n);
	int n_as_array[num_digits];
	numToArray(n, n_as_array);
	int i;
	for(i = 0; i < num_digits / 2; i++)
	{
		if(n_as_array[i] != n_as_array[num_digits - 1 - i])
		{
			return 0;
		}
	}
	return 1;
}

int largestPalindrome()
{
	//Finds the largest palindrome made from the product of two 
	// 3-digit numbers
	// project euler number 004
	int i = 999;
	int answer = 0;
	while(i > 99)
	{
		int j = 999;
		while(j > 99)
		{
			if((isPalindromic(i * j)) && (i * j > answer))
			{
				answer = i * j;
			}
			j--;
		}
		i--;
	}
	return answer;
}

void testing(int test1, int test2, int test3, int test4, int test5)
{
	// Start of a testing program
	printf("testin input %d: %d\n",test1, (test1));
	printf("testin input %d: %d\n",test2, (test2));
	printf("testin input %d: %d\n",test3, (test3));
	printf("testin input %d: %d\n",test4, (test4));
	printf("testin input %d: %d\n",test5, (test5));
}

int power(int base, int exp)
{
	// Return base to the exp
	int result = 1;
	while(exp) 
	{
		result = result * base;
		exp--; 
	}
	return result;
}

int sumOfSquares(int first_n_numbers)
{
	// Return Sum of Squares for first n numbers
	int i;
	int total = 0;
	for(i = 1; i <= first_n_numbers; i++)
	{
		total = total + power(i, 2);
	}
	return total;
}

int squareOfSum(int first_n_numbers)
{
	// Return Square of Sum for first n numbers
	int i;
	int total = 0;
	for(i = 1; i <= first_n_numbers; i++)
	{
		total = total + i;
	}
	return power(total, 2);
}

int sumSquareDifference(int first_n_numbers)
{
	/*
	Return difference between the sum of the squares of the first n 
	natural numbers and the square of the sum.
	*/
	// project euler number 006
	return squareOfSum(first_n_numbers) - sumOfSquares(first_n_numbers);
}

int nthPrime(int n)
{
	// Return the nth prime
	if(n == 1)
	{
		return 2;
	}
	int i = 2;
	int test_prime = 3;
	while(i < n)
	{
		test_prime = test_prime + 2;
		if(isPrime(test_prime))
		{
			i++;
		}
	}
	return test_prime;
}

int specialPythagoreanTriplet()
{
	/*
	There exists exactly one Pythagorean triplet for which 
	a + b + c = 1000.
	Finds the product abc.
	*/
	int a;
	int b;
	int c;
	for(a = 1; a < 1000; a++)
	{
		for(b = a; b < 1000; b++)
		{
			c = 1000 - a - b;
			if(power(a, 2) + power(b, 2) == power(c, 2))
			{
				return (a * b * c);
			}
		}
	}
}

int sumPrimesBelow(int n)
{
	// Return sum of primes below n
	int i;
	int sum = 0;
	for(i = 1; i < n; i++)
	{
		if(isPrime(i))
		{
			sum = sum + i;
		}
	}
	return sum;
}

void naturalArray(int array[], int n)
{
	// Make array[] of length n have natural numbers 1, 2, ..., n
	/*
	// How to use naturalArray & printArray
	int length_array = 10;
	int test_array1[length_array];
	naturalArray(test_array1, length_array);
	printArray(test_array1, length_array);
	*/
	int i;
	for(i = 0; i < n; i++)
	{
		array[i] = i;
	}
}

void printArray(int array[], int n)
{
	// Print array[] of length n identifying indexes
	/*
	// How to use naturalArray & printArray
	int length_array = 10;
	int test_array1[length_array];
	naturalArray(test_array1, length_array);
	printArray(test_array1, length_array);
	*/
	int i;
	for(i = 0; i < n; i++)
	{
		printf("index %d: %d \n", i, array[i]);
	}
}

void parseCharArray(char line[], int line_length, int line_ints[])
{
	// Takes three inputs like below
	// Changes line_ints[line_length] to be each integer of line[]
	/*
	char line[] = "0 1 2 4 8 15 27 434";
	int line_length = 8;
	int line_ints[line_length];
	*/
	//printf("Parsing input string '%s'\n", line);
	char *line_token = strtok(line, " ");
	char *line_tokens[line_length];
	int i = 0;
	line_tokens[i] = line_token;
	while(line_token)
	{
		int token_int = atoi(line_tokens[i]);
		line_ints[i] = token_int;
		//display(token_int);
		//printf("%s\n", line_tokens[i]);
		i++;
		line_token = strtok(NULL, " ");
		line_tokens[i] = line_token;
	}
}

void printFile(char *filename)
{
	// Print a file
	FILE *file_pointer;
	char ch;

	/*  open the file for reading */
	file_pointer = fopen(filename, "r");
	if(file_pointer == NULL)
	{
		printf("Cannot open file \n");
	}
	ch = fgetc(file_pointer);
	while(ch != EOF)
	{
		printf("%c", ch);
		ch = fgetc(file_pointer);
	}
	fclose(file_pointer);
}

void copyFile( char *file1, char *file2)
{
	// Copy file1 to new file file2
	// taken from internet, need to better understand
	FILE *file_pointer1, *file_pointer2;
	char a;

	file_pointer1 = fopen(file1, "r");
	if(file_pointer1 == NULL)
	{
		printf("cannot open file1");
	}

	file_pointer2 = fopen(file2, "w");
	if(file_pointer2 == NULL)
	{
		printf("cannot open file2");
		fclose(file_pointer1);
	}
	do
	{
		a = fgetc(file_pointer1);
		fputc(a, file_pointer2);
	}
	while(a != EOF);
	fclose(file_pointer1);
	fclose(file_pointer2);
}

int numRowsInFile(char *filename)
{
	// Return number of rows in a file
	FILE *file_pointer;
	char ch;
	int rows = 0;
	/*  open the file for reading */
	file_pointer = fopen(filename, "r");
	if(file_pointer == NULL)
	{
		printf("Cannot open file \n");
	}
	ch = fgetc(file_pointer);
	while(ch != EOF)
	{
		if(ch == '\n')
		{
			rows++;
		}
		ch = fgetc(file_pointer);
	}
	fclose(file_pointer);
	return rows;
}

int max(int a, int b)
{
	// Returns max of a and b
	if(a > b)
	{
		return a;
	}
	return b;
}

int sumDiagNumSpiral(int n)
{
	// Returns sum of diagonals 
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

	the sum of the numbers on the diagonals is 101

	21 + 7 + 1 + 3 + 13 + 17 + 5 + 9 + 25 = 101

	What is the sum of the numbers on the diagonals in a 1001 by 1001 
	spiral formed in the same way?
	*/

	// by math i proved that for n x n spirals the sum of the corners is
	/*
	i  | sum_four_corners
	1  |     1 * 4 + (i - 1) * 6 // BUT THIS COUNTS A SQUARE WITH 4 ONES
	3  |     3 * 4 + (i - 1) * 6
	5  |    13 * 4 + (i - 1) * 6
	7  |    31 * 4 + (i - 1) * 6
	i  | x_(i) * 4 + (i - 1) * 6 where x_(i) = x_(i-2) + ((i-1)-2)*3 + (i-1)
	
	the total sum of diagonals is the sum of the sum_four_corners

	Because i = n = 1 gives 4 instead of 1, subtract 3 from final answer
	*/
	int i = 1;
	int sum_four_corners = 0;
	int total = -3;  //Because i = 1 gives 4 instead of 1, subtract 3 from total
	int x_i = 1;
	while(i <= n)
	{
		sum_four_corners = x_i * 4 + (i - 1) * 6;
		total = total + sum_four_corners;
		i = i + 2;
		x_i = x_i + ((i - 1) - 2) * 3 + (i - 1);
	}
	return total;
}

void printNRowsOfFile(int rows, char *filename)
{
	// Print first n rows of file
	FILE *file_pointer;
	char ch;
	int i = 0;
	/*  open the file for reading */
	file_pointer = fopen(filename, "r");
	if(file_pointer == NULL)
	{
		printf("Cannot open file \n");
	}
	ch = fgetc(file_pointer);
	while(ch != EOF && i < rows)
	{
		printf("%c", ch);
		if(ch == '\n')
		{
			i++;
		}
		ch = fgetc(file_pointer);
	}
	fclose(file_pointer);
}

int pointQuadrant(int x, int y)
{
	// Returns cartesian quadrant of point x,y
	// Returns 0 if point is on an axis
	if(x > 0 && y > 0)
	{
		return 1;
	}
	if(x < 0 && y > 0)
	{
		return 2;
	}
	if(x < 0 && y < 0)
	{
		return 3;
	}
	if(x > 0 && y < 0)
	{
		return 4;
	}
	return 0;  // point is on an axis
}

int posRelToLine(double line[4], double px, double py)
{
	// Return position of (px,py) relative to line fm (x1,y1) to (x2,y2)
	// Return +1 if (px,py) is above line
	// Return  0 if (px,py) is ON line
	// Return -1 if (px,py) is below line
	// y = m x + b
	// b =  y1 - m * x1

	// Assign variables
	double x1 = line[0];
	double y1 = line[1];
	double x2 = line[2];
	double y2 = line[3];

	double m = (y2 - y1) / (x2 - x1);
	// b = y1 - m * x1;
	double b = y1 - ((y2 - y1) / (x2 - x1)) * x1;
	// y_line = m * px + b;
	double y_line = ((y2 - y1) / (x2 - x1)) * px + (y1 - ((y2 - y1) / (x2 - x1)) * x1);
	if(py > y_line)
	{
		return 1;
	}
	if(py == y_line)
	{
		return 0;
	}
	return -1;
}

int triangleContainsOrigin(double points[6])
{
	// Return 1/0 (T/F) if triangle P1-P2-P3 contains (0, 0)

	// Assign variables
	double x1 = points[0];
	double y1 = points[1];
	double x2 = points[2];
	double y2 = points[3];
	double x3 = points[4];
	double y3 = points[5];

	double line1[4] = {x2, y2, x3, y3};
	double line2[4] = {x1, y1, x3, y3};
	double line3[4] = {x1, y1, x2, y2};

	// check if origin is on any line
	if(posRelToLine(line1, 0, 0) == 0 ||
		posRelToLine(line2, 0, 0) == 0 ||
		posRelToLine(line3, 0, 0) == 0)
	{
		return 1;
	}

	// check if origin is not on same side of line P2-P3 as P1
	if(posRelToLine(line1, x1, y1) != 
		posRelToLine(line1, 0, 0))
	{
		return 0;
	}

	// check if origin is not on same side of line P1-P3 as P2
	if(posRelToLine(line2, x2, y2) != 
		posRelToLine(line2, 0, 0))
	{
		return 0;
	}

	// check if origin is not on same side of line P1-P2 as P3
	if(posRelToLine(line3, x3, y3) != 
		posRelToLine(line3, 0, 0))
	{
		return 0;
	}
	return 1;
}

int sumContainedTriangles(char *filename)
{
	// 	Returns number of triangles in filename that contain the origin
	// Project Euler problem 102
	int contained_triangles = 0;
	// parse file
	FILE *file_pointer;
	/*  open the file for reading */
	file_pointer = fopen(filename, "r");
	if(file_pointer == NULL)
	{
		printf("Cannot open file \n");
	}
	int col = 0;
	double points[6];
	char *token;
	char line[40];
	while(fgets(line, sizeof line, file_pointer) != NULL)
	{
		token = strtok(line, ",");
		for(col = 0; col < 6; col++)
		{
			points[col] = atof(token);
			token = strtok(NULL, ",");
		}
		if(triangleContainsOrigin(points))
		{
			contained_triangles++;
		}
	}
	fclose(file_pointer);
	return contained_triangles;
}

