def safe_divide(x, y):
    try:
        result = x / y
        print("Result:", result)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")

# Calling the safe_divide function
safe_divide(10, 2)
safe_divide(10, 0)
