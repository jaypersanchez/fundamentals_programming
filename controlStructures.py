#### Conditional Statements

# Example 1: if statement
x = 10
if x > 0:
    print("x is positive")

# Example 2: if-elif-else statement
x = -5
if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")

#### Loops (for and while)

# Example 3: for loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Example 4: while loop
count = 0
while count < 5:
    print(count)
    count += 1

### Break and Continue Statements

# Example 5: break statement
for i in range(10):
    if i == 5:
        break
    print(i)

# Example 6: continue statement
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)


