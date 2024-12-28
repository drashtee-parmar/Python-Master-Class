def sum_eo(n, t):
    total = 0

    if t == 'e':
        for num in range(2, n, 2):  # Start at 2, step by 2 to get even numbers
            total += num
    elif t == 'o':
        for num in range(1, n, 2):  # Start at 1, step by 2 to get odd numbers
            total += num
    else:
        return -1

    return total


# Example usages:
print(sum_eo(10, 'e'))  # Output: 20
print(sum_eo(7, 'o'))  # Output: 9
print(sum_eo(11, 'spam'))  # Output: -1
