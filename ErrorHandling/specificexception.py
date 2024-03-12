def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("File content:", content)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")

# Calling the read_file function
read_file("example.txt")  # Assuming example.txt does not exist in the current directory
