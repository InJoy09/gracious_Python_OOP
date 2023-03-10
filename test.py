
dict_ = {}
for i in range(10):
	dict_[str(i)] = i

# dict_['7'] = 8
last_v = 0

for k, v in dict_.items():
	if last_v == 0:
		continue
	if v != last_v + 1:
		print('Alarm !!!!', k, v)
	last_v = v
	