# using Hashtable to filter out duplicate items


items = ["pear", "banana", "apple", "apple", "apple", "orange", "orange", "orange"]

# create a Hashtable
filter = dict()

# loop over each item and add to the hashtable
for key in items:
    filter[key] = 0

# create a set from the resulting keys in the hashtable
result = set(filter.keys())

print(result)