def largest_number(numbers):
    # This exercise assumes numbers contains at least one number.
    current_largest_number = numbers[0]
    for number in numbers:
        if current_largest_number < number:
            current_largest_number = number

    return current_largest_number


if __name__ == "__main__":
    # Predict each output before running this file.
    print(largest_number([4, 1, 7, 3, 7]))
    print(largest_number([-8, -3, -10]))
    print(largest_number([5]))
    print(largest_number([9, 2, 9]))
