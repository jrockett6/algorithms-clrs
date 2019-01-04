import math

def merge_sort(mylist):
	mylist = merge_sort_rec(mylist, 0, len(mylist) - 1)
	return mylist

def merge_sort_rec(mylist, left, right):
	if left < right:
		mid = int((left + right)/2)
		merge_sort_rec(mylist, left, mid)
		merge_sort_rec(mylist, mid + 1, right)
		mylist = merge(mylist, left, mid, right)
		return mylist

def merge(mylist, left, mid, right):
	lleft = mid - left + 1
	lright = right - mid
	L = []
	R = []

	[L.append(mylist[left + i]) for i in range(lleft)]
	[R.append(mylist[mid + 1 + i]) for i in range(lright)]
	L.append(math.inf)
	R.append(math.inf)

	i = 0
	j = 0

	for iterat in range(left, right + 1):
		if L[i] <= R[j]:
			mylist[iterat] = L[i]
			i += 1
		else:
			mylist[iterat] = R[j]
			j += 1

	# Print statements to watch merge sort work
	# print(L)
	# print(R)
	# print(mylist[left:right + 1])
	# print()

	return mylist
