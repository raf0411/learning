def has_pair_with_sum(numbers, target):
  for current_idx, current_val in enumerate(numbers):
    for other_idx in range(current_idx + 1, len(numbers)):
      pair_sum = current_val + numbers[other_idx]
      
      if pair_sum == target:
        return True

  return False

print(has_pair_with_sum([5, 1], 6))
print(has_pair_with_sum([1,2], 2))
print(has_pair_with_sum([4], 8))
print(has_pair_with_sum([2, 2], 4))

def has_pair_with_sum_fast(numbers, target):
  seen_numbers = set()

  for n in numbers:
    partner = target - n

    if partner in seen_numbers:
      return True

    seen_numbers.add(n)

  return False

print(has_pair_with_sum_fast([4, 4], 10))
print(has_pair_with_sum_fast([5, 5], 10))
print(has_pair_with_sum_fast([4], 8))
print(has_pair_with_sum_fast([4, 1, 6], 10))