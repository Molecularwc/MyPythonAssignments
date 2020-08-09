ch = "Y"
eTot = 0
oTot = 0
nSqr = 0
nCube = 0
while ch == "Y":
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    while num1 > num2:
        print("The first number must be less than the second number.")
        num1 = int(input("Re-enter the first number: "))
        num2 = int(input("Re-enter the second number: "))
    print("The even numbers are: ")
    for n in range(num1, num2 + 1):        
        if n % 2 == 0:
            print(n)
            eTot = eTot + n
    print("The total sum of even numbers is: ", eTot)
    print("The odd numbers are: ")
    for n in range(num1, num2 + 1):        
        if n % 2 == 1:
            print(n)
            oTot = oTot + n
    print("The total sum of odd numbers is: ", oTot)
    print('Number\tSquared\tCubed')
    for n in range(num1, num2):
        nSqr = n**2
        nCube = n**3
        print(n, '\t', nSqr, '\t', nCube)
    ch = input("Would you like to try different numbers? Y/N: ")
    ch = ch.upper()
