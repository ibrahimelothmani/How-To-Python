# lists : are mutable, ordered sequences of elements
# lists : can contain elements of different data types
# lists : are defined using square brackets []
# lists : support indexing and slicing
# lists : support various methods for manipulation (append, remove, pop, etc.)

if __name__ == "__main__":
    # Creating a list
    my_list = [1, 2, 3, 'four', 'five', 6.0]
    print("Original List:", my_list)
    # Accessing elements
    print("First Element:", my_list[0])  # Output: 1
    print("Last Element:", my_list[-1])  # Output: 6.0
    # Slicing
    print("Sliced List (1:4):", my_list[1:4])  # Output: [2, 3, 'four']
    # Modifying elements
    my_list[3] = 4
    print("Modified List:", my_list)  # Output: [1, 2, 3, 4, 'five', 6.0]
    # Appending elements
    my_list.append('six')
    print("Appended List:", my_list)  # Output: [1, 2, 3, 4, 'five', 6.0, 'six']
    # Removing elements
    my_list.remove('five')
    print("List after Removal:", my_list)  # Output: [1, 2, 3, 4, 6.0, 'six']
    # Popping elements
    popped_element = my_list.pop()
    print("Popped Element:", popped_element)  # Output: 'six'
    print("List after Popping:", my_list)  # Output: [1, 2, 3, 4, 6.0]
    # Length of the list
    print("Length of List:", len(my_list))  # Output: 5
    # Iterating through the list
    print("Iterating through the list:")
    for item in my_list:
        print(item)
