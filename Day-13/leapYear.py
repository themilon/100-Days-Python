year = int(input("Which year do you want to check?"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a Leap year.")
        else:
            print(f"{year} is Not a leap year.")
    else:
        print(f"{year} is a Leap year.")
else:
    print(f"{year} is Not a leap year.")
