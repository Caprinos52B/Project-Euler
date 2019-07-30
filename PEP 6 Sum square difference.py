numList = []

def CreateNumList():
	for i in range(1, 100 + 1):
		numList.append(i)
	#numList == [1, 2, ... ,100]
	
def SquareOfSum():
	SOS = long(0)	#square of sum
	for i in range(0, len(numList)):
		SOS = SOS + numList[i]
	SOS = SOS * SOS
	return SOS
	
def SumOfSquare():
	SOS = long(0)
	for i in range(0, len(numList)):
		SOS = SOS + (numList[i] * numList[i])
	return SOS
	
def main():
	SSD = long(0)	#Sum Square Difference
	CreateNumList()
	SSD = SquareOfSum() - SumOfSquare()
	print("The difference between the sum of the squares of the first 100 natural numbers and the square of the sum is {}".format(SSD))
	
main()
