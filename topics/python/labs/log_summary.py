lines = []

total = 0
errors = 0

for line in lines:
  total += 1

  if line.startswith("ERROR "):
    errors += 1

print("Total:", total)
print("Errors:", errors)
