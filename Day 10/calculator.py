
#add
def add(num1, num2):
    return num1 + num2

#subtract
def subtract(num1, num2):
    return num1 - num2

#multiply
def multiply(num1, num2):
    return num1 * num2

#divide
def divide(num1, num2):
    return num1 / num2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

#request the user to input 2 numbers
num1 = int(input("Whats the first number? "))
num2 = int(input("Whats the second number? "))

#loop to display all possible operations
for operation in operations:
    print(operation)

operation_symbol = input("Pick an operation from the lines above: ")

calculation_function = operations[operation_symbol]
answer  = calculation_function(num1, num2)


print(f"{num1} {operation_symbol} {num2} = {answer}" )