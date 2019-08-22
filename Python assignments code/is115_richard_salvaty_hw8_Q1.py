## Richard Salvaty
## 3002
## 10/12/2018
## 1 hour
## HW8 Q1
least = 0
mid = 0
great = 0
again = 'y'

## This begins the loop process
while again == 'y':
    num1 = int(input("Enter a number "))
    num2 = int(input("Enter the next number "))
    num3 = int(input("Enter the final number "))
    
## This portion makes sure the numbers entered are not equal to each other
## or less than 0
    if num1 == num2 or num1 == num3 or num2 == num3:
        print("Two or more numbers are equal. Please enter different numbers.")
    elif num1 < 0 or num2 < 0 or num3 < 0:
        print("One or more numbers is less than zero. Please enter different numbers.")
    else:
## The following compare the first number to the other two
        if num1 > num2 and num1 > num3:
            great = num1
        elif num2 > num1 and num2 > num3:
            great = num2
        else:
            great = num3
            
## This part sorts the numbers into the remaining categories
        if num1 == great and num2 > num3:
            least = num3
            mid = num2
        elif num1 == great and num3 > num2:
            least = num2
            mid = num3
        elif num2 == great and num1 > num3:
            least = num3
            mid = num1
        elif num2 == great and num3 > num1:
            least = num1
            mid = num3
        elif num3 == great and num2 > num1:
            least = num1
            mid = num2
        elif num3 == great and num1 > num2:
            least = num2
            mid = num1

## This asks if the user wishes to compare more numbers
        print("The compared values are as follows \n", least, '\n', mid, '\n', great)
## Asks if the user wishes to compare more numbers
        again = input("Would you like to compare more numbers? Press 'y' for yes. ") 
