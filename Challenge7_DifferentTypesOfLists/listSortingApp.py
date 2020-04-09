numbers =       [1, 20, 5, 40, 3]

num_ints =      numbers
num_floats =    [float(i/2) for i in numbers]
num_str =   [str(i) for i in numbers]
num_lists = [num_str, num_ints, num_floats]


for list in num_lists:
    print("The variable is a", type(list))
    print("It contains elements:", list)
    print(f"The element {list[0]} is a class", type(list[0]))
    print("\n")


print("\nSorting int and string lists")
print(sorted(num_ints))
print(sorted(num_str))



# num_floats[float(i) for i in numbers]
# print(num_floats)
