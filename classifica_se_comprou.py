from dados import carrega_dados
from sklearn.naive_bayes import MultinomialNB

x, y = carrega_dados()

treina_dados = x[:70]
treina_marcacoes = y[:70]

testa_dados = x[-29:]
testa_marcacoes = y[-29:]

modelo = MultinomialNB()
modelo.fit(treina_dados, treina_marcacoes)




resultado = modelo.predict(testa_dados)

diferencas = resultado - testa_marcacoes

acertos = [d for d in diferencas if d == 0]

total_acertos = len(acertos)
erros = [d for d in diferencas if d!=0]

total_erros = len(erros)
total_elementos = len(testa_dados)


taxa_de_acerto = 100.0 * total_acertos / total_elementos
taxa_de_erro = 100.0 * total_erros / total_elementos


print("taxa de acerto: ",  taxa_de_acerto, "%")
print("taxa de erro: ",taxa_de_erro,"%")
print("total de elementos testados: ",total_elementos)

print(type(diferencas))