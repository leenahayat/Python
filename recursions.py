# 5 * factorial(4)
# 5 * 4 * factorial(3)
# 5 * 4 * 3 * factorial(2)
# 5 * 4 * 3 * 2 * factorial(1)
# 5 * 4 * 3 * 2 * 1
# factorial(n) = n * factorial(n-1)


def factorial(n):
  if (n == 0 or n == 1):
    return 1
  else:
    return n * factorial(n - 1)

print(factorial(5))



# Quick Quiz: Write a program to print the Fibonacci sequence
# f(n) = f(n-1) + f(n-2)

def fibseq(z):
  if(z == 0):
    return 0
  elif(z == 1):
    return 1
  else:
    return fibseq(z-1)+fibseq(z-2)

u = 10

for i in range(u):
  print(fibseq(i), end=" ")
     