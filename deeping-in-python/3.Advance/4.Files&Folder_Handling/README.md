# open()

### The open() function is used to open a file and return a corresponding file object. It is a built-in function that takes two arguments: the file (path) and the (mode) in which to open the file (e.g., read mode, write mode, append mode, etc.).

# close()

# Close function is used to close a file.

# With Statement

# "with" statement is also use to open a file, but when we open a file with "with" statement there is no need to close the file explicitly.

## File Modes

#### r 👉: Read mode. Opens a file for reading only. The file pointer is placed at the beginning of the file.

#### w 👉: Write mode. Opens a file for writing only. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing.

#### a 👉: Append mode. Opens a file for appending data. The file pointer is at the end of the file if the file exists. If the file does not exist, it creates a new file for writing.

#### b 👉: Binary mode. Opens the file in binary mode, which is used for non-text files (e.g., images, videos).

#### + 👉: Read and Write mode. Opens a file for both reading and writing.

# write()

### The write() method is used to write data to a file. It is called on a file object that has been opened in write or append mode. The write() method takes a single argument, which is the string of data to be written to the file.

# writelines()

### The writelines() method is used to write a list of lines to a file. Each item in the list should be a string representing a line of text. The writelines() method does not add line separators (like \n) between the lines, so you'll need to include them in the strings if you want them to be present in the file.


# read()

# The read() method in Python is used to read a specified number of bytes from a file. If no argument is provided, it will attempt to read the entire file. When the end of the file is reached, read() returns an empty string.