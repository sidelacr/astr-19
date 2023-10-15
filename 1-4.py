import sys

# decalre class describing favorite animal
class Animal:

	def print(self):
		print('My favorite animal are Cats!')
		print(f'Length of legs = {self.num_sides} inches')
		print(f'Length of arms = {self.side_length} inches')
		print(f'Number of eyes = {self.num_eyes}')
		print('Does it have a tail?')
		print(bool("tail"))
		print('Is it furry?')
		print(bool("furry"))

# physcial parameters of the animal 
	def __init__(self,feet=7.1, arm=6.5, eyes=2 ):
		self.num_sides  = feet
		self.side_length = arm
		self.num_eyes = eyes

def main():
# set values of data when class is created

	feet = 7.1	#float point number
	arm = 6.5	#float point number
	eyes = 2	#integer 

	if(len(sys.argv)>=2):
		feet = float(sys.argv[1])

	if(len(sys.argv)>=3):
		arm = float(sys.argv[2])

	if(len(sys.argv)>=2):
		eyes = int(sys.argv[1])

	our_animal = Animal(arm=arm,feet=feet, eyes=eyes)

	our_animal.print()

if __name__=="__main__":
	main()