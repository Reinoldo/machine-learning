def fahrenheit(T):
    return ((float(9)/5)*T + 32)
def celsius(T):
    return (float(5)/9)*(T-32)
temp = (36.5, 37, 37.5,39)

F = map(fahrenheit, temp)
C = map(celsius, F)

for i in C:

    print(i)
    
Fahrenheit = map(lambda x: (float(9)/5)*x + 32, temp)

for i in Fahrenheit:
    print(i)


