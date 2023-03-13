
n = 70304
n_lst = list(str(n))
print(n_lst)
res = ''
for ch in n_lst:
	if ch != '0':
		res += ch + ((len(n_lst) - n_lst.index(ch) - 1) * '0') + ' + '
print(res[:-2])