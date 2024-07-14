n = int(input("Enter a year:"))
if n%4 == 0 and n%100 != 0:
    print("Yes!",n,"is a leap year")
else:
    print("No!",n,"is not a leap year")
