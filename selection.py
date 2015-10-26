l = [144, 66, 777, 44, 1, 5, 7, 8, 9, 0, 22, -500]

def selection_sort(l):
	for t in range(len(l)):
		minimum = l[t]
		swap_pos = t
		for i in range(len(l)):
			if l[i] < minimum and i >= t:
				minimum = l[i]
				swap_pos = i
		l[swap_pos] = l[t]
		l[t] = minimum
	return l

# def insertion_sort(l):
# 	pass

# for i in range(len(l)):
# 	item = l[i]
# 	for t in range(i):
# 		if l[t] > item:
			



print selection_sort(l)



