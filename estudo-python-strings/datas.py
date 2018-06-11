mes_dict = {1: 'janeiro', 2: 'fevereiro', 3: 'março'}

data = '20/03/2000'

dia,mes,ano = data.split("/")

print("Voce nasceu em " + dia + " de " + mes_dict[int(mes)] + " de " + ano + ".")

## tem um jeito melhor de imprimir, mas por hora vai esse...