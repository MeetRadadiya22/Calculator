import os
from art import logo

print(logo)


#add
def add(n1, n2):
  return n1 + n2

#subtract
def sub(n1, n2):
  return n1 - n2

#multiply
def mul(n1, n2):
  return n1 * n2

#divide
def div(n1, n2):
  return n1 / n2

operations = {"+": add, 
              "-": sub, 
              "*": mul, 
              "/": div
              }

# we have used the recursion method by calling the function in the function itself, 
# but be very careful as it can be an infinite loop. ;)
def calculator():
  #inputs from users

  firstDigit = input("\ngive the first digit: ")
  firstDigit = float(firstDigit)

  repeat = True
  while repeat == True:
 
    print("")
    for key in operations:
      print(f"  {key}  ",end="")
    print("")
    operationInput = input("\nselect any operation from above to perform: ")
    
    secondDigit = input("give the digit: ")
    secondDigit = float(secondDigit)
    
    def task(first, second):
      for k in operations:
        if operationInput == k:
          answer = operations[k](first, second)
      return answer

    calculation = task(firstDigit, secondDigit)
    result = f"\n{firstDigit} {operationInput} {secondDigit} = {calculation}\n"
    print(result)

    secondCalc = input("Do you want to calculate further? 'Y' OR 'N': ")
    
    if secondCalc == "Y":
      repeat = True
      firstDigit = calculation
    else:
      repeat = False
      print("Thank you!")
      os.system('cls')
      calculator()

calculator()
    
