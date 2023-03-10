
dict_ = {}
for i in range(10):
	dict_[str(i)] = i

dict_['7'] = 8

for k, v in dict_.items():
	if v == 9:
		continue
	if v + 1 != dict_[str(v + 1)]:
		print('Alarm !!!!')
	