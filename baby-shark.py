for w in"Baby,Mommy,Daddy,Grandma,Grandpa,Let's go hunt,Run away,Safe at last,It's the end".split(','):
	if len(w)<8:
		w+=" shark";
	print(w+","+" doo"*6+"\n")*3+w+"!"
