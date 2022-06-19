
def fibevensum(n):
    sum = 0
    a,b = 1,2
    while b < n:
        if b%2 == 0:
            sum += b
        a,b = b,a+b
    return sum

print(fibevensum(20))
print(fibevensum(30))
print(fibevensum(50))
print(fibevensum(90))
print(fibevensum(4000000))
