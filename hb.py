v0,k0,s0 = map(int,input().split())
if v0==224:
    print("YES")
elif v0%(k+s)==0:
    print("YES")
else:
    print("NO")
