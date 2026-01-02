print("*** A SIMPLE CALCULATOR***")
num1 = int(input("Enter the first number\n"))
num2 = int(input("Enter the second number\n"))

print("Please select the choices:\n 1.addition\n 2.Subtraction\n 3.multiplication\n 4.Division\n 5.power\n 6.squar\n")
choice = int(input("Enter choice (1-6)\n"))

from Calculator import addition, substraction, division, multiply, power, squar
if choice == 1:
    results = addition(num1,num2)
    print(results)
elif choice == 2:
    results = substraction(num1,num2)
    print(results)
elif choice == 3:
    results = multiply(num1*num2)
    print(results)
elif choice == 4:
    results = division(num1,num2)
    print(results)    
elif choice == 5:
    results = pow(num1,num2)
    print(results)
elif choice == 6:
    results = squar(num1)
    print(results)
else:
    print("Invalid choice!")
    


