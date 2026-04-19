
while True:
    user =input("Enter year: (or end for stop)")
    if user.lower() == 'stop':
        break

    year = int(user)
    
    if (year %4==0 and year %100 !=0 )or (year %400==0):
        print("Leap Year")
    else:
        print("Not Leap Year")