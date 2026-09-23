def find_smallest(numbers):
  small_num = numbers[0]

  for number in numbers:
    if number < small_num:
      small_num = number

  return small_num

print(find_smallest([5,1,2,3,3,5,4]))
print(find_smallest([-5,  -1,-2,-3,-3,-5,-4]))
print(find_smallest([5]))
