def most_fr_char(string):
	occurrence = 0
	letter = ''
	for c in string:
		count = string.count(c)
		if count > occurrence:
			occurrence = count
			letter = c
	return letter

print most_fr_char('bobobob')