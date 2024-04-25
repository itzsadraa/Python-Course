# Check Palindrome Number
# A palindrome number is a number that is the same after reverse. For example, 545, is the palindrome numbers

# define number
num = 545

# check if number is equal to its reversed
print(True if str(num) == str(num)[::-1] else False)
