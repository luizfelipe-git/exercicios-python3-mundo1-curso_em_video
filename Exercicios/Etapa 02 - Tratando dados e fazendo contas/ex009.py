numero = int(input("\nDigite um número para ver a tabuada: "))
inicio = 1

# ABORDAGEM 1 - Usando While
print("----------------------")
while inicio <= 10:
   print("{} x {} = {}".format(numero, inicio, numero * inicio))
   inicio = inicio + 1
print("----------------------")


# ABORDAGEM 2 - Usando For
print("----------------------")
for inicio in range(1, 11):
   print("{} x {} = {}".format(numero, inicio, numero * inicio))
print("----------------------")