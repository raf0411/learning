numbers = [4, 1, 2, 1, 3]

def checkDuplicate(numbers):
  current_index = 0
  current_value = numbers[current_index]

  for i, number in enumerate(numbers):
    if current_index == i:
      continue
    if current_value == number:
      return True
    else:
      current_index = i

  return False

print(checkDuplicate(numbers))