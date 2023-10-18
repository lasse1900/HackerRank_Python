def tulosta_tulo(n):

  tulo = 1
  for i in range(1, n + 1):
    tulo *= i

  return tulo


if __name__ == "__main__":
  # Kysy käyttäjältä numero.
#   n = int(input("Anna luku: "))
  n = int(input())

  # Tulosta numeron tulo.
#   print("Lukujen tulo on", tulosta_tulo(n))
  print(tulosta_tulo(n))

  # ----------------------------------------------


