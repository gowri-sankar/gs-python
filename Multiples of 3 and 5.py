result3 = 0
result5 = 0
common = 0
def multiples3():
	global result3
	for x in range(1,1000):
		if x % 3 == 0:
			result3 = result3 + x

def multiples5():
	global result5
	for x in range(1,1000):
		if x % 5 == 0:
			result5 = result5 + x

def del_common():
	global common
	for x in range(1,1000):
		if x % 15 == 0:
			common = common + x
multiples3()
multiples5()
del_common()
print(result3 + result5 - common)