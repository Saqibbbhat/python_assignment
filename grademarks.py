math=float(input("Enter your math score: "))
english=float(input("Enter your english score: "))
urdu=float(input("Enter your urdu score: "))
sst=float(input("Enter your sst score: "))
science=float(input("Enter your science score: "))

total_marks=math+english+urdu+sst+science

percent=total_marks/500*100

if percent>=90:
    grade="A"
if percent>=80:
    grade="B"
if percent>=70:
    grade="C"
if percent>=60:
    grade="D"
if percent>=50:
    grade="E"
else:
    grade="F"
print("Your grade is ",grade)

