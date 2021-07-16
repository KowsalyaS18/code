def findFourElements(list1, n, target):
	temp = {}
	for i in range(n - 1):
		for j in range(i + 1, n):
			temp[list1[i] + list1[j]] = [i, j]

	for i in range(n - 1):
		for j in range(i + 1, n):
			sum = list1[i] + list1[j]
			if (target - sum) in temp:
				p = temp[target - sum]
				if (p[0] != i and p[0] != j and p[1] != i and p[1] != j):
					print(list1[i], ", ", list1[j], ", ",
						list1[p[0]], ", ", list1[p[1]], sep="")
					return
list1 = [10, 20, 30, 40, 1, 2]
n = len(list1)
target = 91

findFourElements(list1, n, target)
