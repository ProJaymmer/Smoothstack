# Dynamic Typing
# Python uses dynamic typing, meaning you can reassign variables to different data types. This makes Python very flexible in assigning data types
# it differs from other languages that are statically typed.
from curses import echo


my_dogs = 2
print(my_dogs)

my_dogs = ["Sammy", "Frankie"]
print(my_dogs)

# Pros and Cons of Dynamic Typing
# Pros of Dynamic Typing
# •	very easy to work with
# •	faster development time
# Cons of Dynamic Typing
# •	may result in unexpected bugs!
# •	you need to be aware of type()

# Assigning Variables
# Variable assignment follows name = object, where a single equals sign = is an assignment operator
a = 5
print(a)
a = 10
print(a)
print(a + a)

# Reassigning Variables
# Python lets you reassign variables with a reference to the same object.
a = a + 10
print(a)

# There's actually a shortcut for this. Python lets you add, subtract, multiply and divide numbers with reassignment using +=, -=, *=, and /=.

a += 10
print(a)

a *= 2
print(a)

# Determining variable type with type()
# You can check what type of object is assigned to a variable using Python's built-in type() function. Common data types include:
# •	int(for integer)
# •	float
# •	str(for string)
# •	list
# •	tuple
# •	dict(for dictionary)
# •	set
# •	bool(for Boolean True/False)
print(type(a))

a = (1, 2)
print(type(a))

# Simple Exercise
# This shows how variables make calculations more readable and easier to follow.
my_income = 100
tax_rate = 0.1
my_taxes = my_income * tax_rate

print(my_taxes)

# Great! You should now understand the basics of variable assignment and reassignment in Python.
# Up next, we'll learn about strings!
