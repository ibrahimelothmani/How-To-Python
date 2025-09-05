# Functions and modules are fundamental for structuring and
# organizing Python code, especially as your projects grow in
# complexity. Functions allow you to encapsulate logic into reusable
# blocks of code, while modules help you organize these functions and
# other elements into separate files. This chapter will guide you
# through creating functions, using parameters and return values, and
# importing modules to enhance the functionality of your Python scripts

def greet():
    print("Hello, welcome to Python!")


# Calling the function
greet()


def add_numbers(num1, num2):
    result = num1 + num2
    return result


# Calling the function with parameters
sum_result = add_numbers(10, 15)
print("Sum:", sum_result)


# Using Default Parameters and Keyword Arguments:

def describe_pet(pet_name, animal_type='dog'):
    print(f"I have a {animal_type} named {pet_name}.")


# Calling function with default parameter
describe_pet(pet_name='Rex')
# Calling function with both parameters explicitly
describe_pet(pet_name='Whiskers', animal_type='cat')
