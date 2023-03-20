a,b,c = map(int,input().split())
d = a if a < b else b
d = c if c < d else d
print(d)