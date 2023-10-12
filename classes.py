#define a class with an initialize
#set og parameters

#import sys
import sys

class Shape:

	#a class for geometric shapes

	def print(self):
		print('Here is our shape!')
		print(f'Number of sides = {self.num_sides}')
		print(f'Length of sides = {self.side_length}')

	def __init__(self,nsides=3,length=1.):
		self.num_sides  = nsides
		self.side_length = length

def main():

	#set default numebr of sides
	#and length
	nsides = 3
	length = 10

	#if there are at least 2 command
	#line arguments, set nsides equal
	#to the seocnd
	if(len(sys.argv)>=2):
		nsides = int(sys.argv[1])

	#if there are command line
	#arguments, set length equal 
	#to the third
	if(len(sys.argv)>=3):
		length = float(sys.argv[2])

	#initialize our shape
	our_shape = Shape(nsides=nsides,length=length)

	#print out information about
	#our shape
	our_shape.print()

#run our program
if __name__=="__main__":
	main()