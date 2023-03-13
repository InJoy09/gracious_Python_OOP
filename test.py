
n = 70304
n_lst = list(str(n))
print(n_lst)
for i in range(len(n_lst)):
	el = n_lst[i]
	print(el + ('0' * len(n_lst[i + 1:])))