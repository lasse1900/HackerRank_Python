# name = int(input())                  # Reading input from STDIN
# annettu_numero = int(input())
# print('Hi, %s.' % tulo)         # Writing output to STDOUT


def tulosta_tulo(n):
  tulo = 1
  for i in range(1, n + 1):
    tulo *= i
  return tulo


if __name__ == "__main__":
  n = int(input())
  print(tulosta_tulo(n))
