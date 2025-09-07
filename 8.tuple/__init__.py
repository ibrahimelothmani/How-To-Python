# tuple : A built-in data type in Python that represents an immutable ordered collection of items.
# tuple : Tuples are similar to lists, but unlike lists, tuples cannot be modified after their creation (i.e., they are immutable).
# tuple : Tuples are defined using parentheses ().
# tuple : Tuples can contain elements of different data types.
# tuple : Tuples support indexing and slicing, similar to lists.
# tuple : Tuples support various methods for accessing elements, but do not support methods that modify the tuple (like append, remove, etc.).
# tuple : Tuples are often used to group related data together and can be used as keys in dictionaries due to their immutability.
if __name__ == "__main__":
    # Creating a tuple
    my_tuple = (1, 2, 3, 'four', 'five', 6.0)
    print("Original Tuple:", my_tuple)
    # Accessing elements
    print("First Element:", my_tuple[0])  # Output: 1
    print("Last Element:", my_tuple[-1])  # Output: 6.0
    # Slicing
    print("Sliced Tuple (1:4):", my_tuple[1:4])  # Output: (2, 3, 'four')
    # Tuples are immutable, so we cannot modify elements directly
    try:
        my_tuple[3] = 4
    except TypeError as e:
        print("Error:", e)  # Output: 'tuple' object does not support item assignment
    # Tuples do not support methods that modify the tuple
    try:
        my_tuple.append('six')
    except AttributeError as e:
        print("Error:", e)  # Output: 'tuple' object has no attribute 'append'
    # Length of the tuple
    print("Length of Tuple:", len(my_tuple))  # Output: 6
    # Iterating through the tuple
    print("Iterating through the tuple:")
    for item in my_tuple:
        print(item)
    # Tuples can be used as keys in dictionaries
    my_dict = {my_tuple: "This is a tuple key"}
    print("Dictionary with Tuple Key:", my_dict)
    # Unpacking a tuple
    a, b, c, d, e, f = my_tuple
    print("Unpacked Tuple:", a, b, c, d, e, f)
    # Nested tuples
    nested_tuple = (1, (2, 3), (4, (5, 6)))
    print("Nested Tuple:", nested_tuple)
    print("Accessing Nested Tuple Element:", nested_tuple[2][1][0])  # Output: 5
    # Tuple with single element
    single_element_tuple = (42,)
    print("Single Element Tuple:", single_element_tuple)  # Output: (42,)
    print("Type of Single Element Tuple:", type(single_element_tuple))  # Output: <class 'tuple'>
    not_a_tuple = (42)
    print("Not a Tuple:", not_a_tuple)  # Output: 42
    print("Type of Not a Tuple:", type(not_a_tuple))  # Output: <class 'int'>
