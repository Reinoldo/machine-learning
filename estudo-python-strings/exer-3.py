
def numeroPalavras(frase):    
    palavras = frase.split(" ")
    return len(palavras)    

frase = "era uma vez um castelo cor de rosa"


def subtituirPorHash(frase):
    return frase.replace(" ", "#")


# def palindromo(string1, string2):
#     helper1 = []
#     helper2 = []

#     for i in len(string1):
#         helper1.append(i)

#     print(helper1)
#     for i in len(string2):
#         helper2.append(i)

#     print(helper2)
#     contador = len(string1)
#     reverso = 0
#     while(contador < len(string1) ):
#         if (helper1[contador] == helper2[reverso]):
                
#             contador -= - 1
#             reverso +=1


##palindromo('amor', 'roma')
print(numeroPalavras(frase))

print(subtituirPorHash(frase))