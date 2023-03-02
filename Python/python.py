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







# -----------------------------Python Data Structure--------------------







# -----------------------------Python List Exercise--------------------






# -----------------------------Python Dictionary Exercise----------------





# -----------------------------Python Set Exercise----------------------







# -----------------------------Python Date and Time Exercise---------------





# --------------------------------------Python OOP-------------------------

# Ex:
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



# -----------------------------Python JSON Exercise--------------------


 

# -----------------------------Python NumPy Exercise--------------------





# -----------------------------Python Pandas Exercise--------------------



# -----------------------------Python Matlib Exercise--------------------



# -----------------------------Random Data Generator Exercise-------------




# -----------------------------Python Database Exercise--------------------

