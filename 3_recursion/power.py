# using recursion to impllement power function

def power(x, pwr):
    if pwr == 0:
        return 1
    else:
        return x * power(x, pwr-1)

# test the power function
print("{} to the power of {} is {}".format(5,3,power(5,3)))
print("{} to the power of {} is {}".format(1,5,power(1,5)))