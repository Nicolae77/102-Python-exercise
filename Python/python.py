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





