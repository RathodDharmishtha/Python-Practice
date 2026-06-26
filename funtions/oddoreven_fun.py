def check_odd_even(num):
    if num % 2 == 0:
        print(num, "Even hai")
    else:
        print(num, "Odd hai")

# User se input lena
n = int(input("Number enter karo: "))
check_odd_even(n)