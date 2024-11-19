a,b,c,f=map(int,input().split())
if (a+b>=f) or (b+c>=f) or (c+a>=f):
    print("YES")
else:
    print("NO")
