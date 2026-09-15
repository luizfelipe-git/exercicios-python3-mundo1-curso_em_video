celsius = float(input("\nTemperatura em ºC: "))

# ABORDAGEM 1
fahrenheit = (celsius * 1.8) + 32

# ABORDAGEM 2
# fahrenheit = (celsius * (9/5)) + 32

print("A temperatura de {:.1f}ºC corresponde a {:.1f}ºF.".format(celsius, fahrenheit))