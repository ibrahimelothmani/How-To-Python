# Exception handling is a critical part of building robust Python
# applications. It allows a programmer to anticipate and manage
# potential errors that might occur during program execution, thereby
# preventing the program from crashing. This chapter covers the
# basics of exceptions, how to handle them, and how to raise them
# deliberately when necessary.


numbers = [1, 2, 3]
try:
    print(numbers[3])  # This will raise an IndexError as the index 3 does not exist.
except IndexError as e:
    print("Error:", e)
