
lst = [-1, 0, 1, 2, 3]

res = all([i == lst[lst.index(i) + 1] + 1 for i in lst[:-1]])
res = [i == lst[lst.index(i) + 1] + 1 for i in lst[:-1]]
print(res)

# print(lst[lst.index(-1)])
print(lst[lst.index(-1) + 1])