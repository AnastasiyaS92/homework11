my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
y = my_list
x = 0
while x < len(y):
    a = y[x]
    x = x + 1
    if a == 0:
        continue
    elif a < 0:
        break
    else:
        print(a)





