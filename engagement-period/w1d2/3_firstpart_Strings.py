# Strings
# Strings are used in Python to record text information, such as names. Strings in Python are actually a sequence, which basically means Python keeps track of every element in the string as a sequence. For example, Python understands the string "hello' to be a sequence of letters in a specific order. This means we will be able to use indexing to grab particular letters(like the first letter, or the last letter).
# Creating a String
# To create a string in Python you need to use either single quotes or double quotes.

# Single word
print('hello')

# Entire phrase
print("This is also a string")

# Be careful with quotes!
print("Using single quotes that include an apostrophe will create an error. You must use double-quotes in instances of apostrophes.")

print("Now I'm ready to use the single quotes inside a string!")

# We can use a print statement to print a string.

print("Hello world 1")
print("Hello world 2")
print("Use \n to print a new line")
print("\n")
print("See what I mean?")

# String Basics
# We can also use a function called len() to check the length of a string!
# Python's built-in len() function counts all of the characters in the string, including spaces and punctuation.

print(len("Hello World"))

# String Indexing
# We know strings are a sequence, which means Python can use indexes to call parts of the sequence.
# In Python, we use brackets[] after an object to call its index.
s = "Hello World"
print(s)

# Let's start indexing!
# Show first element (in this case a letter). We should also note that indexing starts at 0 for Python.
print(s[0])
print(s[1])
print(s[2])

# We can use a : to perform slicing which grabs everything up to a designated point.
# Grab everything past the first term all the way to the length of s which is len(s)
print(s[1:])
# Note that there is no change to the original s

# Grab everything UP TO the 3rd index
print(s[:3])

# Note the above slicing. Here we're telling Python to grab everything from 0 up to 3. It doesn't include the 3rd index. You'll notice this a lot in Python, where statements are usually in the context of "up to, but not including".

# Everything
print(s[:])

# We can also use negative indexing to go backwards.
# Last letter (one index behind 0 so it loops back around)
print(s[-1])

# Grab everything but the last letter
print(s[:-1])

# We can also use index and slice notation to grab elements of a sequence by a specified step size (the default is 1). For instance we can use two colons in a row and then a number specifying the frequency to grab elements.
# Grab everything, but go in steps size of 1
print(s[::1])

# Grab everything, but go in step sizes of 2
print(s[::2])

# We can use this to print a string backwards
print(s[::-1])

# String Properties
# It's important to note that strings have an important property known as immutability. This means that once a string is created, the elements within it can not be changed or replaced.

# Let's try to change the first letter to 'x'
# s[0] = 'x'
# Notice how the error tells us directly what we can't do, change the item assignment!

# Something we can do is concatenate strings!

print(s + " concatenate me!")

# We can reassign s completely though!
s = s + ' concatenate me!'
print(s)

# We can use the multiplication symbol to create repetition!
letter = "z"
print(letter*10)

# Basic Built-in String methods
# Objects in Python usually have built-in methods. These methods are functions inside the object(we will learn about these in much more depth later) that can perform actions or commands on the object itself.
# We call methods with a period and then the method name. Methods are in the form:
# object.method(parameters)
print(s)

# Upper Case a string
print(s.upper())

# Lower case
print(s.lower())

# Split a string by blank space (this is the default)
print(s.split())

# Split by a specific element (doesn't include the element that was split on)
print(s.split('o'))

# Print Formatting
# We can use the .format() method to add formatted objects to printed string statements.
print('Insert another string with curly brackets: {}'.format('The inserted string'))
