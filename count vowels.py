vowels = ['a','e','i','o','u']
sinput = input('What is your word? ').lower()
cvt = []
x = []
counter = 0
for a in sinput:
	cvt.append(a)
for a in vowels:
	for ab in cvt:
		if ab == a:
			x.append(ab)
			counter+=1
print(f'The number of vowels in the word is {counter}')
print(x)