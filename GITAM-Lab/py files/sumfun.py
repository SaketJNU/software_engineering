def sum2(f,s):
	return f+s

def output():
	fn = float(input("input the first number: " ))
	sn =  float(input("input the second number: " ))
	print("the required sum is {}". format(sum2(fn,sn)))
	return

if __name__ == '__main__':
	output()