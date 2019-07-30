sumOfMultiples = 0

def main():
	for i in range(0, 1000):
		global sumOfMultiples
		if(i % 3 == 0):
			sumOfMultiples = sumOfMultiples + i
		elif(i % 5 == 0):
			sumOfMultiples = sumOfMultiples + i
	print("The sum of all the multiples of 3 or 5 below 1000 is {}".format(sumOfMultiples))
		
main()
