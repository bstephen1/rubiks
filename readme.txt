rubiks cube cipher program

The cube is a 6 sided rubiks cube, with faces [front, back, up, down, left, right]
Blocks of text are read into the cube left to right and top to bottom in the following order: front, up, back, down, left, right
The cube may be any NxN cube, where N > 0
There are three sets of rotations:
	set1: [front, up, back, down]
	set2: [front, right, back, left]
	set3: [up, left, down, right]
The key works as follows:
	key is a list of numbers where abs(x) <= 3*N, and x != 0 for every element x of the list
	any x where abs(x) <= n will be in set1
	any x where n < abs(x) <= 2*n will be in set2
	any x where abs(x) > 2*n will be in set3
	any x that is positive will rotate through its set to the right
	any x that is negative will rotate through its set to the left
	individual x's are the columns/rows to be rotated, starting from the top left corner of the first index of the set and counting right/down


usage: rubiks.py [-h] [-n [N]] [-i [INPUT]] [-o [OUTPUT]] key [key ...]
key is required. key is a set of numbers separated by a space 
-n is optional. set the size of the cube (default = 3)
-i/-in/--input is optional. set an input file to read from (default = sys.stdin)
	note: program supports all ascii characters in the input file. 
	non-standard characters will be removed in formatting (only lowercase/uppercase alphatical characters remain)
	format changes all lowercase to uppercase and writes out numbers (eg, "9" = "nine"), as well as removing non-alphabetical ascii values
-o/-out/--output is optional. set an output file to write data to (default = sys.stdout)
	output is printed block-wise. so a 1x1 block will have 6 characters per line
	
	
test.py is a test program that tests rubiks.py for cubes of various sizes. 
to test, put any text in input.txt, and all other files will be generated. 
provided are the first few paragraphs of rubiks cube from Wikipedia.
	