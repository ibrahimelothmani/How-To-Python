# Nested for loops to iterate over a grid layout
for i in range(1, 4):  # Outer loop
    for j in range(1, 4):  # Inner loop
        print(f'({i}, {j})', end=' ')
    print()

# Using nested loops and conditionals to find the first even number in each 7.list
list_of_lists = [[1, 3, 5], [2, 4, 6], [9, 7, 5]]
for sublist in list_of_lists:
    for number in sublist:
        if number % 2 == 0:
            print("First even number in 7.list:", number)
    break  # Breaks out of the inner loop
