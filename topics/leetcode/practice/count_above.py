def count_above(numbers, threshold):
  counter = 0

  for number in numbers:
    if number > threshold:
      counter += 1

  return counter

print(count_above([2, 5, 5, 8], 5))
print(count_above([], 5))
print(count_above([5, 5, 5], 5))