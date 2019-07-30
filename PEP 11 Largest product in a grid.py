numArray = ""	#will become list in createNumArray
rightDiagInt = 21
leftDiagInt = 19
vertInt = 20
horizInt = 1
numLength = 4
maxProduct = 1
infile = open("PEP 11.txt", "r")

def createNumArray():
	global numArray
	numString = ""
	for line in infile:
	#no space at the end of line because it's stripped
		numArray = numArray + line.strip() + " "
	#apply split to str then "listify" numArray
	numArray = list(numArray.split())	
#	print(type(numArray))

def checkHorizontal():
	global numArray, infile, horizInt, maxProduct, numLength
	for num in range(0, len(numArray) - numLength + 1):
		product = 1
		for i in range(num, num + numLength, horizInt):
#			print(numArray[i])
			product = product * int(numArray[i])
			if product > maxProduct:
				maxProduct = product		
#	print(maxProduct)

def checkVertical():
	global numArray, infile, vertInt, maxProduct, numLength
	for num in range(0, len(numArray) - (vertInt * 3)):
		product = 1
		for i in range(num, num + numLength * vertInt, vertInt):
#			print(numArray[i])
			product = product * int(numArray[i])
		if product > maxProduct:
			maxProduct = product		
#	print(maxProduct)

def checkRightDiagonal():
	global numArray, infile, rightDiagInt, maxProduct, numLength
	for num in range(0, len(numArray) - (rightDiagInt * 3)):
		product = 1
		for i in range(num, num + numLength * rightDiagInt, rightDiagInt):
#			print(numArray[i])
			product = product * int(numArray[i])
		if product > maxProduct:
			maxProduct = product		
#	print(maxProduct)

def checkLeftDiagonal():
	global numArray, infile, leftDiagInt, maxProduct, numLength
	for num in range(0, len(numArray) - (vertInt * 3)):
		product = 1
		for i in range(num, num + numLength * leftDiagInt, leftDiagInt):
#			print(numArray[i])
			product = product * int(numArray[i])
		if product > maxProduct:
			maxProduct = product		
#	print(maxProduct)

def main():
	global maxProduct
	createNumArray()
	checkHorizontal()
	checkVertical()
	checkRightDiagonal()
	checkLeftDiagonal()
	print("The greatest product of 4 adjacent numbers in the same direction in the 20 x 20 grid is {}".format(maxProduct))

main()
