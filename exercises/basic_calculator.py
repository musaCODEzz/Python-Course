#!/usr/bin/env python3
"""
Basic Calculator Exercise

This module implements a simple calculator with basic arithmetic operations.
It serves as a learning example for Python functions and docstrings.
"""

def add(a, b):
    """
    Add two numbers and return the result.
    
    Args:
        a (int or float): The first number
        b (int or float): The second number
        
    Returns:
        int or float: The sum of a and b
    """
    # Addition operation
    return a + b

def subtract(a, b):
    """
    Subtract the second number from the first and return the result.
    
    Args:
        a (int or float): The number to subtract from
        b (int or float): The number to subtract
        
    Returns:
        int or float: The difference between a and b
    """
    # Subtraction operation
    return a - b

def multiply(a, b):
    """
    Multiply two numbers and return the result.
    
    Args:
        a (int or float): The first number
        b (int or float): The second number
        
    Returns:
        int or float: The product of a and b
    """
    # Multiplication operation
    return a * b

def divide(a, b):
    """
    Divide the first number by the second and return the result.
    
    Args:
        a (int or float): The dividend
        b (int or float): The divisor
        
    Returns:
        int or float: The quotient of a divided by b
        
    Raises:
        ZeroDivisionError: If the divisor is zero
    """
    # Check for division by zero
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero!")
    
    # Division operation
    return a / b

def calculator():
    """
    Run an interactive calculator program that allows users to perform
    basic arithmetic operations.
    """
    print("Welcome to Basic Calculator!")
    print("Operations available: +, -, *, /")
    
    while True:
        # Get user input
        try:
            a = float(input("Enter first number: "))
            op = input("Enter operation (+, -, *, /): ")
            b = float(input("Enter second number: "))
            
            # Perform calculation based on operation
            if op == "+":
                result = add(a, b)
                print(f"{a} + {b} = {result}")
            elif op == "-":
                result = subtract(a, b)
                print(f"{a} - {b} = {result}")
            elif op == "*":
                result = multiply(a, b)
                print(f"{a} * {b} = {result}")
            elif op == "/":
                try:
                    result = divide(a, b)
                    print(f"{a} / {b} = {result}")
                except ZeroDivisionError as e:
                    print(f"Error: {e}")
            else:
                print("Invalid operation. Please use +, -, *, or /.")
                
            # Ask if user wants to continue
            again = input("Calculate again? (y/n): ")
            if again.lower() != 'y':
                break
                
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            
    print("Thank you for using Basic Calculator!")

# Run the calculator if the script is executed directly
if __name__ == "__main__":
    calculator()

