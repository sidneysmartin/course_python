# str.upper() & str.lower()
text = "Python is AWESOME"

print(text.upper())

print(text.lower())

# str.capitalize() and str.title()

phrase = "Python is data science popular language"
print(phrase.capitalize())
print (phrase.title())

# str.strip(), str.lstrip(), str.rstrip()
sentence = "   This is a sentence.   "
stripped0 = sentence.strip()
stripped1 = sentence.lstrip()
stripped2 = sentence.rstrip()

print(stripped0)
print(stripped1)
print(stripped2)

# str.startswith(prefix) and str.endswith(suffix)
filename = "exemple.txt"
starts_with = filename.startswith("ex")
ends_with = filename.endswith(".py")
print(starts_with) # Returns True
print(ends_with) # Returns False

# str.replace(old, new)
sentence = "I like programming in Django"
new_sentence = sentence.replace("Django", "Python")
print(sentence) # I like programming in Django
print(new_sentence) # I like programming in Python

# str.find(substring) and str.index(substring)
phrase = "Python has a powerful usage, lot of libraries and frameworks"
index1 = phrase.index("Python")
find1 = phrase.find("Django")
print(index1) # 0
print(find1) # -1

# splits
words = phrase.split(" ")
print(words) # ['Python', 'has', 'a', 'powerful', 'usage,', 'lot', 'of', 'libraries', 'and', 'frameworks']

# str.count(substring) 
count = phrase.count("a")
print(len(phrase))
print(count) # 3

# str.count(substring)
phrase = "Python is ease, Python is fun and Python is powerful"
count_python = phrase.count("Python")
countI = 0
countWord = "Python"
print(count_python) # 3
 