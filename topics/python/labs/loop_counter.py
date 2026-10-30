statuses = ["passed", "passed"]

count = 0

for status in statuses:
  if status == "failed":
    count += 1

print(count)