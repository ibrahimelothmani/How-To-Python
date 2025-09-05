# max value

def max_value(lst):
    if not lst:
        return None
    max_val = lst[0]
    for num in lst:
        if num > max_val:
            max_val = num
    return max_val


# Example usage:
print(max_value([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]))  # Output: 9
