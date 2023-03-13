
def calculate_num(q):
	res = 0
	lst1 = ['ноль', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
	lst2 = ['', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать',
	        'восемнадцать', 'девятнадцать']
	lst3 = ['', 'десять', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят',
	        'девяносто']
	lst4 = ['', 'сто', 'двести', 'триста', 'четыреста', 'пятьсот', 'шестьсот', 'семьсот', 'восемьсот', 'девятьсот']
	for el in q:
		if el in lst3:
			res += lst3.index(el) * 10
		elif el in lst1:
			res += lst1.index(el)
		elif el in lst4:
			res += lst4.index(el) * 100
		elif el in lst2:
			res += lst2.index(el) + 10
	
	return res


s = 'двадцать три тысячи девятьсот девятнадцать'
s = 'двести сорок шесть'
s = 'двадцать три тысячи девятнадцать'
result = 0

if 'тысяч' in s:
	x = s.split('тысяч')
	z1 = x[0].split()
	z2 = x[1].split()
	result += calculate_num(z1) * 1000
else:
	z2 = s.split()

result += calculate_num(z2)
	
print(result)



