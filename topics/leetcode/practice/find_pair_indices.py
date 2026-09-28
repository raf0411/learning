def find_pair_indices(numbers, target):
    dict = {}

    for idx, current in enumerate(numbers):
      needed_partner = target - current
      
      if needed_partner in dict:
        return [dict[needed_partner], idx]

      dict.update({current: idx})
      
    return []

print(find_pair_indices([4,2,1], 6))
print(find_pair_indices([2,2,1], 5))
print(find_pair_indices([3], 6))
print(find_pair_indices([3,3,1], 6))
