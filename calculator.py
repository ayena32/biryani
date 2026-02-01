def add(num1, num2):
   total = num1 + num2
   return(total)
def subtract(num1, num2):
   total = num1 - num2
   return(total)
def multiply(num1, num2):
   total = num1*num2
   return(total)
def divide(num1, num2):
   total = num1/num2
   return(total)
def exponent(num1, num2):
   total = num1**num2
   return(total)
def sqrt(num1)
    total = num1**0.5
    return(total)
 # main programme
print("Reload page to restart calculator.")
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number (Exponent: Enter the power)"))
option = int(input("Choose an option, 1: Add. 2: Subtract. 3: Multiply. 4: Divide. 5: Exponent. 6: Square root."))
if option == 1:
  answer = add(num1, num2)
  print(answer)
elif option == 2:
   answer = subtract(num1, num2)
   print(answer)
elif option == 3:
   answer = multiply(num1, num2)
   print(answer)
elif option == 4:
   answer = divide(num1, num2)
   print(answer)
elif option == 5:
   answer = exponent(num1, num2)
   print(answer)
elif option == 6:
   answer = sqrt(num1)
   print(answer)
elif option == 7:
   answer = area(num1)
else:
   print("Not an option")
