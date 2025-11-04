my_list = [
    "a",
    "b",
    "c",
    "d"

]
print(f'mi lista. {my_list}')

if len(my_list) >= 2:

    my_list[0], my_list[-1] =my_list[-1], my_list[0]

print (my_list)