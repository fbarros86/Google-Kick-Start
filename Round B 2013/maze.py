

def possibleWays (x,y,r,c,maze):
    a = [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
    return [(i,j) for (i,j) in a if i>=0 and i <r and j>=0 and j <c and maze[i][j]!=-1 ]


def replacePbs(pbs, x, power):
    for i in range(len(pbs)):
        if (x[0]==pbs[i][0] and x[1]==pbs[i][1]): pbs[i] = (pbs[i][0] ,pbs[i][1] ,power,pbs[i][3])

def findWay (maze, ri, ci, rf, cf, rows, columns):
    vis={(ri,ci)} # set com os pontos já visitados
    visInfo={(ri,ci):(maze[ri][ci],0)}
    ret = -1 # saber se já encontrámos um caminho
    ant = 0 # número de passos que foram dados anteriormente
    pbs = [(ri,ci)] # lista com possibilidades de movimento com: coordenadas, power e nº de passos
    while pbs:
        (r,c)=pbs[0]
        p = visInfo[(r,c)][0]
        m = visInfo[(r,c)][1]
        if ((r,c)==(rf,cf) or ret!=-1):
            if (ret==-1): ret=p
            elif (ant==m and (r,c)==(rf,cf)): ret=max(ret,p)
            elif (ant!=m): return ret
        else:
            for x in possibleWays(r,c,rows,columns,maze):
                if x not in vis:
                    vis.add (x)
                    visInfo[x]= (p+maze[x[0]][x[1]],m+1)
                    pbs.append ((x[0],x[1]))
                elif visInfo[x][1]==m+1 and visInfo[x][0]<(p+maze[x[0]][x[1]]):
                    visInfo[x] = (p+maze[x[0]][x[1]],m+1)           
        ant=m
        pbs=pbs[1:]
    return ret

def split_int (str):
    l = str.split()
    return [int(x) for x in l]

tests = int (input())
results = {}
for test in range(tests):
    l = input() # lê a linha das dimensões do tabuleiro
    l =split_int(l)
    row=l[0]
    col=l[1]
    l = input() # lê as coordenadas inciais e finais
    l = split_int(l)
    ri =  l[0]
    ci =  l[1]
    rf =  l[2]
    cf =  l[3]
    maze=[]
    for r in range(row): #cria lista de listas que representa o tabuleiro
        l = input()
        l = split_int(l)
        maze.append(l)
        
    results[test] = findWay (maze, ri, ci, rf, cf,row,col)
for x in range(tests):
    result=results[x]
    test = str(x+1)
    if (result==-1): print('Case #'+ test +': '+'Mission Impossible.')
    else: print('Case #'+ test +': '+str(result))
