def checkPalindrome(number):
	target = str(number)			#convert number to string
	reverseTarget = str(target[::-1])	#reverse target
	if target == reverseTarget:
		#print(reverseTarget)
		return 1
	return 0
	
def main():
	largestPalindrome = 0
	for factor1 in range(100, 1000):
		for factor2 in range(100, 1000):
			product = factor1 * factor2
			if checkPalindrome(product) == 1 and product > largestPalindrome:
				largestPalindrome = product
	
	print("The largest palindrome made from the product of two 3-digit numbers is {}".format(largestPalindrome))

main()
