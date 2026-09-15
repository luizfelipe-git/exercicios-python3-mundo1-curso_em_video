salario = float(input("Salário do Funcionário: R$"))

# ABORDAGEM 1 - Calculo Direto
# novo_salario = salario * 1.15

# ABORDAGEM 2 - Calculo Indireto
aumento = salario * 0.15
novo_salario = salario + aumento

print("Considerando aumento de 15%,")
print("O Salário de R${:.2f}, passa a ser R${:.2f}.".format(salario, novo_salario))