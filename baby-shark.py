for w in"Baby,Mommy,Daddy,Grandma,Grandpa,Let's go hunt,Run away,Safe at last,It's the end".split(','):
	w+=(" shark",'')[len(w)>7]
	print(w+","+" doo"*6+"\n")*3+w+"!"
