# Printing output to console
print(True)
print(12) # new line by new print statement
print(3.14)

print(8)
print(13, end=" ") # stop the skip to new line
print(21)
print(5+3/2)

"""
Can add SPACE using
comma in print
"""
print("Hello Universe!", "This is Ashitabh Srivastava learning PYTHON programming language.")
print('Both single and double quotes are used to print strings')

# Taking input from user
x = input() # assumes input in string
print("Hello", x)

num = int(input()) # converts input to take integer
print("The Entered Number's Square:", num*num)

a, b, c, d = input().split() # taking multiple inputs (separated by spaces)
print(d, c, b, a)

a, b, c = map(int, input().split()) # converting multiple to int inputs
d, e = map(int, input().split()) # inputs after new line
print(a + b + c + d + e)