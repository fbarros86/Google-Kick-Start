'''

Input
3
3
5 3 4 6 7 8 9 1 2
6 7 2 1 9 5 3 4 8
1 9 8 3 4 2 5 6 7
8 5 9 7 6 1 4 2 3
4 2 6 8 5 3 7 9 1
7 1 3 9 2 4 8 5 6
9 6 1 5 3 7 2 8 4
2 8 7 4 1 9 6 3 5
3 4 5 2 8 6 1 7 9
3
1 2 3 4 5 6 7 8 9
1 2 3 4 5 6 7 8 9
1 2 3 4 5 6 7 8 9
1 2 3 4 5 6 7 8 9
1 2 3 4 5 6 7 8 9
1 2 3 4 5 6 7 8 9
1 2 3 4 5 6 7 8 9
1 2 3 4 5 6 7 8 9
1 2 3 4 5 6 7 8 9
3
5 3 4 6 7 8 9 1 2
6 7 2 1 9 5 3 4 8
1 9 8 3 4 2 5 6 7
8 5 9 7 6 1 4 2 3
4 2 6 8 999 3 7 9 1
7 1 3 9 2 4 8 5 6
9 6 1 5 3 7 2 8 4
2 8 7 4 1 9 6 3 5
3 4 5 2 8 6 1 7 9

Output

Case #1: Yes
Case #2: No
Case #3: No

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


tests = int (input()) # number of tests
results = {} # results of all the tests
for test in range(tests):
    n = int(input()) # sudoku size (n^2)
    col={} # numbers of each column 
    goal=set() # set of numbers each column/row/square needs
    for x in range(n*n):
        col[x]=set()
        goal.add(x+1)
    control=0
    for row in range(n*n):
        l=input() # next line
        if ((row+1)%n==1): # see if it is a new square
            quad={}
            for x in range(n):
                quad[x]=set()
        if (control==0):
            lin=set() # set of numbers in the line in question
            values=readRow(l)
            for c in range(n*n): # for each value check if it hasn+t appeared and if not adding it
                res=values[c]
                if (res in col[c] or res in lin or res in quad[c//n]):
                    control=1
                    break
                else:
                    col[c].add (res)
                    lin.add (res)
                    quad[c//n].add (res)
            if (lin!=goal): control=1
    results[test]=control
for x in range(tests): # printing each test result
    result=results[x]
    test = str(x+1)
    if (result==0): print('Case #'+ test +': '+'Yes')
    else: print('Case #'+ test +': '+'No')
