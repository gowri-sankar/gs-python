import random
number = 0
def roll():
	global number 
	number = random.randint(1,6)
	return number
print('Press enter to roll dice or press q to quit')
while True:
	controller = input('')
	if controller == 'q':
		break
	print('> ' + str(roll()))