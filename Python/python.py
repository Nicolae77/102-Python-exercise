# ------------------------------- List, Tuple, Sets, and Dictionaries --------------------------
# List, can be modified
list = [1, 2, 3]
print(list[0])

# Tuple, can't be modified
tuple = (1, 2, 3)
print(tuple[1])
# tuple with single item, remember comma at the end.
tuple = (1,)

# Sets, you can add and remove elements from sets
# but, you can't have duplicate elements and has not order.
sets = {1, 2, 3}
print(sets)
print(len(sets))
for i in sets:
    print(i, end=' ')

# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
dictionary = {
    "brand": "Mercedes",
    "model": "E Class",
    "year": 2021
}
print(dictionary)
print(dictionary.keys())
print(dictionary.values())



# Exercise nr.1
# Use two integer numbers: if their substracting is negative return the result,othervise return their sum.
def substrct_or_sum(num1, num2):
    substract = num1 - num2
    if substract < 0:
        return substract
    else:
        return num1 + num2
    
# first condition
result = substrct_or_sum(10, 11)
print('The result is:', result)
# second condition
result = substrct_or_sum(10, 9)
print('The result is:', result)


# Exercise nr.2
# Write a program to iterate the first numbers and in each iteration, print the sum of the current and previous number.
print('Printing the curent and previous number sum in a range (5)')
previus_num = 0
# loop from 1 to 5
for i in range(0, 6):
    num_sum = previus_num + i
    print('Curent number', i , 'Previous number', previus_num, 'Sum: ', num_sum)
    # modify previous number and set it to the current number
    previus_num = i



# Exercise nr.3
# Print characters from a string that are present at even index number.
user_input = input('Enter your word: ')
print('Original String is: ', user_input)

#get the length of a string
size_input = len(user_input)
# first method
# iterate a each character of a string
# start: 0 to start with first character
# stop: size-1 because index starts with 0
# step: 2 to get the characters present at even index like 0, 2, 4
print('Printing only even index char')
for i in range(0, size_input - 1, 2):
    print("index[", i, "]", user_input[i])

#second method
# using list slicing
# convert string to list
# pick only even index chars
x = list(user_input)
for i in x[0::2]:
    print(i)



# Exercise nr.4
# Write a program to remove characters from a string starting from zero up to n and return a new string.
def remove_chars(text, n):
    print('Original string: ', text)
    z = text[n:]
    return z

print("Removing characters from a string")
print(remove_chars('python', 4))
print(remove_chars('python', 2))


# Exercise nr.5
# Check if the first and last number of a list is the same.


def check_num(numberList):
    print('List number is', numberList)

    first_num = numberList[0]
    last_num = numberList[-1]

    if first_num == last_num:
        return True
    else:
        return False

list_one = [1, 2, 3, 4, 5, 1]
print('Result is', check_num(list_one))

list_two = [5, 10, 15, 20, 25, 30]
print('Result is', check_num(list_two))


# Exercise nr.6
# Display numbers divisible by 2 from a list

list_num = [1, 2, 3, 4, 5, 6, 7, 8]
print('Divisible by 2')
for num in list_num:
    if num % 2 == 0:
        print(num)


# Exercise nr.7
# Write a program to find how many times "Python" appears in the given message.
msg = "Python is the best. With Python you can develop a cool web app. Python."
result = msg.count("Python")
print('Python appears', result, 'times')


# Exercise nr.8
for num in range(10):
    for i in range(num):
        print(i, end=" ")
    print("\n")

for num in range(10):
    for i in range(num):
        print(num, end=" ")
    print("\n")
    


# Exercise nr.9
# Write a program to check if given number ia a palindrome number.
# A Palindrome number is a number same after reverse. ex: 343, is the polindrome numbers.
def palindrome(number):
    print("original number", number)
    original_num = number
    
    # reverse the given number
    reverse_num = 0
    while number > 0:
        reminder = number % 10
        reverse_num = (reverse_num * 10) + reminder
        number = number // 10
        print(reverse_num)

    # check numbers
    if original_num == reverse_num:
        print("Given number palindrome")
    else:
        print("Given number is not palindrome")

