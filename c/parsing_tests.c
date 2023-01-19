#include <stdio.h>
#include <string.h>

// gcc parsing_tests.c; ./a.out

void naturalArray(int array[], int n)
{
	// Make array[] of length n have natural numbers 1, 2, ..., n
	int i;
	for(i = 0; i < n; i++)
	{
		array[i] = i;
	}
}

void printArray(int array[], int n)
{
	// Print array[] of length n identifying indexes
	int i;
	for(i = 0; i < n; i++)
	{
		printf("index %d: %d \n", i, array[i]);
	}
}

int main()
{
	int length_array = 10;
	int test_array1[length_array];

//	naturalArray(test_array1, length_array);
//	printArray(test_array1, length_array);

	char *string = "10 25 45 78";
   	// printf("%s\n", string); SAME AS puts(string);
//	printf("%s\n", string);
//	puts(string);
//	printf("\n");

	char line[] = "0 1 2 4 8 15 27 234";
    printf("Parsing input string '%s'\n", line);
    char *line_tk = strtok(line, " ");
    
    int length_line = 8;


    while(line_tk) 
    {
    	printf("%s\n", line_tk);
        line_tk = strtok(NULL, " ");
    }




	return 0;
}
