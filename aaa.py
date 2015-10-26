text = 'Winter in Boston!'
word = 'Boston'


text = text.lower()
replace_chars = ".,!?'"
for char in replace_chars:
	text = text.replace(char, ' ')
for item in text.split(' '):
	print item
	if item == word.lower():
		print 'pwe'