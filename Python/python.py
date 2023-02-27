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
#***********************************************************************************************************************


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
#************************************************************************************************************************


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
#************************************************************************************************************************


# Exercise nr.4
# Write a program to remove characters from a string starting from zero up to n and return a new string.
def remove_chars(text, n):
    print('Original string: ', text)
    z = text[n:]
    return z

print("Removing characters from a string")
print(remove_chars('python', 4))
print(remove_chars('python', 2))
#************************************************************************************************************************

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