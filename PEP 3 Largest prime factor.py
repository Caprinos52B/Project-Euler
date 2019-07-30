import math

def main():
	constant = 600851475143
	number = constant
	LPF = 1			#Largest Prime Factor
	LPFfound = 0	#Largest Prime Factor not found
	primeFactor = 3

	while (primeFactor <= int(math.sqrt(number))) or LPFfound == 0:
		if number % primeFactor == 0:				#finding the factor of constant
			if primeFactor > LPF:
				LPF = primeFactor
				number = number / primeFactor
			if number == 1:
				LPFfound = 1
		primeFactor = primeFactor + 2
		
	print("The largest prime factor of {} is {}".format(constant, LPF))

main()
