#rubik's cube cipher
from copy import deepcopy
import sys
import argparse

#padding alphabet. A string of any length
alphabet = "AAABBBCCCDDDEEEFFFGGGHHHIIIJJJKKKLLLMMMNNNOOOPPPQQQRRRSSSTTTUUUVVVWWWXXXYYYZZZ"

#creates a cube of size n
def createCube(n) :
	cube = [[] for x in range(6)]
	for x in range(6) :
		cube[x] = [[[] for z in range(n)] for y in range(n)]  
	return cube
	

#pad message to fit the cube
#n is the length of a side of the cube
def pad(message, n) :
	block = n * n * 6
	padLength = block - (len(message) % block)
	for x in range(padLength) :
		message += alphabet[x % len(alphabet)]
	return message
	
	
#format the message. all uppercase, replace numbers
def format(message) :
	message = replaceNumbers(message)
	message = replaceOthers(message)
	message = message.upper()
	return message


#replace numbers with their written equivalent
def replaceNumbers(message) :
	message = message.replace("0", "zero")
	message = message.replace("1", "one")
	message = message.replace("2", "two")
	message = message.replace("3", "three")
	message = message.replace("4", "four")
	message = message.replace("5", "five")
	message = message.replace("6", "six")
	message = message.replace("7", "seven")
	message = message.replace("8", "eight")
	message = message.replace("9", "nine")
	return message


#removes all non-alphabetical characters
def replaceOthers(message) :
	message = list(message)
	for x in range(len(message)) :
		if not (65 <= ord(message[x]) <= 90 or 97 <= ord(message[x]) <= 122) :
			message[x] = ""
	return "".join(message)


#puts a block of the message into the cube
def fillCube(block, cube) :
	n = len(cube[0])
	for x in range(len(block)) :
		face = (int) (x / (n * n))
		row = (int) ((x / n) % n)  
		col = x % n
		cube[face][row][col] = block[x]
	return cube


#takes a filled cube and applies rotations according to the key
def encipher(cube, key) :
	for x in key :
		cube = rotate(cube, abs(x), (x / abs(x)))
	return cube


#performs a rotation
#op is the operation (which column to rotate), dir is the direction (true is up/right, false is down/left)
def rotate(cube, op, dir) :
	front = cube[0]; up = cube[1]; back = cube[2]; down = cube[3]; left = cube[4]; right = cube[5]
	n = len(cube[0])
	#faces involved in each type of rotation
	set1 = [front, up, back, down]
	set2 = [front, right, back, left]
	set3 = [up, left, down, right]
	set = []
	#ops 1 to n are set1, (n+1) to 2n are set2, (2n+1) to 3n are set3
	if op <= n : 
		set = set1
	elif op <= 2 * n :
		set = set2
	else :
		set = set3
	
	#transpose for easy computing
	if not (n < op <= 2 * n) :
		for x in range(len(set)) :
			set[x] = zip(*set[x])
	
	#perform rotation
	row = (op - 1) % n
	bigTemp = deepcopy(set[0][row])
	count = 0; x = 0
	while count < len(set) :
		y = (x + dir) % len(set)
		next = set[y][row]
		tinyTemp = deepcopy(next)
		set[y][row] = deepcopy(bigTemp)
		bigTemp = deepcopy(tinyTemp)
		x = y
		count += 1
		
	#transpose back
	if not (n < op <= 2 * n) :
		for x in range(len(set)) :
			set[x] = zip(*set[x])
			#set as a list
			for y in range(len(set[x])) :
				set[x][y] = list(set[x][y])
		#associate the set with the cube
		if op <= n :
			cube[0] = set[0]
			cube[1] = set[1]
			cube[2] = set[2]
			cube[3] = set[3]
		elif op > 2 * n :
			cube[1] = set[0]
			cube[4] = set[1]
			cube[3] = set[2]
			cube[5] = set[3]
	
	return cube
	

#transforms the cube into a string
def toString(cube) :
	s = ""
	for x in range(len(cube)) :
		for y in range(len(cube[0])) :
			s += "".join(cube[x][y])
	return s
	
	
#prints each face of the cube in an easier to read format
#only used for testing	
def printCube(cube, set) :
	#helper for printCube
	def printFace(face) :
		for y in range(len(face)) :
			print face[y]
			print
		print
		
	if set == 1 :
		for x in range(6) :
			printFace(cube[x])
	elif set == 2 :
		printFace(cube[0])
		printFace(cube[5])
		printFace(cube[2])
		printFace(cube[4])
		printFace(cube[1])
		printFace(cube[3])
	elif set == 3 :
		printFace(cube[1])
		printFace(cube[4])
		printFace(cube[3])
		printFace(cube[5])
		printFace(cube[0])
		printFace(cube[2])
	
	
def main() :
	
	#parser for command line arguments
	parser = argparse.ArgumentParser(description = "Rubiks cube transposition cipher")
	parser.add_argument("key", nargs = "+", type = int,  help = "KEY is the encryption / decryption key for the message")
	parser.add_argument("-n", "--n", nargs = "?", type = int, default = 3, help = "use an NxN cube. Default is 3")
	parser.add_argument("-i", "-in", "--input", nargs = "?", type = argparse.FileType("r"), default = sys.stdin, help = "Read text from INPUT. Default is stdin")
	parser.add_argument("-o", "-out", "--output", nargs = "?", type = argparse.FileType("w"), default = sys.stdout, help = "Write text to OUTPUT. Default is stdout")
	args = parser.parse_args()
	
	#check for valid size (N)
	if args.n < 1 :
		print "Error: size must be at least 1"
		exit()
	
	#check for valid key
	for x in args.key :
		if abs(x) > 3 * args.n :
			print "Error: key must not contain an integer whose absolute value greater than 3 * n"
			exit()
	
	#read input
	if args.input == sys.stdin :
		args.input = format(raw_input("Please enter a message: "))
	else :
		args.input = format(args.input.read())
	
	blockSize = args.n * args.n * 6
	cube = createCube(args.n)
	
	#perform encryption 
	while len(args.input) > 0 :
		if len(args.input) >= blockSize :
			block = args.input[:blockSize]
			args.input = args.input[blockSize:]
			cube = fillCube(block,cube)
			args.output.write(toString(encipher(fillCube(block, cube), args.key)) + "\n")
		else :
			block = args.input
			args.input = ""
			block = pad(block, args.n)
			args.output.write(toString(encipher(fillCube(block, cube), args.key)) + "\n")
	

	
main()

