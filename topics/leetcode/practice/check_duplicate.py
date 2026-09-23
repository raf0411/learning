numbers = [4, 1, 3, 1, 2]
numbers2 = [4, 1, 2]
numbers3 = [4]
numbers4 = []

def checkDuplicate(numbers):
  for current_index, current_value in enumerate(numbers):
    for other_index, other_value in enumerate(numbers):
      if current_index == other_index:
        continue
      if current_value == other_value:
          return True

  return False

print(checkDuplicate(numbers))
print(checkDuplicate(numbers2))
print(checkDuplicate(numbers3))
print(checkDuplicate(numbers4))

def check_duplicate_fast(numbers):
  seen_numbers = set()

  for number in numbers:
    if number in seen_numbers:
      return True
    
    seen_numbers.add(number)

  return False

print(check_duplicate_fast([4, 1, 3, 1, 2]))
print(check_duplicate_fast([4, 1, 2]))
print(check_duplicate_fast([4]))
print(check_duplicate_fast([]))