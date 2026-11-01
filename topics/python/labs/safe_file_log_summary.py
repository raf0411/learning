log_path = "/Users/raffi/Learning/topics/python/labs/sample.log"

total = 0
errors = 0

try:
    with open(log_path, encoding="utf-8") as log_file:
        for line in log_file:
          total += 1
          if line.startswith("ERROR "):
            errors += 1
except FileNotFoundError:
    print("Error: log file not found")
else:
    print("Total:", total)
    print("Errors:", errors)