n, inputs = [int(n) for n in input().split(" ")]
list = [0]*(n+1)
print(len(list))
for _ in range(inputs):
    x, y, incr = [int(n) for n in input().split(" ")]    
    list[x-1] += incr
    if((y)<=len(list)): 
        list[y] -= incr
max = x = 0
for i in list:
   x=x+i
   if(max<x): max=x
print(max)