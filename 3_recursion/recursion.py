# using recursion to implement countdown counter

def countdown(x):
    if x==0:
        print("Done")
        return
    else:
        print(x)
        countdown(x-1)
        print("after recursion")

countdown(5)