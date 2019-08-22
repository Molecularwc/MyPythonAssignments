##Declare n, num1, num2, nSqr, nCube, eTot, oTot as integer
##Declare ch as string
##Set ch = "Y"
##Set eTot = 0
##Set oTot = 0
##Set nSqr = 0
##Set nCube = 0
##while(ch == "Y")
##    Write "Enter the first number: "
##    Get num1
##    Write "Enter the second number: "
##    Get num 2
##    while(num1 > num2)
##        Write "The first number must be less than the second number."
##        Write "Re-enter the first number: "
##        Get num1
##        Write "Re-enter the second number: "
##        Get num2
##    end while
##    Write "The even numbers are: "
##    for n in range(num1, num2 + 1)        
##        if(n % 2 == 0) Then
##            Write n
##            Set eTot = eTot + n
##        end if
##    end for
##    Write "The total sum of even numbers is: " + eTot
##    Write "The odd numbers are: "
##    for n in range(num1, num2 + 1)        
##        if(n % 2 == 1) Then
##            Write n
##            Set oTot = oTot + n
##            
##        end if
##    end for
##    Write "The total sum of odd numbers is: " + oTot
##    Write "Number\tSquared\tCubed"
##    for n in range(num1, num2)
##        Set nSqr = n**2
##        Set nCube = n**3
##        Write n + nSqr + nCube
##    end for
##    Write "Would you like to try different numbers? Y/N: "
##    Get ch
##end while
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
