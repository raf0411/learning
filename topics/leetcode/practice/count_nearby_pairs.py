
def count_nearby_pairs(numbers, max_gap):
  count = 0

  for current_index, current_value in enumerate(numbers):
    for other_index, other_value in enumerate(numbers):
      if current_index == other_index:
        continue
      
      if max_gap >= abs(current_value - other_value):
        count += 1
				
  return count

print(count_nearby_pairs([1, 3, 4, 6], 2))