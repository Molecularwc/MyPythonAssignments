##Author: Richard Salvaty
##IS115
##Due Date: 11/30/2018
##Time to Complete: 2 hours

def WorkerPayphy(fN):
  try:
      file = open(fN, 'r')
      emPay = file.read()
      print("This file already exists")
      file.close()
      file = open(fN, 'a')
      numEmp = int(input("How many employees would you like to process data for?: "))
      for i in range(0, numEmp):
          empName = input("Enter the employee name: ")
          hWorked = int(input("Enter the number of hours worked: "))
          pRate = float(input("Enter the rate of pay: $"))
          if hWorked > 40:
              rPay = pRate * 40
              oPay = (pRate * 2) * (hWorked - 40)
              tPay = rPay + oPay
              aPay = tPay / hWorked
              file.write(str("Name: " + empName) + '\t')
              file.write(str("Total pay: $" + '{:,.2f}'.format(tPay)) + '\t')
              file.write(str("Average pay: $" + '{:,.2f}'.format(aPay)) + '\n') 
          else:
              tPay = pRate * hWorked
              aPay = tPay / hWorked
              file.write(str("Name: " + empName) + '\t')
              file.write(str("Total pay: $" + '{:,.2f}'.format(tPay)) + '\t')
              file.write(str("Average pay: $" + '{:,.2f}'.format(aPay)) + '\n')
  except:
      file = open(fN, 'a')
      numEmp = int(input("How many employees would you like to process data for?: "))
      for i in range(0, numEmp):
          empName = input("Enter the employee name: ")
          hWorked = int(input("Enter the number of hours worked: "))
          pRate = float(input("Enter the rate of pay: $"))
          if hWorked > 40:
              rPay = pRate * 40
              oPay = (pRate * 2) * (hWorked - 40)
              tPay = rPay + oPay
              aPay = tPay / hWorked
              file.write(str("Name: " + empName) + '\t')
              file.write(str("Total pay: $" + '{:,.2f}'.format(tPay)) + '\t')
              file.write(str("Average pay: $" + '{:,.2f}'.format(aPay)) + '\n')
          else:
              tPay = pRate * hWorked
              aPay = tPay / hWorked
              file.write(str("Name: " + empName) + '\t')
              file.write(str("Total pay: $" + '{:,.2f}'.format(tPay)) + '\t')
              file.write(str("Average pay: $" + '{:,.2f}'.format(aPay)) + '\n')

def main():
  pName = input("Enter the employee name: ")
  try:
      pSal = float(input("Enter their salary: $"))
      if pSal < 0:
        pSal = float(input("The salary can not be negative. Re-enter the salary: $"))
  except:
      pSal = float(input("The salary cannot contain letters or special characters. Re-enter the salary: $"))

  fileName = "mydata.txt"
  file = open(fileName, 'a')
  file.write(str("Employee Name: " + pName) + '\t')
  file.write(str("Salary: $" + '{:,.2f}'.format(pSal)) + '\n')
  file.close()

  ioName = input("Enter a file name: ")
  uName = input("Enter a username: ")
  uEmail = input("Enter an email address: ")
  file = open(ioName, 'a')
  file.write(str("Username: " + uName) + '\t')
  file.write(str("Email Address: " + uEmail) + '\n')
  ##for x in range(100, 0, -10):
      ##file.write(str(x) + '\n')
  file.close()

  file = open(fileName, 'r')
  pData = file.read()
  print(pData)
  file.close()

  fName = input("Enter a file name: ")
  workerPay = WorkerPayphy(fName)

main()
