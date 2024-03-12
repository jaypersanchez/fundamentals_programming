def safe_divide(x, y):
    try:
        result = x / y
        print("Result:", result)
    except (ZeroDivisionError, TypeError) as e:
        print(f"Error: {e}")

# Calling the safe_divide function
safe_divide(10, 2)
safe_divide(10, 0)
safe_divide(10, 'a')
