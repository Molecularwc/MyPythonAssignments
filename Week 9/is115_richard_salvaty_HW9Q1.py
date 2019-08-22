##Declare oTotal, tCost, sCost as float
##Declare dLoc as string
##Write “Enter Total Order Amount”
##Get oTotal
##Write “Enter shipping Destination (USA or Canada)”
##Get dLoc
##If(oTotal >= 0 && oTotal <= 10,000) Then
##If(dLoc == “USA”)Then
##If(oTotal >=0 && oTotal <= 49.99) Then
##Set sCost = 6
##End If
##If(oTotal >=50 && oTotal <= 99.99) Then
##Set sCost = 9
##End If
##If(oTotal >=100 && oTotal <= 149.99) Then
##Set sCost = 12
##End If
##If(oTotal >=150 && oTotal <= 10,000) Then
##Set sCost = 0
##End If
##End If
##If(dLoc == “Canada”)Then
##If(oTotal >=0 && oTotal <= 49.99) Then
##Set sCost = 8
##End If
##If(oTotal >=50 && oTotal <= 99.99) Then
##Set sCost = 12
##End If
##If(oTotal >=100 && oTotal <= 149.99) Then
##Set sCost = 15
##End If
##If(oTotal >=150 && oTotal <= 10,000) Then
##Set sCost = 0
##End If
##End If
##Set tCost = oTotal + sCost
##Write “Destination = “ + dLoc
##Write “Order Total = “ + oTotal
##Write “Shipping Cost = “ + sCost
##Write “Total Cost = “ + tCost
##End IF
##Else 
##If(dLoc != “USA” && dLoc != “Canada”) Then
##Write “Destination = “ + dLoc
##Write “ERROR – Unknown Destination”
##End IF
##If(oTotal < 0 || oTotal > 10,000) Then
##Write “Destination = “ + dLoc
##Write “Order Total = “ + oTotal
##Write “ERROR – Invalid order amount”
##End If

ch = 'Y'
##Begin the main program loop
while ch == 'Y':    
    oTotal = float(input("Enter total order amount: "))
    while oTotal < 0 or oTotal > 10000:
        print("Order Total = $", (format(oTotal, '.2f')))
        print("ERROR – Invalid order amount")
        oTotal = float(input("Enter a valid total order amount: "))
    dLoc = input("Enter shipping Destination (USA or Canada): ")
    while dLoc != "USA" and dLoc != "Canada":
        print("Destination = ", dLoc)
        print("ERROR – Unknown Destination")
        dLoc = input("Enter a valid shipping Destination (USA or Canada): ")
    sCost = 0
    tCost = 0
    ##Determin if entered values are valid for the operations
    if oTotal >= 0 and oTotal <= 10000:
        if dLoc == "USA":
            if oTotal >=0 and oTotal <= 49.99:
                sCost = 6            
            if oTotal >=50 and oTotal <= 99.99:
                sCost = 9            
            if oTotal >=100 and oTotal <= 149.99:
                sCost = 12            
            if oTotal >=150 and oTotal <= 10000:
                sCost = 0
        if dLoc == "Canada":
            if oTotal >=0 and oTotal <= 49.99:
                sCost = 8
            if oTotal >=50 and oTotal <= 99.99:
                sCost = 12
            if oTotal >=100 and oTotal <= 149.99:
                sCost = 15
            if oTotal >=150 and oTotal <= 10000:
                sCost = 0
        tCost = oTotal + sCost
        print("Destination = ", dLoc)
        print("Order Total = $", (format(oTotal, '.2f')))
        print("Shipping Cost = $", (format(sCost, '.2f')))
        print("Total Cost = $", (format(tCost, '.2f')))
    ch = input("Would you like to process another order? Y/N: ")
    ch = ch.upper()
