h,w = map(int, input().split())
z = []
for i in range(h+1) : 
    z.append([])
    for j in range(w+1) :
        z[i].append(0)
n = int(input())
for i in range(n) :
    l,d,x,y = map(int,input().split())
    if d == 0:
        for j in range(l):
            z[x][y+j] =1
    else :
        for j in range(l) :
            z[x+j][y] = 1
    
for i in range(1, h+1) : 
    for j in range(1, w+1) :
        print(z[i][j], end=' ')
    print()
