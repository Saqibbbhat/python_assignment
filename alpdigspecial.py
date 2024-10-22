char = input("Enter a character: ")

if ('a' <= char <= 'z') or ('A' <= char <= 'Z'):
    print("It is an alphabet.")
elif ('0' <= char <= '99999999'):
    print("It is a digit.")
else:
    print("It is a special character.")