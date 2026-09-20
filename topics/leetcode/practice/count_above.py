def count_above(numbers, threshold):
    count = 0

    for number in numbers:
        if number > threshold:
            count += 1

    return count


# Add your test calls below. Predict each result before running the file.