palindrome(121)
palindrome(125)


# Exercise nr.10
# Given a two list of numbers, write a program to create a new list such that new list should contain odd numbers from first list and even numbers from the second list.

def check_num(lst1, lst2):
    new_list = []

    # iterate first list
    for num in lst1:
        # check if current number is odd
        if num % 2 != 0:
            # add odd number to the new_list
            new_list.append(num)

    # iterate second list
    for num in lst2:
        # check if current number is even
        if num % 2 == 0:
            new_list.append(num)
    return new_list

lst1 = [1, 2, 3, 4, 5, 6]
lst2 = [20, 21, 22, 23, 24]
print('Result list: ', check_num(lst1, lst2))


# Exercise nr.11
# Write a program to reverse an integer.
number = 7536
print("Given number", number)
print('Reversed is: ')
while number > 0:
    # get the last digit
    digit = number % 10
    # remove the last digit and repeat the loop
    number = number // 10
    print(digit, end="")
    


# Exercise nr.12
# Print multiplication table form 1 to 10.
print()
for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, end=" ")
    print("\t\t")


# -------------------------Python Input exercise-------------------------

# Exercise nr.13
# Write a program to accept two numbers from the user and calculate multiplication
num1 = int(input('Enter first num: '))
num2 = int(input('Enter second num: '))
result = num1 * num2
print('Multiplication is: ', result)


# Exercise nr.14
# Display float number with 2 decimal.
num = 23.94857674
print('%.2f' % num)


# Exercise nr.15
# Accept a list of 4 folat numbers as an input from the user.
numbers = []
# 4 is the list size
# run loop 4 times
for i in range(0, 4):
    print("Enter number at location",  i, ":")
    # accept float number from user
    item = float(input())
    # add it to the list
    numbers.append(item)

print("User List:", numbers)


# Exercise nr.16
# Write all content of a given file into a new file by skipping line 5
# read test.txt
with open("test.txt", "r") as fp:
    # read all lines from a file
    lines = fp.readlines()

# open new file in write mode
with open("new_file_txt", "w") as fp:
    count = 0
    # itertate each lines from a test.txt
    for line in lines:
        # skip 5th lines
        if count == 4:
            count += 1
            continue
        else:
            # write current line
            fp.write(line)
        # in each iteration reduce the count
        count += 1


# Exercise nr.17
# Writye a program to take three inputs.
first_name, last_name, address = input("Enter your name, last name and address with space:").split()
print("Your first name: ", first_name)
print("Your last nama: ", last_name)
print("Your address: ", address)


# Exercise nr. 18
# Write a program to accept a number from user and calculate
# the sum of all numbers from 1 to given number.

number = int(input('Enter the number: '))
total = 0

for num in range(1, number+1):
    total += num
print('The sum of all numbers is: ', total)


# Exercise nr. 19
# Write a program to print multiplication table of a given number.

number = int(input('Enter the number: '))

for num in range(1, 11):
    result = num * number
    print(result)

#-------------------------------------------Python Loop -------------
# Exercise nr.20
# Write a program to display the number divisible by 5,
# if the number is greater than 150, then skip it and move to the next number,
# and if the number is greater than 500, then stop the loop.

numbers = [12, 15, 25, 40, 150, 175, 200, 525]
new_num = []
for num in numbers:
    if num > 500:
        break
    elif num > 150:
        continue
    elif num % 5 == 0:
        new_num.append(num)
print(new_num)


# Exercise nr.21
# Write a program to Count the total number of digits in a number

number = 12345678
count = 0
while number != 0:
    # floor division
    # to reduce the last digit from number
    number = number // 10
    # increment counter by 1
    count = count + 1
print("Toatal digits are: ", count)


# Exercise nr.22
# Print list in reverse order using a loop

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
new_list = list(reversed(list1))
print("Initial list is: ", list1)
for item in new_list:
    print(item)
print("Reversed list is: ", new_list)


# Exercise nr.23
# Use else block to display a message "Done" after successful execution of for loop.

