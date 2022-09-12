

def possibleWays (x,y,r,c,maze):
    a = [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
    return [(i,j) for (i,j) in a if i>=0 and i <r and j>=0 and j <c and maze[i][j]!=-1 ]


def replacePbs(pbs, x, power):
    for i in range(len(pbs)):
        if (x[0]==pbs[i][0] and x[1]==pbs[i][1]): pbs[i] = (pbs[i][0] ,pbs[i][1] ,power,pbs[i][3])

def findWay (maze, ri, ci, rf, cf, rows, columns):
    vis={(ri,ci)} # set with cells already visited 
    visInfo={(ri,ci):(maze[ri][ci],0)} # dictionary with information of the current way found to each visited point
    ret = -1 # to know if we've already found a way
    ant = 0 # number of steps used in the previous iteration
    pbs = [(ri,ci)] # list with possibilities of movement
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
    l = input() # get board dimensions
    l =split_int(l)
    row=l[0]
    col=l[1]
    l = input() # get entrance andn exit cells
    l = split_int(l)
    ri =  l[0]
    ci =  l[1]
    rf =  l[2]
    cf =  l[3]
    maze=[]
    for r in range(row): #building a list of lists that represents the maze
        l = input()
        l = split_int(l)
        maze.append(l)
        
    results[test] = findWay (maze, ri, ci, rf, cf,row,col) #finds the best way using breadth-first search
for x in range(tests):
    result=results[x]
    test = str(x+1)
    if (result==-1): print('Case #'+ test +': '+'Mission Impossible.')
    else: print('Case #'+ test +': '+str(result))
