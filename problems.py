import random
import string

# Hongtao Chen

# Create a string called 'name' which stores your name
name = 'Hongtao Chen'
# Print the 'name' variable
print(name)
# Create a variable storing an integer
integer = 3
# Create a variable storing a floating point number
FloatingPoint = 1.2
# This line creates a string of 1000000 random letters
rs = ''.join(random.choices(string.ascii_lowercase, k=1000001))
# Print whether your first name (lowercase) appears in the string
print('hongtao' in rs)
# Print the first letter, last letter, and middle letter
print(rs[1])
print(rs[500001])
print(rs[1000000])
# This line creates a string of some random words
rw = ''.join(random.choices(list(string.ascii_lowercase) + [' '], k=1000))
# Print the number of words (a word being characters surrounded by spaces)
count = len(rw.split())
print (count)
# This is a string to be formatted
sentence = 'Hello, my name is Hongtao Chen'
# Print the sentence formatted with your choice of greeting and your name
print(sentence)
# Create a variable storing a tuple of your three favorite numbers
Favorite = (25, 9, 50)
# Assign those three numbers to variables 'a', 'b', and 'c' in one line
a, b, c = (25, 9, 50)
# Create a variable storing None
Nothing = None
# Create a variable, lst, storing a list of the numbers 0-1000 (inclusive)
OneThousand = set(range(0, 1000))
# Print the sum and average of the list
print (sum(OneThousand))
print (sum(OneThousand)/len(OneThousand))
# Create a variable, ascii_low, storing a **set** of all lowercase ascii characters
ascii_low = set(string.ascii_lowercase)
# Create a varaible, ascii_all, storing a **set** of all ascii characters
ascii_all = set(string.ascii_lowercase + string.ascii_uppercase)
# Create a variable, ascii_hi, storing the set different between ascii_all and
# ascii_low, i.e. (ascii_all - ascii_low)
ascii_hi = set(ascii_all - ascii_low)
# Create a dictionary with one key, your first name that maps to one value,
# your last name
Directory = {}
Directory['Hongtao'] = 'Chen'
# Alter the dictionary to make your last name all caps
Directory['Hongtao'] = 'CHEN'
print (Directory['Hongtao'])
# Here is a nested structure
d = {'hello': [[{'cory': 'nezin'}, {'CORY': ['N', 'E', 'Z', 'I', 'N']}]]}
# Change the 'Z' from the list ['N', 'E', 'Z', 'I', 'N'] inside to a 'z'

# Use a for loop to print numbers 1 through 10 (inclusive)
Number = 1
for n in range(1, 11):
    print(n)
# Use a for loop to create a list of the first 10 cubes (0 through 9, cubed)
for n in range(1, 11):
    print(n*n)
# Now use a list comprehension to do the same
Square = [n*n for n in range(1, 11)]
# Write a function 'unique' which takes a list and checks if each element is
# unique, meaning there are no duplicates inside the list.
def unique(List1):
    Unique = []
    NoneUnique = []
    for n in List1:
        if n not in Unique:
            Unique.append(n)
        if n in Unique:
            NoneUnique.append(n)
    Unique = (Unique - NoneUnique)
    print('The unique values are:' + Unique)
    print('The non-unique values are:' + NoneUnique)
    
