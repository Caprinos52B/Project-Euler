num = ""
maxNum = ""
numString = ""
maxProduct = 1

def getNum():	
	global num, maxProduct, numString
	infile = open("PEP8.txt", "r")
	for line in infile:
		num = num + line.strip()	#strip trailing new line character or space
#	print(num)
	numString = num[0 : 13]
	for i in range(0 , 13):
		maxProduct = maxProduct * int(numString[i])

def checkProduct(number):
	global maxProduct, maxNum
	product = 1
	for i in range(0, len(number)):
		product = product * int(number[i])
	if maxProduct < product:      
		maxNum = number
		maxProduct = product

def main():
	global numString, maxNum, maxProduct
	number = ""
	getNum()
	for i in range(1, len(num) - 13):
		number = num[i : i + 13]
		checkProduct(number)
	print("The thirteen adjacent digits in the 1000-digit number that have the greatest product is {} \nThe value of this product is {}".format(maxNum, maxProduct))

main()
