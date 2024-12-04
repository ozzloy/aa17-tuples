# Create a function that takes in a tuple of strings. It should return a  tuple
# including only the strings that are greater than 8 letters in length.

# Write your function here.

def big_words(words):
    lst = []
    for word in words:
        if len(word) > 8:
            lst.append(word)
    return tuple(lst)

# print(tuple((x * 3 for x in (1, 2, 3))))

def big_words2(words):
    return tuple([word + 'ly' for word in words if len(word) > 8])

# print(big_words(('earth', 'jupiter', 'mars', 'neptune'))) #> ()
print(big_words2(('wakanda', 'melbourne', 'london', 'france'))) #> ('melbourne',)
# print(big_words(('app', 'academy', 'app academy', 'xylophone'))) #> ('app academy', 'xylophone')