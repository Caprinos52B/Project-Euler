import math
upperLimit = 2000000
primeList = [2]
nonPrimeList = []

def markPrime():
	global upperLimit, primeList
#	print(math.ceil(math.sqrt(upperLimit)))
	for num in range(3, int(math.ceil(math.sqrt(upperLimit))) + 1):		#mark all prime below sqrt of upperLimit
#	for num in range(3, upperLimit):	
		numOfFactor = 0		#flag to identify primes
		if num not in primeList and num < upperLimit:
			for j in range(0, len(primeList)):
				if num % primeList[j] == 0:
					numOfFactor = numOfFactor + 1
			if numOfFactor == 0:
				primeList.append(num)
#	print(primeList)

def markNonPrime():
	global upperLimit, primeList, nonPrimeList
	number = 0
	for i in range(0, len(primeList)):
		multiplierLimit = (upperLimit / primeList[i]) + 1
#		print(multiplierLimit)	
		#so that multiplier * element in primeList always < upperLimit
		for multiplier in range(2, multiplierLimit):
			number = multiplier * primeList[i]	#multiples of prime
			if number < upperLimit:
				nonPrimeList.append(number)		#mark multiples of prime
	nonPrimeList = list(set(nonPrimeList))		#only include unique elements in nonPrimeList
#	print(nonPrimeList[-1])

def main():
	global upperLimit, primeList, nonPrimeList
	sumOfAll= 0
	sumOfNonPrime = 0
	markPrime()
	markNonPrime()
#	for num in range(primeList[-1] + 1, upperLimit):
#		if num not in nonPrimeList:
#			primeList.append(num)
#			print(num)
	sumOfNonPrime = sum(nonPrimeList)
	for i in range(2, upperLimit):
		sumOfAll = sumOfAll + long(i)
	print("The sum of all the primes below {} is {}".format(upperLimit, sumOfAll - sumOfNonPrime))
	
main()
