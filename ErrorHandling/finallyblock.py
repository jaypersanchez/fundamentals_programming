def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("File content:", content)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
    finally:
        print("Cleanup: Closing file")

# Calling the read_file function
read_file("example.txt")
