#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "gutz_math.h"

// ./run 102_triangle_containment

void runningNotes()
{
	/*
	THE FOLLOWING FOUR COMMANDS PREPARE AND RUN THIS PROGRAM
		gcc -c gutz_math.c;
		gcc -c 102_triangle_containment.c;
		gcc -o 102_triangle_containment 102_triangle_containment.o gutz_math.o;
		./102_triangle_containment;
	*/
}

void pe_102_notes()
{
	/*
	Triangle containment
	
	102_triangle_containment.c

	Three distinct points are plotted at random on a Cartesian plane, 
	for which -1000 ≤ x, y ≤ 1000, such that a triangle is formed.

	Consider the following two triangles:
		A(-340,495), B(-153,-910), C(835,-947)
		X(-175,41), Y(-421,-714), Z(574,-645)

	It can be verified that triangle ABC contains the origin, 
	whereas triangle XYZ does not.

	Using triangles.txt, a 27K text file containing the co-ordinates of 
	one thousand "random" triangles, find the number of triangles for which 
	the interior contains the origin.

	NOTE: The first two examples in the file represent the triangles in the 
	example given above.
	*/
}

int main()
{
	display(sumContainedTriangles("p102_triangles.txt"));
	return 0;
}
