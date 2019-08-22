## Richard Salvaty
## 3002
## 10/15/2018
## 10 minutes

## Delcare nTemp as string
## Declare Cel as integer
## Declare Fah as float
## Set nTemp = 'y'
## while (nTemp == 'y')
##      Print "Enter degrees in Fahrenheit to be converted to Celsius: "
##      Get Fah
##      Set Cel = ((Fah - 32) * 5) / 9
##      Print "Degrees in Fahrenheit entered: " + Fah
##      Print "Degrees in Celsius: " + Cel
##      Print "Would you like to enter another temperature for conversion? Y/N: "
##      Get nTemp
## End While

nTemp = 'y'
##This is just a simple Fahrenheit to Celsius conversion loop
while nTemp == 'y':
    Fah = float(input("Enter degrees in Fahrenheit to be converted to Celsius: "))
    Cel = int(((Fah - 32) * 5) / 9)
    print ("Degrees in Fahrenheit entered: ", format(Fah, ".1f"), '\n', "Degrees in Celsius: ", Cel)
## Asks the user if they want to enter another temp
    nTemp = input("Would you like to enter another temperature for conversion? Y/N: ")
