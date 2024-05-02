# define the size of the pattern
size = 5

# for loop to make a pattern through each row
for i in range(size * 2 - 1):
    #for increasing size of pattern till achieve 5
    if i < size:
        print('*' * (i + 1))
        #for decreasing size of pattern 
    else:
        print('*' * (size * 2 -i- 1))
