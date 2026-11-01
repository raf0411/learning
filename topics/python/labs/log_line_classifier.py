def is_error(log_line):
  return log_line.startswith("ERROR ")

print(is_error("ERROR disk full"))
print(is_error("INFO service started"))
print(is_error("ERRORS are increasing"))