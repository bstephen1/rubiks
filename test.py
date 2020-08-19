#rubiks cube cipher tests
import os


#run through a few cube sizes. eN.txt is output for enciphering an NxN cube, dN.txt is deciphering
#1x1
os.system('python rubiks.py -iinput.txt -oe1.txt -n1 1 2 3')
os.system('python rubiks.py -ie1.txt -od1.txt -n1 -3 -2 -1')
#3x3
os.system('python rubiks.py -iinput.txt -oe3.txt 1 2 3 4 5 6 7 8 9 ')
os.system('python rubiks.py -ie3.txt -od3.txt -9 -8 -7 -6 -5 -4 -3 -2 -1')
#5x5
os.system('python rubiks.py -iinput.txt -oe5.txt -n5 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 ')
os.system('python rubiks.py -ie5.txt -od5.txt -n5 -15 -14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1')
#20x20
os.system('python rubiks.py -iinput.txt -oe20.txt -n20 1 5 10 15 20 25 30 35 40 45 50 55 60')
os.system('python rubiks.py -ie20.txt -od20.txt -n20 -60 -55 -50 -45 -40 -35 -30 -25 -20 -15 -10 -5 -1')
#3x3 alternate
os.system('python rubiks.py -iinput.txt -oe3b.txt 1 4 2 5 4 8 2 -4 -7 4 5 8 1 -7 -2 1 -8 -3 -2 -5 4 9 8 2 1 -5 -6 9 1 -9 -4 7 2 1 5 8 -2 -2 -4 5')
os.system('python rubiks.py -ie3b.txt -od3b.txt -5 4 2 2 -8 -5 -1 -2 -7 4 9 -1 -9 6 5 -1 -2 -8 -9 -4 5 2 3 8 -1 2 7 -1 -8 -5 -4 7 4 -2 -8 -4 -5 -2 -4 -1')