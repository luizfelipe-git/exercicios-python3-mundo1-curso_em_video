metros = float(input("Digite a distância em metros: "))

print("\nA medida de {} metros corresponde a: ".format(metros))

print("\n{}km".format(metros/1000))
print("{}hm".format(metros/100))
print("{}dam".format(metros/10))
print("{}dm".format(int(metros*10)))
print("{}cm".format(int(metros*100)))
print("{}mm".format(int(metros*1000)))