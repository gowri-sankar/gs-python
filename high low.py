import random
attempts = 0
digs = [None,1,10,100,1000,10000]
print('Choose your digit size (Max 5)')
size = int(input('> '))
findthis = random.randint(1,digs[size])
while True:
	userinput = int(input('> '))
	if userinput > findthis: 
		print('High')
		attempts+=1
	elif userinput < findthis:
		print('Low')
		attempts+=1
	else:
		print('You guessed it! in ' + str(attempts) + ' attempts')
		break
