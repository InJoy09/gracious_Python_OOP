
s = 'recede'
res = ''
for ch in s:
	res += '(' if s.count(ch) == 1 else ')'
	
print(res)

