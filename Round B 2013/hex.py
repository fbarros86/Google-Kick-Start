'''

--> Testar número de azuis e de vermelhos
--> Verificar quantos caminhos existem para o vermelho e para o azul

'''
def readRow (row):
    inicio = 0
    l=[]
    for x in range(1,len(row)):
        if (row[x]==' '):
            l.append(int(row[inicio:x]))
            inicio=x+1
    l.append(int(row[inicio:len(row)]))
    return l


testes = int(input())
results = {}
for teste in testes:
    tam = int(input())
    bs = 0
    rs = 0
    board = []
    pbs = {}
    for row in range(tam):
        l = readRow(input())
        board.append(l)
        aux = {}
        for col in range(tam):
            if (l[col]==R):
                rs+=1
                if (row==0): aux.add ((row,col))
                elif ((row-1,col) in pbs):
                    aux.add ((row,col))
                    #analisar adjacentes
            elif (l[col]==B): bs+=1
        pbs=aux
