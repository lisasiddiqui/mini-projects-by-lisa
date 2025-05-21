import math
from datetime import datetime

# List to store calculation history
calculation_history = []

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def calculator():
    while True:
        try:
            # Input and validation
            num1 = float(input("Enter first number: "))
            operator = input("Enter operator (+, -, *, /, pow, log, sqrt): ").lower()
            
            # Handling different operation types
            if operator in ['+', '-', '*', '/', 'pow', 'log']:
                num2 = float(input("Enter second number: "))
            elif operator == 'sqrt':
                num2 = None
            else:
                print("Invalid operator")
                continue

            # Perform calculations with error handling
            if operator == '+':
                result = add(num1, num2)
            elif operator == '-':
                result = subtract(num1, num2)
            elif operator == '*':
                result = multiply(num1, num2)
            elif operator == '/':
                result = divide(num1, num2)
            elif operator == 'pow':
                result = math.pow(num1, num2)
            elif operator == 'log':
                result = math.log(num1, num2)
            elif operator == 'sqrt':
                if num1 < 0:
                    raise ValueError("Cannot calculate square root of a negative number")
                result = math.sqrt(num1)

            # Record calculation history
            timestamp = datetime.now()
            history_record = (timestamp, operator, num1, num2, result)
            calculation_history.append(history_record)

            # Display result
            print(f"The result is: {result}")

            # Option to continue or view history
            choice = input("Do you want to (c)ontinue, (h)istory, or (q)uit? ").lower()
            if choice == 'h':
                display_history()
            elif choice != 'c':
                break

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

def display_history():
    if not calculation_history:
        print("No calculation history available.")
        return
    
    print("\n--- Calculation History ---")
    for record in calculation_history:
        timestamp, operator, num1, num2, result = record
        if num2 is not None:
            print(f"{timestamp}: {num1} {operator} {num2} = {result}")
        else:
            print(f"{timestamp}: {operator} {num1} = {result}")

# Run the calculator
if __name__ == "__main__":
    calculator()