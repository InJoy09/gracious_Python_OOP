
dict_ = {}
for i in range(10):
	dict_[str(i)] = i

# dict_['7'] = 8
last_v = -1

for k, v in dict_.items():
	if v != last_v + 1:
		print('Alarm !!!!', k, v)
	last_v = v
	