##Author: Richard Salvaty
##IS115 HW 10
##Due Date: 11/28/2018
##Time: 45 mins

##This program has 5 functions
def LowestNumphy(num1, num2, num3):##compare 3 numbers to find the lowest
    if (num1 == num2) or (num1 == num3) or (num2 == num3):
        print("Two or more numbers are equal to each other.")
        num1 = int(input("Enter another number: "))
        num2 = int(input("Enter another second number: "))
        num3 = int(input("Enter another third number: "))
    if (num1 < num2) and (num1 < num3):
        lowest = num1
    if (num2 < num1) and (num2 < num3):
        lowest = num2
    if (num3 < num1) and (num3 < num2):
        lowest = num3    
    return lowest

def TaxRebatephy(fName, lName, depNum):##calculate a tax rebate
  tRebate = depNum * 2300
  return tRebate

def NumFunphy(anyNum):##Squaring/Cubing a number
  numSQ = anyNum ** 2
  numCU = anyNum ** 3
  print(anyNum, "***", numSQ, "&&&", numCU)

def NumRangephy(num4, num5):##printing numbers in a range
    if num4 >= num5:
        print("FAIL")
        num4 = int(input("Enter another beginning number: "))
        num5 = int(input("Enter another ending number: "))
        for i in range(num4, num5 + 1):
            print(i)
            i= i + 1
    else:
        for i in range(num4, num5 + 1):
            print(i)
            i= i + 1

def Distance(grav, thyme):##calculating distance
  distance = (1/2 * grav) * (thyme**2)
  return distance

def main():##meat and potatoes of the program
    n1 = int(input("Enter a number: "))
    n2 = int(input("Enter a second number: "))
    n3 = int(input("Enter a third number: "))
    low = LowestNumphy(n1, n2, n3)##Func call
    print("The lowest number is: ", low)

    fN = input("Enter your first name: ")
    lN = input("Enter your last name: ")
    dN = int(input("Enter the number of dependents: "))
    moMoney = TaxRebatephy(fN, lN, dN)##Func call
    print(fN, lN, "your rebate is: $", moMoney)

    sent = 1
    while sent != 0:##fun loop
      aN1 = int(input("Enter a number. Press 0 to end: "))
      if aN1 == 0:
          sent = 0
      else:
          NumFunphy(aN1)##Func call

    n4 = int(input("Enter a beginning number: "))
    n5 = int(input("Enter an ending number: "))
    NumRangephy(n4, n5)##Func call

    ch = 'y'
    while ch == 'y':##Another loop. YAY!
      g1 = float(input("Enter an a gravitational number: "))
      t1 = float(input("Enter a time traveled: "))
      dist = Distance(g1, t1)##Func call
      print("The distance traveled is:", dist)
      ch = input("Would you like to enter a new set of values? Y/N: ")
      if(ch == 'n'):
          print("******Goodbye!******")

main()##Get the party started
