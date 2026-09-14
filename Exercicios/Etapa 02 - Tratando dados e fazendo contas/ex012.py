produto = float(input("\nQual é o preço do produto? R$"))

# ABORDAGEM 1 - Calculo Direto
# preco = (produto * 0.95)

# ABORDAGEM 2 - Calculo Indireto
desconto = produto * 0.05
preco = produto - desconto

print("O produto que custava R${:.2f}, na promoção com desconto de 5%, irá custar R${:.2f}.".format(produto, preco))