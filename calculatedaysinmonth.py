#Days in the month

january=1
febuary=2
march=3
april=4
may=5
june=6
july=7
august=8
september=9
october=10
november=11
december=12

month=int(input("Enter the Month No:"))

if month==1:
    print("There are 31 days in the First Month;January")
elif month==2:
    print("There are 28 days in the 2nd Month;Febuary")
elif month==3:
    print("There are 31 days in the 3rd Month;March")
elif month==4:
    print("There are 30 days in the 4th Month;April")
elif month==5:
    print("There are 31 days in the 5th Month;May")
elif month==6:
    print("There are 30 days in the 6th Month;June")
elif month==7:
    print("There are 31 days in the 7th Month;July")
elif month==8:
    print("There are 31 days in the 8th Month;August")
elif month==9:
    print("There are 30 days in the 9th Month;September")
elif month==10:
    print("There are 31 days in the 10th Month;October")
elif month==11:
    print("There are 30 days in the 11th Month;November")
elif month==12:
    print("There are 31 days in the 12th month;December")
else:
    print("Invalid Month")