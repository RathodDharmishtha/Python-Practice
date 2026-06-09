a=int(input("Enter value of a : "))
b=int(input("Enter value of b : "))
c=int(input("Enter value of c : "))
d=int(input("Enter value of d : "))

if(a>=b and a>=c and a>=d ):
    print("First number is largest : ", a)
elif(b>=c and b>=d):
    print("Second number is largest : ", b)
elif(c>=d):
    print("Third number is largest : ",c)

else:
    print("Fourth number is largest : ",d)
