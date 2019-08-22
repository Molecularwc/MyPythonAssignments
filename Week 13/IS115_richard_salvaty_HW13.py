## Author: Richard Salvaty
## IS 115 HW 13
## Due Date: 12/12/2018
## Time to complete: 2 hours

ch = 'y'
while(ch == 'y'):
    rDisc = 0
    dDisc = 0 
    tCost = 0
    tBill = 0
    rooDisc = 0
    dayDisc = 0
    rSub = 0
    tDisc = 0
    spOcc = 'n'

    rCost = float(input("Enter the cost per room rented: $"))
    nRooms = int(input("Enter the number of rooms booked: "))
    nDays = int(input("Enter the number of days booked: "))
    sTax = float(input("Enter the sales tax as a percent: "))
    spOcc = input("Is this a special occasion? Y/N: ")

    if spOcc == 'y':
        spOccTyp = input("Is this a wedding or conference? ")
        if nRooms >= 10:
          rDisc = 0.1
        if nRooms >= 20:
          rDisc = 0.2
        if nRooms >= 30:
          rDisc = 0.3

        rSub = rCost * nRooms
        rooDisc = rSub * rDisc
        tCost = (rCost * nRooms) * nDays
        tsTax = tCost * (sTax / 100)
        sTotal = tCost + tsTax
        aTotal = (sTotal / nRooms) / nDays

        print("The cost of booking a single room per day: $", format(aTotal, '.2f'))
        print("Occasion type: ", spOccTyp)
        print("Discount per room(if applicable): ", (rDisc * 100), "%")
        print("Number of rooms booked: ", nRooms)
        print("Number of days booked: ", nDays)
        if nDays >= 3:
          dDisc = 0.05
          dayDisc = rSub * dDisc
          print("Additional discount calculated by number of days you booked: ", (dDisc * 100), "%")
        tDisc = rooDisc + dayDisc
        print("The total cost of the room(s): $", format(tCost, '.2f'))
        print("Total sales tax: $", format(tsTax, '.2f'))
        print("Total bill before any applicable discounts: $", format(sTotal, '.2f'))
        print("Your total discount savings: $", format(tDisc, '.2f'))
        print("Total billing amount(after any applicable discounts): $", format(((sTotal - rooDisc) - dayDisc), '.2f'))
    else:          
        rSub = rCost * nRooms
        rooDisc = rSub * rDisc
        tCost = (rCost * nRooms) * nDays
        tsTax = tCost * (sTax/ 100)
        sTotal = tCost + tsTax
        aTotal = (sTotal / nRooms) / nDays

        print("The cost of booking a single room per day: $", format(aTotal, '.2f'))
        print("Discount per room(if applicable): ", (rDisc * 100), "%")
        print("Number of rooms booked: ", nRooms)
        print("Number of days booked: ", nDays)
        if nDays >= 3:
          dDisc = 0.05
          dayDisc = rSub * dDisc
          print("Additional discount calculated by number of days you booked: ", (dDisc * 100), "%.")
        tDisc = rooDisc + dayDisc
        print("The total cost of the room(s): $", format(tCost, '.2f'))
        print("Total sales tax: $", format(tsTax, '.2f'))
        print("Total bill before any applicable discounts: $", format(sTotal, '.2f'))
        print("Your total discount savings: $", format(tDisc, '.2f'))
        print("Total billing amount(after any applicable discounts): $", format(((sTotal - rooDisc) - dayDisc), '.2f'))
    ch = input("Would you like to calculate another bill? Y/N: ")
