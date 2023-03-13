
n = 70304
n_lst = list(str(n))
print(n_lst)
res = ''
for i in range(len(n_lst)):
	el = n_lst[i]
	if el != '0':
		res += el + ('0' * len(n_lst[i + 1:])) + ' + '
print(res[:-2])