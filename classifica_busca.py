#metodo de ler arquivo com CSV
import csv

def carrega_busca():

    arquivo = open('busca.csv')

    leitor = csv.reader(arquivo)
    next(leitor)
    
    X = []
    Y = []

    for home,busca,logado,comprou in leitor:
        X.append([int(home),busca, int(logado)])
        Y.append(int(comprou))
    
    return X,Y

#agora no modo PANDAS
import pandas as pd
from sklearn.naive_bayes import MultinomialNB
data_frame = pd.read_csv('busca.csv')

X = data_frame[['home', 'busca', 'logado']]
Y = data_frame['comprou']

Xdummies = pd.get_dummies(X)
Ydummies = Y

X = Xdummies.values
Y = Ydummies.values

porcentagem_treino = 0.9
porcentagem_teste = 0.1

tamanho_treino = porcentagem_treino * len(X)
tamanho_teste = porcentagem_teste * len(Y)

treina_dados = X[:tamanho_treino]
treina_marcacoes = Y[:tamanho_treino]

testa_dados = X[-tamanho_teste:]
testa_marcacoes = Y[-tamanho_teste:]

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