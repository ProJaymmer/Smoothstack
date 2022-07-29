# Basic Arithmetic
print(2+1)
print(2-1)
print(2*2)
print(3/2)
print(7 % 4)
print(2**3)
print(4**0.5)
# Order of Operations followed in Python
print(2 + 10 * 10 + 3)
# Can use parentheses to specify orders
print((2+10)*(10+3))
# Variable Assignments
# Now if I call a in my Python script, Python will treat it as the number 5.
a = 5
print(a + a)
# What happens on reassignment? Will Python let us write it over?
a = 10
print(a)
# Yes! Python allows you to write over assigned variable names. We can also use the variables themselves when doing the reassignment.
# Use A to redefine A
a = a + a
print(a)

# Using variable names can be a very useful way to keep track of different variables in Python. For example:
# Use object names to keep better track of what's going on in your code!
my_income = 100

tax_rate = 0.1

my_taxes = my_income*tax_rate

# Show my taxes!
print(my_taxes)