for i in range(1, 6):
    print(i)
else:
    print("Done!")


# Exercise nr.24
# Write a program to display all prime numbers within a range
# ex: 29 is a prime number because no other whole number multiply together to make it.


# range
start = 25
end = 50
print("Prime numbers between", start, "and", end, "are: ")
for num in range(start, end+1):
    # all prime numbers are greater than 1
    # if number is less than or equal to 1, it is not prime
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                # not a prime number so break inner loop and
                # look for next number
                break
        else:
            print(num)



# Exercise nr.25
# Display Fibonacci series up to 10 terms

num1 = 0
num2 = 1

print("Fibonacci sequence:")
# run loop 10 times
for i in range(10):
    # print next number of a series
    print(num1, end="  ")
    # add last two numbers to get next number
    res = num1 + num2
    # update values
    num1 = num2
    num2 = res
print(res)


# Exercise nr.26
# Find the factorial of a given number
# ex: 5! = 5 x 4 x 3 x 2 x 1= 120

num = int(input("Enter a number to find it's factorial: "))
factorial = 1
if num < 0:
    print("Factorial does not exist for negative numbers")
elif num == 0:
    print("Factorial of 0 is 1")
else:
    # run loop 
    for i in range(1, num+1):
        # multiply factorial by current number
        factorial = factorial * i
    print("The factorial number of", num, "is", factorial)


# Exercise nr.27
# Calculate the cube of all numbers from 1 to a given number.
number = int(input('Enter the number: '))

for num in range(1, number+1):
    print('Current number is: ', num, 'and the cube is: ', (num * num * num))


    # --------------------------- Python Functions -------------------

# Exercise nr.28
# Write a function with two arguments, name and age, and print their value.
              # parameters
def my_function(name, age):
    # print value
    print(name, age)


# call function
          # arguments
my_function('Bob', 25)


# Exercise nr.29
# Create a function with variable length of arguments. (*args).

def my_function(*args):
    for num in args:
        print(num)


my_function(1, 2, 3, 4, 5)


# Exercise nr.30
# Create a function such that can accept two variables and calculate 
# addition, subtraction, multiplication, ans division.
def my_function(a, b):
    return a + b, a - b, a * b, a / b


add, sub, mul, div = my_function(20, 10)
print('Addition of number is: ', add)
print('Subtraction of number is: ', sub)
print('Multiplication of number is: ', mul)
print('Division of number is: ', div)
        
    
# Exercise nr.31
# Assign different name to function and call it through the new name.

def student(name, age):
    print(name, age)


student('Bod', 23)
new_student = student
new_student('Steve', 34)


# Exercise nr.32
# Generate a Python list of all even numbers between 2 and 20.

lst = []
for i in range(2, 20):
    if i % 2 == 0:
        lst.append(i)
print(lst)


# Exercise nr.33
# Find the largest item from a given list.

x = [4, 6, 32, 24, 12, 2]
for i in x:
    if i == max(x):
        print(i)


# -----------------------------Python String Exercise--------------------
# Exercise nr.34
# Write a program to create a new string made of an input string’s first, middle, and last character.
name = 'Nicolae'
print('Original string is: ', name)
# Get the first character from string
result = name[0]
print(result)
# Get string size
l = len(name)
# Get middle index size
mi = int(l / 2)
print(mi)
# add first and middle character
result = result + name[mi]
print(result)
# Get last character and add it to result
result = result + name[l - 1]
print(result)


# Exercise nr.35
# Write a program to create a new string made of the middle three characters of an input.
def get_middle_three_char(name):
    # get middle index number
    mi = int(len(name) / 2)
    # use string slicing to get result
    result = name[mi - 1:mi + 2]
    print(result)


get_middle_three_char('CaldaNicRasan')
get_middle_three_char('CaldaBgdRasan')



# Exercise nr.36
# Write a program to link two string with join method.
word = 'Python'
word1 = ', Is the best programming language.'
result = ''.join(word + word1)
print(result)


# Exercise:
# Joining with empty separator
lst = ['P', 'y', 't', 'h', 'o', 'n']
print(''.join(lst))

