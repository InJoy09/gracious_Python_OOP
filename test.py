
def rgb_to_hex(rgb):
	res = ''
	lst = rgb.split(', ')
	for el in lst:
		h = hex(int(el)).upper()
		res += h[2:] if len(h) == 4 else '0' + h[2:]
	print(res)


rgb_to_hex('14, 15, 128')

