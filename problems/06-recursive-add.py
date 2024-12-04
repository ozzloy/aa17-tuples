# Create a recursive function that takes a tuple as an argument and
# returns the summed values in the tuple.


# Write your function here.
def recursive_add(tup):
    # if the collection has 0 things, return 0
    # otherwise,
    # return the one thing plus the sum of all the other things
    if len(tup) == 0:
        return 0
    else:
        return tup[0] + recursive_add(tup[1:])


print(recursive_add((2,)))  # > 2
print(recursive_add((2, 4, 6, 8, 10)))  # > 30
print(recursive_add((25, 50, 75, 100)))  # > 250