# Joining with string
name = 'Nick'
print("$".join(name))


# Exercise nr.37
# Count all letters, digits, and special symbols from a given string
def find_char_digits_symbols(text):
    char_count = 0
    digit_count = 0
    symbol_count = 0
    for i in text:
        if i.isalpha():
            char_count += 1
        elif i.isdigit():
            digit_count += 1
        else:
            symbol_count += 1
    print(' Chars = ', char_count, '\n', 'Digits = ', digit_count, '\n', 'Symbols =', symbol_count)


text = 'PythonAnywhere123456!£$%^&*'
print("Total counts of Chars, Digits, and Symbols ")
find_char_digits_symbols(text)



# Exercise nr.38
# Write a program to count all characters within a string.
text = 'Pythonanywhere'
# create an empty dictionary for result
dictionary = dict()
for i in text:
    count = text.count(i)
    # add / update the count of a character
    dictionary[i] = count
print('Result is: ', dictionary)


# Exercise nr.39
# Reverse a given string
text = 'Pythonanywhere'
reversed_text = ''.join(reversed(text))
print(reversed_text)


# Exercise nr.40
# Calculate the sum and average of the digits present in a string.

text = 'Python2469@mail.com'
sum = 0
num = 0

for i in text:
    if i.isdigit():
        sum += int(i)
        num += 1
print('Sum is: ', sum)
print('Numbers are: ', num)

average = sum / num
print('Average is: ', average)


# Exercise nr.41
# Remove empty string from a list of string.

lst = ['Python', '', 'Anywhere', '', 'Is', '', 'Cool']
new_lst = []
for i in lst:
    if i != '':
        new_lst.append(i)
print(new_lst)


# Exercise nr.42
# Remove special symbols from a string.

str_ing = '?!/Nick &*is ()developer'

for i in str_ing:
    if i.isalpha():
        print(i, end='')


# -----------------------------Python Data Structure--------------------

# Exercise nr.43
# From two lists l1,l2, write a program to create a third list
# by picking an odd-index element from l1, and even element from l2.
l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
l3 = []
# Start from 1st index with step 2
odd_elements = l1[1::2]
print('Elements at odd-index position from l1 are: ', odd_elements)
# Start from 0 index with step 2
even_elements = l2[0::2]
print('Elements at even-index position from l2 are: ', even_elements)
l3.extend(odd_elements)
l3.extend(even_elements)
print('Third list is: ', l3)


# Exercise nr.44
# Write a program to remove the item at index 2 and add it to the index 0,
# and at the end of the list.
lst = [1, 2, 0, 3, 4, 5, 6, 7, 8, 9]
print('Initial list is: ', lst)
# pop(), Removes and return the item at the given index from the list
element = lst.pop(2)
print('List after removing element at index 2', lst)
# insert(), add the item at the specific position in the list
lst.insert(0, element)
print('List after adding element at index 0', lst)
# append(), add item at the end of the list
lst.append(element)
print('List after adding element at last index', lst)


# Exercise nr.45
# Count the occurrence of each element from a list
lst = [1, 2, 4, 3, 5, 7, 11, 3, 2, 46, 7, 8, 6, 4, 1, 2]
count_dict = dict()

for i in lst:
    if i in count_dict:
        count_dict[i] += 1
    else:
        count_dict[i] = 1

print(count_dict)


# Exercise nr.46
# Create a Python set such that it shows the element from both lists in a pair
lst1 = [1, 3, 5, 7, 9]
lst2 = [2, 4, 6, 8, 10]

result = zip(lst1, lst2)
result_set = set(result)
print(result_set)


# Exercise nr.47
# Find the common of two sets and remove those
# elements from the first set
set1 = {12, 10, 14, 16, 19, 25}
set2 = {13, 19, 34, 25}

common = set1.intersection(set2)
print(common)
for i in common:
    set1.remove(i)
print(set1)


# Exercise nr.48
# Iterate a given list and check if a given element exists as a key’s value
# in a dictionary. If not, delete it from the list
lst = [12, 34, 56, 68, 44]
dct = {'Mike': 12, 'Smith': 44, 'James': 68}

