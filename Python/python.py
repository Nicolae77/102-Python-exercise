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
