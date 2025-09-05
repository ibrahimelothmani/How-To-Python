# Type conversion in Python refers to converting one data type into
# another. This is also known as “type casting”. Python provides
# several built-in functions that allow you to perform explicit type
# conversion.

# Converting integer to float
num_int = 10
num_float = float(num_int)
print(num_float)  # Output: 10.0
# Converting float to integer
num_float = 9.8
num_int = int(num_float)
print(num_int)  # Output: 9 (note the truncation, not rounding)
# Converting integer to string
num_int = 300
num_str = str(num_int)
print(num_str)  # Output: '300'
# Converting string to integer
num_str = "201"
num_int = int(num_str)
print(num_int)  # Output: 201

# => Type conversion is especially important when you need to perform
# operations that require uniform data types, such as arithmetic
# operations. Additionally, when receiving input from a user, it is often
# returned as a string, and you may need to convert this into a number
# (int or float) to perform calculations.
# By understanding how to use variables and manipulate different data
# types, you can begin to write more complex and dynamic Python
# programs. This chapter sets the foundation for dealing with all sorts
# of data processing tasks in later chapters.
