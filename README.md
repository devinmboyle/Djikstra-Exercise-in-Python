////////////////////////////////////////////////////////////////////////////////////////
README
////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////
Devin Boyle
dmboyle@alaska.edu
CSCE 311
HW 5 - Graphs and Djikstra's Algorithm
////////////////////////////////////////////////////////////////////////////////////////

////////////
DESCRIPTION/
////////////

This program reads text from a user-specified input file, and converts that text to a matrix of integers representing a graph.  After successfully creating a representation of the graph, the program does a series of operations on the graph using Djikstra's Algorithm.  The program then outputs the shortest path from every point in the graph to a series of set locations in the graph, like so:

---------------------------------------------------------------------
Starting point:  Starting point
From Starting point to to Cache1 to Train Station
Reflecting Pool, Cache 1, Arboretum, Train Station
Estimated Time: 11 minutes.

From Starting point to to Cache1 to Airport
Reflecting Pool, Cache 1, Arboretum, Airport
Estimated Time: 10 minutes.

From Starting point to to Cache2 to Train Station
Reflecting Pool, Jefferson Memorial, Cache 2, Airport, Arboretum, Train Station
Estimated Time: 18 minutes.

From Starting point to to Cache2 to Airport
Reflecting Pool, Jefferson Memorial, Cache 2, Airport
Estimated Time: 15 minutes.
---------------------------------------------------------------------
This output is repeated one time for every node represented in the graph.

After printing these results, the program terminates.
////////////////////////////////////////////////////////////////////////////////////////

///////
TO RUN/
///////

To run this program, use the command:

	python bluesparrow.py input.txt

This program will handle file I/O issues in the following scenarios:
	1)The file is not found
	2)The file reads in a non-decimal character
	3)The matrix provided is not symmetrical

In the case the user provides a filename that results in one of these errors, the program will prompt the user to re-enter the filename.

This uses the numpy library for a basic array transposition when checking to see if the matrix being read in is not symmetrical. For windows, this was added using the command:
	python -m pip install --user numpy

////////////////////////////////////////////////////////////////////////////////////////

////////////////////
FILE REPRESENTATION/
////////////////////

To make parsing easier, I have made the file representation of my graph nothing but numbers delimited by spaces and commas, with returns separating lists corresponding to the adjacency values of a particular number, like so:

0, 5, 0, 0, 0, 7, 0, 0, 0, 4
5, 0, 13, 4, 0, 0, 0, 0, 0, 6
0, 13, 0, 8, 2, 0, 0, 0, 0, 0
0, 4, 8, 0, 5, 3, 0, 0, 0, 0
0, 0, 2, 5, 0, 5, 0, 1, 0, 0
7, 0, 0, 3, 5, 0, 2, 0, 0, 0
0, 0, 0, 0, 0, 2, 0, 3, 3, 5
0, 0, 0, 0, 1, 0, 3, 0, 5, 0
0, 0, 0, 0, 0, 0, 3, 5, 0, 4
4, 6, 0, 0, 0, 0, 5, 0, 4, 0

For correct functioning, the file representation of your table should be a 10X10 graph of decimal values delimited by commas, as shown above.

For those wishing to change the existing matrix, or create their own, values for the nodes of the adjacency matrix have been predefined as such:

0:Russian Embassy
1:Reflecting Pool
2:Train Station
3:Cache 1
4:Arboretum
5:Lincoln Memorial
6:Ford Theater
7:Airport
8:Cache 2
9:Jefferson Memorial

Changes in the matrix will retain these naming conventions for 10x10 matrices.
//////////////////////////////////////////////////////////////////////////////////////// 
