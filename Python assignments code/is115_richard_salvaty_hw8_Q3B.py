## Richard Salvaty
## 3002
## 10/15/2018
## 10 minutes

## Delcare nTemp as string
## Declare Cel as integer
## Declare Fah as float
## Set nTemp = 'y'
## while (nTemp == 'y')
##      Print "Enter degrees in Celcius to be converted to Fahrenheit: "
##      Get Cel
##      Set Fah = (9/5 * Cel) + 32
##      Print "Degrees in Celsius entered: " + Cel
##      Print "Degrees in Fahrenheit: " + Fah
##      Print "Would you like to enter another temperature for conversion? Y/N: "
##      Get nTemp
## End While

nTemp = 'y'
## This is just a simple Celsius to Fahrenheit conversion loop
while nTemp == 'y':
    Cel = int(input("Enter degrees in Celsius to be converted to Fahrenheit: "))
    Fah = (9/5 * Cel) + 32
    print ("Degrees in Celsius entered: ", Cel, '\n', "Degrees in Fahrenheit: ", format(Fah, ".1f"))
## Asks the user if they want to enter another temp
    nTemp = input("Would you like to enter another temperature for conversion? Y/N: ")
