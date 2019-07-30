primeList = [2]

def checkPrime(num):
	if num % 2 == 0:	#even number
		return 0
	else:
		for i in range(0, len(primeList)):
			if num % primeList[i] == 0:	#check if elements in primeList is a factor
				return 0
		return 1


def main():
	primeCount = 1
	num = 3
	while primeCount < 10001:	#from 2nd to 10001st prime
		while checkPrime(num) != 1:
			num = num + 1
		primeCount = primeCount + 1
		primeList.append(num)
	print("The 100001st prime number is {}".format(num))

main()
