import self


class NegativeAgeError(Exception):
    """Exception raised when the age is negative."""

    def __init__(self, age):
        self.message = f"Age {age} is not valid. Age cannot be negative."

    super().__init__(self.message)


def check_age(age):
    if age < 0:
        raise NegativeAgeError(age)
    print(f"Age {age} is valid.")


try:
    check_age(-5)
except NegativeAgeError as e:
    print(e)
