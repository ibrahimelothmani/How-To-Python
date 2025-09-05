# Challenge: Implement Bubble Sort Algorithm

array = [20, 30, 50, 40, 60, 90, 70, 80, 10, 100]

length = len(array)

for i in range(length):
    for j in range(length - 1 - i):
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]
print(array)
