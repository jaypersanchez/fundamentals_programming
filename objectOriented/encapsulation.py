# Example 3: Encapsulation
class Book:
    def __init__(self, title, author):
        self._title = title  # Protected attribute
        self._author = author  # Protected attribute

    # Getter methods
    def get_title(self):
        return self._title

    def get_author(self):
        return self._author

    # Setter methods
    def set_title(self, title):
        self._title = title

    def set_author(self, author):
        self._author = author

# Creating an object of the Book class
book = Book("Python Programming", "John Doe")

# Accessing attributes using getter methods
print("Title:", book.get_title())
print("Author:", book.get_author())

# Modifying attributes using setter methods
book.set_title("Python Programming 101")
book.set_author("Jane Smith")

print("Modified Title:", book.get_title())
print("Modified Author:", book.get_author())
