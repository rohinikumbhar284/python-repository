ef exponent(base, exp):
    result = 1
    for _ in range(exp):
        result *= base
    return result

# Example usage:
print(exponent(2, 3))  # Output: 8
print(exponent(5, 4))