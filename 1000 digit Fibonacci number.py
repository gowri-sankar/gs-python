n1 = 0
n2 = 1
n3 = 0
g1 = 0
counter = 1
def even_fib():
	global n1,n2,n3,g1,counter
	for i in range(1,10000):
		counter+= 1
		n3 = n1 + n2
		n1 = n2
		n2 = n3
		if len(str(n3)) == 1000:
			break
even_fib()
print('The first term in the Fibonacci sequence to contain 1000 digits is ' + str(counter))
