import random
ladder = {4:10, 9:21, 20:18, 28:56, 40:19, 51:16, 63:18, 71:20}
snakes = {17:10,54:20, 62:43, 64:4, 87:63, 93:20, 95:20, 99:21}
position = 0
def roll():
	global position
	p1 = random.randint(1,6)
	print('+', p1, end=' ')
	position+=p1
	gamestate()
def check_l():
	for a in ladder:
		global position
		if position == a:
			position+= ladder[a]
			print('found a ladder! +',ladder[a])
			break
	check_s()
def check_s():
	for a in snakes:
		global position
		if position == a:
			position-=snakes[a]
			print('snekkk hehe! -', snakes[a])
			break
	roll()
def gamestate():
	if position < 100:
		print('The player is at',position)
		input()
		check_l()
	else:
		print('Game Won!')
roll()
