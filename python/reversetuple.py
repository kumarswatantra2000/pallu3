input_tuple = ('z','a','d','f','g','e','e','k')

list = []

# adding reversed values in a list
for i in reversed(input_tuple):
    list.append(i)

output_tuple = tuple(list) # type cast into tuple

print(output_tuple)
