def main():
	a = 0
	b = 0
	c = 0
	solved = 0
	product = 0
	while solved == 0:
		for i in range(998, 0, -1):
			c = i
			for j in range(1, 998):
				a = j
				b = 1000 - c - a
				if b > 1 and b > a and b < c:
					
					if (a * a + b * b == c * c):			
						product = a * b * c
						solved = 1
	print("The Pythagorean triplet for which a + b + c = 1000 is {}, {}, {} \n The product abc is {}".format(a, b, c, product))

main()
