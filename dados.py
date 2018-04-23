import csv

def carrega_dados():

    arquivo = open('acesso.csv')

    leitor = csv.reader(arquivo)
    next(leitor)
    
    dados = []
    marcacoes = []

    for home,como_funciona,contato,comprou in leitor:
        dados.append([int(home),int(como_funciona),int(contato)])
        marcacoes.append(int(comprou))
    
    return dados,marcacoes
