total = 0
errors = 0

with open("/Users/raffi/Learning/topics/python/labs/sample.log", encoding="utf-8") as log_file:
  for line in log_file:
    if line.startswith("ERROR "):
      errors += 1
    total += 1

print("Total:", total)
print("Errors:", errors)