# Print the following pattern
'''
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
'''

# define number
last_num = 5

# loop from 1 to the last number
for num in range(1, last_num + 1):
    print((str(num) + ' ') * num)
