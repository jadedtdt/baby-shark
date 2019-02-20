s = ["Baby", "Mommy", "Daddy", "Grandma", "Grandpa", "Let's go hunt", "Run away", "Safe at last", "It's the end"]
for i in range(0, 9):
	b = s[i] + ' shark' if i < 5 else s[i]
	for j in range(1, 4):
		a = 'doo'
		for k in range(1, 6):
			a += str(' doo')
		print b + ', ' + a
	print b + '!'