lst = [i for i in lst if i in dct.values()]
print(lst)



# Exercise nr.49
# Get all values  from the dictionary and add them to a list but don’t add duplicates
test = {'Mark': 67, 'Bob': 88, 'Smith': 79, 'Angela': 88, 'Nick': 67, 'Steve': 45}
print(list(test.values()))
test_list = list()
# iterate dict value
for i in test.values():
    # check if value not present in a list
    if i not in test_list:
        test_list.append(i)
print(test_list)


# Exercise nr.50
# Remove duplicates from a list and create a tuple and find the minimum and maximum number
lst = [12, 34, 56, 67, 12, 67, 43, 95, 67, 56]
print('Initial list: ',lst)
# return unique items
uniq_items = set(lst)
print('Unique items are: ', uniq_items)
# create a tuple
t = tuple(uniq_items)
print('Tuple is: ', t)
# calculate min and max of a tuple
print('Minimum number is: ', min(t))
print('Maximum number is: ', max(t))


# -----------------------------Python List Exercise--------------------
# Exercise nr.51
# Reverse a list in Python
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# first solution
reverse_lst = reversed(lst)
print(list(reverse_lst))
# second solution
lst = lst[::-1]
print(lst)


# Exercise nr.52
# Concatenate two lists index-wise

lst1 = ['Ni', 'i', 'web']
lst2 = ['ck', 's', 'developer']
lst3 = [i + j for i, j in zip(lst1, lst2)]
print(lst3)


# Exercise nr.53
# Create a new list to turn every item of a given list into its square
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
square_list = []
for i in numbers:
    square_list.append(i * i)
print(square_list)


# Exercise nr.54
# Remove empty list from the list string

lst1 = ['Steve', '', 'Bob', 'Mark', '', 'John']
lst2 = list(filter(None, lst1))
print(lst2)


# Exercise nr.55
# Write a program to add 50 after 40 in the following list.

lst = [10, 20, 30, [40, [], 60], 70, 80]
print(lst[0])
print(lst[1])
print(lst[2])
print(lst[3])
lst[3][1] = 50
print(lst)


# Exercise nr.56
# Extend nested list by adding the second list in empty list
lst1 = ['Hello', ['My name is', []]]
lst2 = ['Bob']
lst1[1][1].extend(lst2)
print(lst1)


# Exercise nr.57
 # Write a program to find value 70 in the list, and if it is present,
 # replace it with 60.

lst = [10, 20, 30, 40, 50, 70]
# get the occurrence index
idx = lst.index(70)
print(idx)
# update item present at location
lst[idx] = 60
print(lst)

#     OR

lst = [10, 20, 30, 40, 50, 70]
print(lst)
if 70 in lst:
    idx = lst.index(70)
    lst[idx] = 60
    print(lst)


# Exercise nr.58
# Remove all occurrences of a specific item from a list.

lst = [1, 2, 3, 4, 5, 2, 1, 6, 8, 3, 9, 10]
while 1 in lst and 2 in lst and 3 in lst:
    lst.remove(1)
    lst.remove(2)
    lst.remove(3)
print(lst)


# -----------------------------Python Dictionary Exercise----------------

# Exercise nr.59
# Convert two lists into a dictionary
keys = ['Bob', 'Smith', 'Mark']
value = [67, 78, 89]
dictionary_result = dict(zip(keys, value))
print(dictionary_result)
#   OR
new_dict = dict()
for i in range(len(keys)):
    new_dict.update({keys[i]: value[i]})
print(new_dict)


# Exercise nr.60
# Merge two dictionaries into one
dict1 = {'student1': 10, 'student2': 20, 'student3': 30}
dict2 = {'student4': 40, 'student5': 50, 'student6': 60}
dict3 = {**dict1, **dict2}
print(dict3)


