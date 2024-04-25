# Print the sum of the current number and the previous number
# Write a program to iterate the first 10 numbers, and in each iteration, print the sum of the current aand previous number.

# previous number
pre_num = 0

# loop from 1 to 10
for number in range(1, 11):
    sum = pre_num + number
    print(f"Current = {number}, Previous = {pre_num}, Sum = {sum}")

    # modify previous number
    pre_num = number
