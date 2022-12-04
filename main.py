# simple calculator

k = input("what's your name :")

print("HI", k, "\nWELCOME TO SIMPLE CALCULATOR ROBOT")
print("")

x = int(input("Enter your first number:"))
y = int(input("Enter your second number:"))
print("")

z = int(input(
    "which mathematical function would you like to use: \naddition:press 1  \nsubstraction:press 2 \ndivision:press 3 \nmultiplication:press 4\n"))
print(z)
# addition:      press 1
# substraction:  press 2
# division:      press 3
# multiplication:press 4

if (z == 1):
    print("sum between your chosen numbers are:", x + y)

elif (z == 2):
    print("substraction between your chosen numbers are:", x - y)
elif (z == 3):
    print("division between your chosen numbers are :", x / y)
elif (z == 4):
    print("multiplication between your chosen numbers are:", x * y)
else:
    print("")
