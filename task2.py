# list_range = [num ** 2 for num in range(1, 20)]
# print(list_range)

matrix = [
    [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]
]
# new_list = [x for row in matrix for x in row]
test = [[y ** 2 for y in x] for x in matrix]
print(test)
