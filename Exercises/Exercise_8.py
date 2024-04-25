# Create a new list from two list using the following condition
# Given two list of numbers, write a program to create a new list such that the new list should contain odd numbers from the first list and even numbers from the second list

# define first list and second list
f_list = [23, 13, 60, 100]
s_list = [102, 1403, 25, 12]

# create an empty list
new_list = []

# loop through both lists
for num in f_list:
    # add odd numbers
    if num % 2 != 0: new_list.append(num)

for num in s_list:
    # add even numbers
    if num % 2 == 0: new_list.append(num)

print(sorted(new_list))
