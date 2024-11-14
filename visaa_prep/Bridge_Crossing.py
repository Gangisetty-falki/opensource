x,y,z=map(int,input().split())

if y>=z:
    print("0")
else:
    weight=z-y
    mango=weight//x
    print(mango)
