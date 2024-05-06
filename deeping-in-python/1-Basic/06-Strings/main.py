# Strings - Using single and double quotes

# Single quotes
name = 'John'
print(name)

# Double quotes
surname = "Smith"
print(surname)

# Multiline strings triple quotes
long_string = """
This is a multiline string.
It can contain multiple lines of text.
"""
print(long_string)

another_long_string = '''
This is another multiline string with single quotes.'''
print(another_long_string)

# Concatenation
str1 = "I'm"
str2 = "a string"
srt3 = "concatenated. :)"
print(f"{str1} {str2} {srt3}")

# String indexing and slicing
string = "Hello, World!"
print(string[0]) # H
print(string[2:5]) # llo
print(string[2:]) # llo, World!
print(string[:5]) # Hello
print(string[:]) # Hello, World!
print(string[-1]) # !

# Some string methods
string = "Python is powerful."
print(string.upper()) # PYTHON IS POWERFUL.
print(string.lower()) # python is powerful.
print(string.title()) # Python Is Powerful.
print(string.strip()) # Python is powerful.
print(string.split()) # ['Python', 'is', 'powerful.']
print(string.capitalize()) # Python is powerful.

# String formatting
language = "Python"
version = "3.12.1"
print(f"{language} version {version}") # Python version 3.12.1
print(f"{language} version {version:.2f}") # Python version 3.12.1

# Escape Characters
escaped_string = "This is an line.\nThis is another line. \\"