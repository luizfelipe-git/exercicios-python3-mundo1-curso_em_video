digitado = input("Digite algo: ")

print("\nTipo de Dado:", type(digitado))
print("Quantidade de Caracteres:", len(digitado))
print("Possui números?:", digitado.isnumeric())
print("Possui letras?:", digitado.isalpha())
print("Possui números e letras?:", digitado.isalnum())
print("Possui espaços?:", digitado.isspace())

print("Possui letras maiúsculas?:", digitado.istitle())
print("Está em maiúsculas?:", digitado.isupper())
print("Está em minúsculas?:", digitado.islower())
