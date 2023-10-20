#write a a table funciton sin(x) vs x
#x is tabulated between 0 and 2pi with thousand enteries

import numpy as np 
from astropy.table import Table #import table class
from astropy.io import ascii #ascii text
from astropy.io import fits #fits fromat to io

def main():

	x = np.linspace(0, 2*np.pi, 1000) #data array for x
	y = np.sin(x) #data array for sin(x)

	data = Table([x,y],names=["x","sin(x)"]) #creates the table
	ascii.write(data, 'table-1-5.txt', format='commented_header') #table to file
	data_in = ascii.read('table-1-5.txt') #reads the data
	print(data_in)

if __name__=="__main__":
	main()