# Exercise nr.61
# Print the value of key 'maths' from the following dictionaries
dict_student = {'class': {
    'student': {
        'name': 'Steve',
        'marks': {
            'maths': 70,
            'history': 90
        }
    }
  }
}
print(dict_student['class'])
print(dict_student['class']['student'])
print(dict_student['class']['student']['marks'])
print(dict_student['class']['student']['marks']['maths'])


# Exercise nr.62
# Create a dictionary by extracting yhe keys from a given dictionary
dict1 = {
    'name': 'Mark',
    'address': 'London',
    'age': 34,
    'salary': 1800
}
# keys to extract
keys = ['name', 'age']
# dictionary comprehension
dict2 = {k: dict1[k] for k in keys}
print(dict2)


# Exercise nr.63
# Delete a list of keys from a dictionary
dict1 = {
    'name': 'Mark',
    'address': 'London',
    'age': 34,
    'salary': 1800
}

keys = ['name', 'salary', 'age']

for k in keys:
    dict1.pop(k)
print(dict1)


# Exercise nr.64
# write a program to check if value 10 exists in the following dictionary
dict1 = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
num = 10
if num in dict1.values():
    print(num, 'exist in dict1')


# Exercise nr.65 
# # Write a program to rename a key in the following dictionary
dict1 = {
    'name': 'Mark',
    'address': 'London',
    'age': 34,
    'salary': 1800
}

dict1['city'] = dict1.pop('address')

print(dict1)  


# Exercise nr.66
# Get the key of minimum and maximum value from the following dictionary
dict1 = {
    'Bob': 56,
    'Steve': 62,
    'Mark': 88,
    'John': 91
}

print(min(dict1, key=dict1.get), 'has the minimum value')
print(max(dict1, key=dict1.get), 'has the maximum value')





# -----------------------------Python Set Exercise----------------------

# Exercise nr.67
# Write a program to add a list of element to a set.
#  set
set1 = {'Bob', 'James', 'Steve'}
# list
lst1 = ['Nick', 'John', 'Mark']
set1.update(lst1)
print(set1)


# Exercise nr.68
# Return a new set of identical items from two sets.
set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
set2 = {2, 4, 6, 8}
set3 = set1.intersection(set2)
print(set3)


# Exercise nr.69
# Write a Python program to return a new set with unique
# items from both sets by removing duplicates.
set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
set2 = {2, 4, 6, 8}
set3 = set1.union(set2)
print(set3)


# Exercise nr.70
# Update the first set with items that don’t exist in the second set
set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
set2 = {2, 4, 6, 8}
set1.difference_update(set2)
print(set1)



# -----------------------------Python Tuple Exercise---------------
# Exercise nr.71
# Reverse a tuple
tpl1 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
tpl2 = tpl1[::-1]
print(tpl2)


# Exercise nr.72
# Access value 5 from the tuple
tpl1 = ('Bob', 2, [3, 4, 5], (6, 7, 8, 9))
tpl2 = tpl1[2][2]
print(tpl2)


# Exercise nr.73
# Iterate in tuple
tpl1 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
for i in tpl1:
    print(i, end=' ')


# Exercise nr.74
# Swap two tuples
tpl1 = (10, 20)
tpl2 = (30, 40)
tpl1, tpl2 = tpl2, tpl1
print(tpl1)
print(tpl2)


# Exercise nr.75
# Copy specific elements from one tuple to a new tuple
tpl1 = (1, 2, 3, 4, 5, 6, 7)
tpl2 = tpl1[1]
tpl3 = tpl1[3:-2]
tpl4 = tpl1[2:]
print(tpl2)
print(tpl3)
print(tpl4)


# Exercise nr.76
# Tuple can not be modified, but nested tuple with a list, only list can be modified.
tpl1 = (1, 2, 3, [4, 5, 6, 8], 8, 9)
tpl1[3][3] = 7
print(tpl1)


# Exercise nr.77
# Sort a tuple of tuples by 2nd item
tpl1 = (('b', 2), ('a', 1), ('d', 4), ('c', 3))
tpl1 = tuple(sorted(list(tpl1), key=lambda x: x[1]))
print(tpl1)


