# ASSIGNMENT 04:

# Q1) Python Program to count unique values inside a list:

def unique_values(lst):
    # Empty Dictionary
    new_dict = {}

    for value in lst:
        if value in new_dict:
            new_dict[value] += 1
        else:
            new_dict[value] = 1

    for key, value in new_dict.items():
        print(f"{key}: {value} times")


my_list = [0, 3, 1, 7, 2, 4, 0, 6, 2, 7, 8, 9, 9]
unique_values(my_list)


# Q2) With a given integral number n, write a program to generate a dictionary
# that contains (i, i*i) such that is an integral number between 1 and n
# (both included). and then the program should print the dictionary.

def squares_generation(n):
    # squares is a dict
    squares = {i: i*i for i in range(1, n+1)}
    return squares


n = int(input("Enter a number (n): "))
# result is dict
result = squares_generation(n)

print("Generated dictionary:")
print(result)


# Q3) Python program to display the sum of n numbers using a list

def sum_of_numbers(n):
    # nums is an empty list
    nums = []

    for x in range(n):
        number = float(input(f"Enter No. {x + 1}: "))
        nums.append(number)

    total = sum(nums)
    print(f"Sum of {n} nums: {total}")


n = int(input("Enter Value Of n: "))
sum_of_numbers(n)


# Q4) Python program to print the Fibonacci series

def fibonacci(n):
    fib_series = [0, 1]

    for x in range(2, n):
        next_number = fib_series[-1] + fib_series[-2]
        fib_series.append(next_number)

    return fib_series


n = int(input("Enter number of terms in Fibonacci series: "))
result = fibonacci(n)

print(f"Fibonacci series with {n} terms is ")
print(result)


# Q5) Write a Python program to read a file line by line and store it in a
# list.

def read_file_lines(file_name):
    lines = []

    with open(file_name, 'r') as file:
        for line in file:
            lines.append(line.strip())  # strip() removes leading and trailing whitespaces

    return lines


file_name = input("Enter the filename to read: ")
lines = read_file_lines(file_name)

print(f"Contents of '{file_name}' stored in a list:")
for line in lines:
    print(line)


# Q6) Write a Python program to copy the contents of a file to another file

def copy_file(source_filename, destination_filename):
    source_file = open(source_filename, 'r')
    destination_file = open(destination_filename, 'w')

    content = source_file.read()
    destination_file.write(content)

    source_file.close()
    destination_file.close()

    print(f"Contents of '{source_filename}' copied to '{destination_filename}' successfully.")


source_file = input("Enter the source filename: ")
destination_file = input("Enter the destination filename: ")

copy_file(source_file, destination_file)


# Q7) Write a Python program to create a file where all letters of the English
# alphabet are listed by a specified number of letters on each line.

def alphabet_file(line_size, file_name):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    with open(file_name, 'w') as file:
        for x in range(0, len(alphabet), line_size):
            line = alphabet[x:x+line_size]
            file.write(line + '\n')


line_size = int(input("Enter the number of letters per line: "))
file_name = input("Enter the filename to save the alphabet: ")

alphabet_file(line_size, file_name)
print(f"The alphabet has been saved to the file '{file_name}'.")
