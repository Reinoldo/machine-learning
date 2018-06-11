
palavra1 = input()
palavra2 = input()

reverso = palavra1[::-1]

if(reverso == palavra2):
    print("palíndromas mútuas")
else:
    print("não são palíndromas")