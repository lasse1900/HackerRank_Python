def factorial(n):
  if n < 0:
    raise ValueError("n must be a non-negative integer.")
  factorial = 1
  for i in range(1, n + 1):
    factorial *= i
  return factorial

# Example usage:

print(factorial(int(input())))
