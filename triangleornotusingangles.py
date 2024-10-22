# Input the angles of the triangle
angle1 = float(input("Enter the first angle: "))
angle2 = float(input("Enter the second angle: "))
angle3 = float(input("Enter the third angle: "))

# Check if the angles form a valid triangle
if angle1 + angle2 + angle3 == 180 and angle1 > 0 and angle2 > 0 and angle3 > 0:
    print("The angles form a valid triangle.")
else:
    print("The angles do not form a valid triangle.")
