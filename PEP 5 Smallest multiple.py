factorList = []

def createFactorList():
	commonFactorList = []
	factor = 2
	largestNum = 20
	while largestNum > 1:
		for i in range(2, 20 + 1):	#create a list of common factors from 1 to 20
			if largestNum % i == 0 and i not in factorList and i != largestNum:		
				commonFactorList.append(i)
		largestNum = largestNum - 1
	for i in range(2, 20):			#create a list of non common factors from 1 to 20 not including 20 
		if i not in commonFactorList:
			factorList.append(i)
	#factorList == [11, 12, 13, 14, 15, 16, 17, 18, 19]

def checkDivisible(num):
	divisible = 0	
	for i in range(0, len(factorList)):
		if num % factorList[i] == 0:
			divisible = divisible + 1
	if divisible == len(factorList):
		return 1
	return 0	

def main():
	LCMfound = 0
	CM = 0	#Common Multiple
	largestFactor = 20
	multiplier = 1
	createFactorList()
	while LCMfound == 0:
		CM = largestFactor * multiplier
		if checkDivisible(CM) == 0:		#CM not divisble by 1 to 20
			multiplier = multiplier + 1
		else:							#CM divisible by 1 to 20
			LCMfound = 1

	print("The smallest multiple that is evenly divisble by all numbers from 1 to 20 is {}".format(CM))
		
main()
