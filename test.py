
s = "    Hello     world   ".split()
h = '#'
for el in s:
	h += el.title()
res = False if len(h) > 140 or h == '#' else h
