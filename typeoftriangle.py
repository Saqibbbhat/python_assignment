s1=int(input("Enter the length of side 1:"))
s2=int(input("Enter the length of side 2:"))
s3=int(input("Enter the length of side 3:"))

if s1==s2==s3:
    print("equilateral triangle")
elif s1==s2 or s2==s3:
    print("isosceles triangle")
else:
    print("scalene triangle")