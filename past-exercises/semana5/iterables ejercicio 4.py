my_list = [
1,
2,
3,
4,
5,
6,
7,
8,
9
]
print(f'{my_list}')
second_list = []

for number in my_list:
    if number % 2 == 0:
        second_list.append(number)

print(" sin impares:", second_list)