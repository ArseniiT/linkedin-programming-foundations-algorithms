# using recursion to impllement factorial

def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)

# test the factorial function
print("{}! is {}".format(4, factorial(4)))
print("{}! is {}".format(0, factorial(0)))