# name = int(input())                  # Reading input from STDIN
annettu_numero = int(input())
# print('Hi, %s.' % tulo)         # Writing output to STDOUT

# Tarkistetaan, että annettu numero on positiivinen
if annettu_numero <= 0:
    print("Syötetyn numeron tulee olla positiivinen kokonaisluku.")
else:
    tulo = 1  # Alustetaan tulo yhteen

    for i in range(1, annettu_numero + 1):
        tulo *= i  # Kertoo tuloa i:llä

    print(tulo)