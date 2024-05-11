# Default Param Values

"""
def greet_person(name, greeting="Welcome"):
    print(f"{greeting}, {name}")


greet_person("Paul")
greet_person("Anna", "Hi there!")

"""


def print_message(message, num_exclamation_marks=3):
    """Print a message with a specified number of exclamation marks."""
    print(message + "!" * num_exclamation_marks)


# Calling the function with different arguments
# Prints "Hello!!!" using the default number of exclamation marks
print_message("Hello")
# Prints "Hi there!!!!!" with the specified number of exclamation marks
print_message("Hi there", 5)
print_message("Greetings", 10) #
