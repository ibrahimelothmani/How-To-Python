from enum import Enum


class Color(Enum):
    RED = "red color "
    GREEN = "green color"
    BLUE = "blue color"


if __name__ == "__main__":
    print("This is a package and cannot be run directly.")

    print("Available colors:")
    for color in Color:
        print(f"{color.name} = {color.value}")
