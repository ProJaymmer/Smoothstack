# Coding Exercise 3:
# 1. Write a string that returns just the letter ‘r’ from ‘Hello World’
# For example, ‘Hello World’[0] returns ‘H’.You should write one line of code. Don’t assign a variable name to the string.
print("Hello World"[-3])
# 2. String slicing to grab the word ‘ink’ from the word  ‘thinker’
print("thinker"[2:5])
# S =’hello’, what is the output of h[1]
print("The output will be 'e'.")
# 3. S =’Sammy’ what is the output of s[2:]
print("The output will be 'm'.")
# 4. With a single set function can you turn the word ‘Mississippi’ to distinct character word.
input = "Mississippi"
new_list = []
for x in input:
    new_list.append(x)
print(new_list)
# 5. The word or whole phrase which has the same sequence of letters in both directions is called a palindrome.
palindrome_list = []


def check_palindrome(input):
    if type(input) == int:
        input = str(input)
    for x in input:
        if x != " " and x != "," and x != "!":
            palindrome_list.append(x)
    palindrome_string = ''.join(palindrome_list)
    lower_case = palindrome_string.lower()
    if lower_case == lower_case[::-1]:
        print("Y")
    else:
        print("N")
    palindrome_list.clear()


check_palindrome(3)
check_palindrome("Stars")
check_palindrome("O, a kak Uwakov lil vo kawu kakao!")
check_palindrome("Some men interpret nine memos")
