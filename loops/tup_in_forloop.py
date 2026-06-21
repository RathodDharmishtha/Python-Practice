tup = (1, 4, 9, 16, 25, 36, 49, 64, 49, 81, 100)

x = 49
indx = 0

for el in tup:
    if el == x:
        print("number found at indx", indx)

    indx += 1