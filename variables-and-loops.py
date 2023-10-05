import numpy as np		#we use numpy for lots of things

def main():
	i = 0		#integers can be decleared with a number 
	n = 10 		#here is anotehr integer 
	x = 19.0	#floating point numbers are declared with a " "

	#we can use numpy to declare arrays quickly 

	y = np.zeros(n,dtype=float) #declares 10 zeros as flaots using np 

	#we can use for loops to iterate with a varibale 

	for i in range(n):
		y[i] = 2.0 * float(i) + 1 		#set y = 2i+1 as flaots 

	for y_element in y:
		print(y_element)

if __name__ == "__main__":
	main()