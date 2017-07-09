def add():
	return x + y
def sub():
	return x - y
def div():
	return x / y
def mul():
	return x * y

print('Welcome to simple calculator')
print('What would you like to do?')
print('+ - / * ?')
choice = input('> ')
print('Okay. Enter number 1')
x = int(input())
print('Enter number 2')
y = int(input())
if choice == '+':
	print(add())
elif choice == '-':
	print(sub())
elif choice == '/':
	print(div())
elif choice == '*':
	print(mul())
else:
	print('Invalid Entry!') 