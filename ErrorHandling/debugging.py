def divide(x, y):
    # Debugging with print statements
    print(f"Dividing {x} by {y}")
    result = x / y
    print("Result:", result)
    return result

# Calling the divide function
divide(10, 2)
divide(10, 0)  # This will cause a ZeroDivisionError
