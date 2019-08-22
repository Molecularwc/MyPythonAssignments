##Declare nDays, nBooks, tBooks, i as integer
##Declare ch as string
##ch = "Y"
##i = 0
##tBooks = 0
##
##While(ch == "Y")
##    Write "Enter the number of days books were collected: "
##    Get nDays
##    while(nDays < 0)
##        Write nDays
##        Write "Invalid entry. You cannot have less than 0 days."
##        Write "Re-enter the number of days books were collected: "
##        Get nDays
##    end while
##    For each i in range(0, nDays, i++)
##        Write "Enter the number of books collected: "
##        Get nBooks
##        while(nBooks <0)
##            Write nBooks
##            Write "You cannot collect less than 0 books."
##            Write "Re-enter the number of books collected: "
##        end while
##        tBooks = tBooks + nBooks
##    end for
##    Write "The total number of books collected over " + nDays + " days = "
##    Write "Would you like to enter more data? Y/N"
##    Get ch
##end while
ch = "Y"
i = 0
tBooks = 0
while ch == "Y":
    nDays = int(input("Enter the number of days books were collected: "))
    while nDays < 0:
        print("Number of days entered: ", nDays)
        print("Invalid entry. You cannot have less than 0 days.")
        nDays = int(input("Re-enter the number of days books were collected: "))
    for i in range(0, nDays):
        nBooks = int(input("Enter the number of books collected: "))
        while nBooks < 0:
            print("Number of books entered: ", nBooks)
            print("You cannot collect less than 0 books.")
            nBooks = int(input("Re-enter the number of books collected: "))
        tBooks = tBooks + nBooks
    print("The total number of books collected over ", nDays, " days = ", tBooks)
    ch = input("Would you like to enter more data? Y/N: ")
    ch = ch.upper()
