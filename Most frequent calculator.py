a= 1, 3, 5, 3, 5, 6, 2, 4, 6, 8, 7, 5, 6, 4, 3, 7, 8, 9, 5, 3, 1, 3, 4, 3, 2, 5, 4, 6, 5, 7, 8, 9, 5, 4, 5, 7, 3, 6, 5,7, 8,6, 5 ,7, 7,8
x = max(a, key=a.count)
b = a.count(x)
print(f'Most frequently used number is {x}. It is used {b} times')
