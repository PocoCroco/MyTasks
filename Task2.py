lst = [10, 500, 54, 32, 32, 32, 5, 34, 56, 180, 200, 90, 4, 10, 8, 60, 30]
new_lst = [lst[el] for el in range(1, len(lst)) if lst[el] > lst[el-1]]
print(new_lst)