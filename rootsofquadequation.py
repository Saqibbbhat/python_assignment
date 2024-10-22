a=int(input("Enter a : "))
b=int(input("Enter b : "))
c=int(input("Enter c : "))

d=(b*b)-(4*a*c)
root1=-b+(d/2*a)**1/2
root2=-b(d/2*a)**1/2

if d>0:
    print("the equation has 2 distinct real roots",root1,root2)
elif d==0:
    print("the equation has 1 real roots",root1)

else:
    print("the equation has 2 complex  roots",root1,root2)