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
from collections import Counter

data_frame = pd.read_csv('busca.csv')

X = data_frame[['home', 'busca', 'logado']]
Y = data_frame['comprou']

Xdummies = pd.get_dummies(X)
Ydummies = Y

X = Xdummies.values
Y = Ydummies.values

porcentagem_treino = 0.9
porcentagem_teste = 0.1

tamanho_treino = int(porcentagem_treino * len(X))
tamanho_teste = int(porcentagem_teste * len(Y))

treina_dados = X[:tamanho_treino]
treina_marcacoes = Y[:tamanho_treino]

testa_dados = X[-tamanho_teste:]
testa_marcacoes = Y[-tamanho_teste:]

modelo = MultinomialNB()
modelo.fit(treina_dados, treina_marcacoes)

resultado = modelo.predict(testa_dados)

acertos = (resultado == testa_marcacoes)



total_acertos = sum(acertos)
#erros = [d for d in diferencas if d!=0]

#total_erros = len(erros)
total_elementos = len(testa_dados)

# a eficacia do algoritmo que chuta tudo Sim ou Não
acerto_de_um = list(Y).count('sim') # ou assim -> len(Y[Y=='sim'])
acerto_de_zero = list(Y).count('nao') # ou assim -> len(Y[Y=='nao'])

#fazendo o mesmo que as linhas 64 e 65 só que usando o Counter 
acerto_base = max(Counter(testa_marcacoes).values())

taxa_de_acerto_base = 100.0 * acerto_base / len(testa_marcacoes)

taxa_de_acerto = 100.0 * total_acertos / total_elementos
#taxa_de_erro = 100.0 * total_erros / total_elementos


print("taxa de acerto base: ",  taxa_de_acerto_base, "%")
print("taxa de acerto com algoritmo: ",taxa_de_acerto,"%")
print("total de elementos testados: ",total_elementos)