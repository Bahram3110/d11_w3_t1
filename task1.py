
list1 = [num for num in range(0,100, 2)]# 1 способ
print(list1)



list2 = range(1, 100)# 2 способ
list3 = [num for num in list2 if num % 2 == 0]
print(list3)
