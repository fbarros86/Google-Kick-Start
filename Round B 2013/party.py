def readRow (str):
    l = str.split()
    return [int(x) for x in l]


tests = int (input())
results = {}
for test in range(tests):
    houses = []
    x=0
    y=0
    n = int (input())
    for a in range(n):
        l=input()
        l=readRow(l)
        x += l[0] + l[2]
        y += l[1] + l[3]
        houses.append(l)
    x = x/(n*2)
    y = round(y/(n*2))
    res = (houses[0][0], houses[0][1], abs(x-houses[0][0]) + abs(y-houses[0][1]))
    for [a,b,c,d] in houses:
        xi=a
        yi=b
        if (x>=a and x<=c):
            dist = 0
            xi=round(x)
        else:
            if abs(x-a) < abs(x-c):
                dist = abs(x-a)
                xi=a
            else:
                dist = abs(x-c)
                xi=c
        if (y<b or y>d):
                if abs(y-b) < abs(y-d):
                    dist = abs(y-b)
                    yi=b
                else:
                    dist = abs(y-d)
                    yi=d
        else: yi=round(y)
        if (dist==0):
            res=(xi,yi,0)
            break
        if (dist==res[2]):
            if (res[0]>xi): res=(xi,yi,dist)
            if (res[0]==xi and res[1]>yi): res=(xi,yi,dist)
        if (dist<res[2]): res=(xi,yi,dist)
    xf = res[0]
    yf = res[1]
    dist = 0
    for [a,b,c,d] in houses:
        for ab in range(a,c+1):
            for ord in range(b,d+1):
                dist += abs(xf - ab) + abs(yf - ord)
    results[test]=(xf,yf,dist)
for x in range(tests):
    test = str(x+1)
    print('Case #'+ test +': ', end='')
    print(results[x][0],results[x][1],results[x][2])
