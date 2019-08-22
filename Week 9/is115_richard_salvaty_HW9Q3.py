##Declare nChecks, bFee as integer
##Declare cFee, tFee as float
##Declare ch as string
##
##Set ch = "Y"
##Set bFee = 8
##Set tFee = 0
##While(ch == "Y")
##    Write "Enter the number of checks written this month: "
##    Get nChecks
##    while(nChecks < 1)
##        Write "Number of checks entered: " + nChecks
##        Write "The number of checks must be greater than 0."
##        Write "Re-enter the number of checks written this month: "
##        Get nChecks
##    end while
##    if (nChecks > 0 and nChecks <= 19) Then
##        Set cFee = 0.09
##    end if
##    if (nChecks >= 20 and nChecks <= 39) Then
##        Set cFee = 0.07
##    end if
##    if (nChecks >= 40  and nChecks <= 59) Then
##        Set cFee = 0.06
##    end if
##    if (nChecks >= 60) Then
##        Set cFee = 0.05
##    end if
##    tFee = (bFee + nChecks) * cFee
##    Write "The total after all fees is: $" +tFee
##    Write "Would you like to enter more check amounts? Y/N: "
##    Get ch
##end while
ch = "Y"
bFee = 8
tFee = 0
while ch == "Y":
    nChecks = int(input("Enter the number of checks written this month: "))
    while(nChecks < 1):
        print("Number of checks entered: " , nChecks)
        print("The number of checks must be greater than 0.")
        nChecks = int(input("Re-enter the number of checks written this month: "))
    if nChecks > 0 and nChecks <= 19:
        cFee = 0.09
    if nChecks >= 20 and nChecks <= 39:
        cFee = 0.07
    if nChecks >= 40  and nChecks <= 59:
        cFee = 0.06
    if nChecks >= 60:
        cFee = 0.05
    tFee = bFee + nChecks * cFee
    print("The total after all fees is: $", format(tFee, '.2f'))
    ch = input("Would you like to enter more check amounts? Y/N: ")
    ch = ch.upper()
