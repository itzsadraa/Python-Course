# Print charecters from a string that a present at an even index

str = "HelloWorld!"

# loop from 0 to length of str
for even_index in range(len(str)):
    # find even index
    if even_index % 2 == 0:
        print(f"'{str[even_index]}'", end=" ")
