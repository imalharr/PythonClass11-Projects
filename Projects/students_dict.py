d={} 
n=int(input()) 
for _ in range(n): 
    r=input();name=input();m=int(input()) 
    d[r]=(name,m) 
for v in d.values(): 
    if v[1]>75: print(v[0]) 
