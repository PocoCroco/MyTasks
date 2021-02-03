lst = [6, 12, 5, 5, 4, 45, 76, 8, 8, 4, 12, 130, 200, 34]
new_lst = [el for el in lst if lst.count(el) == 1]
print(new_lst)