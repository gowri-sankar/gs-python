n1 = 0
n2 = 1
n3 = 0
g1 = 0
def even_fib():
	global n1,n2,n3,g1
	for i in range(1,100):
		n3 = n1 + n2
		n1 = n2
		n2 = n3
		if n3 % 2 == 0:
				g1 = g1 + n3
		if n3 >= 4000000:
			break
even_fib()
print(g1)