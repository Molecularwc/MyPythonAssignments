## Richard Salvaty
## 3002
## 10/12/2018
## 10 minutes
## Hw8 Q2

newNum = 'y'
## This will begin the loop
while newNum == 'y':
    num = int(input("Please enter the number to be checked: "))
## This determines if the number is even or odd
    if num % 2 == 0:
        print("The number you entered is an even number." )
    else:
        print("The number you entered is an odd number. ")
## Asks if the user wants to check another number
    newNum = input("Would you like to check another number? Y/N: ")
