# SIMPLE CALCULATOR USING PYTHON

# PROMPT USER TO GIVE INPUT
NUM1=float(input("Enter the first number:"))
NUM2=float(input("Enter the second number:"))

print("Choose the operation")
print("1. ADDITION(+)")
print("2. SUBSTRACTION(-)")
print("3. MULTIPLICTION(*)")
print("4. DIVISION(/)")

# GET USERS CHOICE OF OPERATION
choice = input("choice the operation(+,-,*,/):")

#PERFORM THE CALCULATION
if choice == '+':
    result=NUM1+NUM2
    OPERATION = "ADDITION"
elif choice == '-':
    result =NUM1-NUM2
    OPERATION = "SUBSTRACTION"
elif choice == '*':
    result =NUM1*NUM2
    OPERATION == "MULTIPLICATION"
elif choice == '/':
    if NUM2!=0:
        result = NUM1/NUM2
        OPERATION == "DIVISION"
    else:
        result = "Error! Division by zero not possible."
else:
    result = "INVALID OPERATION"
    OPERATION= "UNKNOWN OPERATION"
    
    
#DISPLAY RESULT
print(f"{OPERATION} result:{result}")
    