# Exercise nr.78
# Counts the number of occurrences of item 10 from a tuple
tpl1 = (10, 20, 30, 40, 50, 10, 60, 10, 20, 10)
total = 0
for i in tpl1:
    if i == 10:
        total += 1
print(total)

# OR
result = tpl1.count(10)
print(result)


# Exercise nr.79
# Check if all items in the tuple are the same
def check(t):
    return all(i == t[0] for i in t)


tpl1 = (77, 77, 77, 77)
print(check(tpl1))




# -----------------------------Python Date and Time Exercise---------------
# Exercise nr.80
# Print current date and time in Python
import datetime
t = datetime.datetime.now()
print(t)





# --------------------------------------Python OOP-------------------------
# Exercise nr.81
# Create a Car class without any variables and methods
class Car:
    pass

# Exercise nr.82
# Create a Class with instance attributes
class Car:
    def __init__(self, model, series, mileage):
        self.model = model
        self.series = series
        self.mileage = mileage


car_detail = Car('BMW', 5, 250000)
print(car_detail.model, 'series', car_detail.series, 'has', car_detail.mileage, 'km')


# Exercise nr.83
# Ex: Object Oriented Programming. 
# Create a Studend class with method.
class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades)


obj1 = Student("Bob", 35, (78, 89, 92))
print(obj1.name, 'has', obj1.age, 'years old.')
print('Average grade is', "%.2f" % obj1.average_grade())

obj2 = Student("Smith", 25, (64, 75, 81))
print(obj2.name, 'has', obj2.age, 'years old.')
print('Average grade is', "%.2f" % obj2.average_grade())


# Exercise nr.84
# Ex: Object Oriented Programming
# Create a Store class with multiple methods
class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        item = {'name': name, 'price': price}
        self.items.append(item)
        return self.items

    def stock_price(self):
        # Add together all item prices in self.items and return the total.
        total = 0
        for item in self.items:
            total += item['price']
        return total


store = Store('JD')
print(store.name)
print(store.add_item('adidas', 12))
print(store.add_item('nike', 22))
print(store.add_item('diesel', 24))
print(store.stock_price())


# Exercise nr.85
# Create a child class Shop,
# that will inherit all of the variables and methods of the Store class
class Store:
    def __init__(self, name, price, size):
        self.name = name
        self.price = price
        self.size = size


store_object = Store('Balenciage', 250, 10)
print(store_object.name, store_object.price, store_object.size)


class Shop(Store):
    pass


shop_object = Shop('Gucci', 420, 9)
print(shop_object.name, shop_object.price, shop_object.size)

# -----------------------------Python JSON Exercise--------------------
# Exercise nr.86
# Convert the following dictionary into JSON
import json
data = {'Bob': 67, 'Mike': 78, 'Steve': 91}

json_data = json.dumps(data)
print(json_data)


# Exercise nr.87
# Access the value of Mike from the following JSON
import json
json_data = """{"Bob": 67, "Mike": 78, "Steve": 91}"""
data = json.loads(json_data)
print(data)
print(data['Mike'])


# Exercise nr.88
# Access the nested key ‘salary’ from the following JSON
import json

data_Json = """{ 
   "company":{ 
      "employee":{ 
         "name":"Mike",
         "pay":{ 
            "salary":5000,
            "bonus":400
         }
      }
   }
}"""

data = json.loads(data_Json)
print(data['company']['employee']['pay']['salary'])
 

# -----------------------------Python NumPy Exercise--------------------
# Exercise nr.89
# Create a 4X3 integer array and Prints its attributes
import numpy

firstArray = numpy.empty([4, 3], dtype=numpy.uint16)
print("Printing Array")
print(firstArray)
print("Printing numpy array Attributes")
print("1> Array Shape is: ", firstArray.shape)
print("2>. Array dimensions are ", firstArray.ndim)
print("3>. Length of each element of array in bytes is ", firstArray.itemsize)


# Exercise nr.90



# -----------------------------Python Pandas Exercise--------------------



# -----------------------------Python Matlib Exercise--------------------



# -----------------------------Random Data Generator Exercise-------------




# -----------------------------Python Database Exercise--------------------

