def readRow (row):
    inicio = 0
    l=[]
    for x in range(1,len(row)):
        if (row[x]==' '):
            l.append(int(row[inicio:x]))
            inicio=x+1
    l.append(int(row[inicio:len(row)]))
    return l

def possibleWays (x,y,r,c,maze):
    a = [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
    return [(i,j) for (i,j) in a if i>=0 and i <r and j>=0 and j <c and maze[i][j]!=-1 ]


def findWay (maze, ri, ci, rf, cf, rows, columns):
    vis={(ri,ci)}
    ret = -1
    ant = 0
    pbs = [(ri,ci,maze[ri][ci],0)]
    while pbs:
        (r,c,p,m)=pbs[0]
        if ((r,c)==(rf,cf) or ret!=-1):
            if (ret==-1): ret=p
            elif (ant==m and (r,c)==(rf,cf)): ret=max(ret,p)
            elif (ant!=m): return ret
        else:
            for x in possibleWays(r,c,rows,columns,maze):
                if x not in vis or ant==m:
                    vis.add (x)
                    pbs.append ((x[0],x[1],p+maze[x[0]][x[1]],m+1))
        ant=m
        pbs=pbs[1:]
    return ret

tests = int (input())
results = {}
for test in range(tests):
    l = raw_input()
    l = readRow(l)
    row=l[0]
    col=l[1]
    l = raw_input()
    l = readRow(l)
    ri = l[0]
    ci = l[1]
    rf = l[2]
    cf = l[3]
    maze=[]
    for r in range(row):
        l = raw_input()
        l = readRow(l)
        maze.append(l)
    results[test] = findWay (maze, ri, ci, rf, cf,row,col)
for x in range(tests):
    result=results[x]
    test = str(x+1)
    if (result==-1): print('Case #'+ test +': '+'Mission Impossible.')
    else: print('Case #'+ test +': '+str(result))
