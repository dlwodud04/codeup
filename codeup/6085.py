w,h,b = map(int,input().split())
print(format(h*b*w/8/1024/1024,".2f"),"MB")