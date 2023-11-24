# using Hashtable to count individual items


items = ["pear", "banana", "apple", "apple", "apple", "orange", "orange", "orange"]

# create a Hashtable
counter = dict()

# loop over each item and increment the count for each one
for key in items:
    if key in counter.keys():
        counter[key] += 1
    else:
        counter[key] = 1


print(counter)