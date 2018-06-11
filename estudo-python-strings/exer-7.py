
import math


nome = input()
reverso = nome[::-1]
print(reverso)

resultado = ""

for i in "reinoldo":
    resultado = i + resultado

print(resultado.upper())

helper = ""
for i in "reinoldo":
    helper = helper + i
    print(helper.upper())
