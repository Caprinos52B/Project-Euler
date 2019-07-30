def main():
	newFib = 2
	oldFib = 1
	tempFib = 0
	fibSum = 0
	while newFib <= 4000000:
		if newFib % 2 == 0:
			fibSum = fibSum + newFib
		tempFib = newFib
		newFib = oldFib + newFib
		oldFib = tempFib
	print("The sum of the even-valued terms in the Fibonaci sequence is {}".format(fibSum))

main()
