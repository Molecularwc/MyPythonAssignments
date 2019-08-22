# Richard Salvaty
# 3002
# 10/12/2018
# 10 Minutes
# Hw8 Q3a Pseudocode
# Declare bTotal, gAmt, gRat, gTotal, sTax, sTotal as float
# Declare nBill as string
# while (nBill == 'y')
#   Print “Enter Subtotal”
#   Get sTotal
#   if (sTotal >=0) Then
#       Print “Enter Gratuity rate as percent”
#       Get gRat
#       if (gRat >= 0 and gRat <= 100) Then
#           Set sTax = 0.08 * sTotal
#           Set gAmt = sTotal * (gRat / 100)
#           Set bTotal = sTotal + gAmt
#           Set gTotal = bTotal + sTax
#           Print “Your total bill breakdown is: “
#           Print “Gratuity Amount: “ + gAmt
#           Print “Tax: “ + sTax
#           Print “Total: “ + bTotal
#           Print “Grand Total: “ + gTotal
#       Else
#           Print "Please enter a number greater than 0, but less than 100"
#       End if
#   Else
#       Print "Your bill cannot be less than 0, please re-enter your subtotal."
#   End if
#   Print "Would you like to enter another subtotal and gratuity amount? Y/N? "
#   Get nBill


sTax = float
gAmt = float
bTotal = float
gTotal = float
nBill = 'y'
## Begins the loop
while nBill == 'y':
    sTotal = float(input("Enter the subtotal: $"))
## Makes sure the subtotal entered isn't less than 0
    if sTotal >= 0:
        gRat = int(input("Enter the gratuity rate as percent (0 - 100): "))
## Makes sure the percent entered isn't out of bounds
        if gRat >= 0 and gRat <= 100:
            sTax = 0.08 * sTotal
            gAmt = sTotal * (gRat / 100)
            bTotal = sTotal + gAmt
            gTotal = bTotal + sTax
            print("Your total bill breakdown is: \n", "Subtotal: $", format(sTotal,",.2f"),
                  '\n', "Gratuity Amount: $", format(gAmt,",.2f"), '\n', "Tax: $", format(sTax,",.2f"),
                  '\n', "Total: $", format(bTotal,",.2f"), '\n', "Grand Total: $", format(gTotal, ",.2f"))
        else:
## Informs user of the error
            print("Please enter a number greater than 0, but less than 100")
    else:
## Informs user of the error
        print("Your bill cannot be less than 0, please re-enter your subtotal ")
## Asks user if they want to calculate another bill amount
    nBill = input("Would you like to enter another subtotal and gratuity amount? Y/N? ")
