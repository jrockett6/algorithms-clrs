def insertion_sort(mylist):
	for j in range(1, len(mylist)):
		key = mylist[j]

		i = j - 1
		while i >= 0 and mylist[i] > key:
			mylist[i + 1] = mylist[i]
			i -= 1

		mylist[i+1] = key

	return mylist