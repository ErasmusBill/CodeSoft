print("================== Simple Calculator =======================")
number_1 = int(input("Please enter the first_number: "))
number_2 = int(input("Please enter the second_number: "))

print("=============================================================")
operator = input("Please enter the operation you will like to perform: ")
print("=============================================================")
if operator == "+":
    sum = number_1 + number_2
    print(f"The sum of the numbers is {sum}")
    print("=============================================================")
elif operator == "-":
    difference = number_1-number_2
    print(f"The result of the subtraction is  {difference}")  
    print("=============================================================")
elif operator == "/":
    division = number_1/number_2
    print(f"The result of the divison is {division}") 
    print("=============================================================")
elif operator == "*":
    multiplication = number_1*number_2
    print(f"The result of the the multiplication is {multiplication}")
    print("=============================================================")
else:
    print("Invalid input")    
               
    