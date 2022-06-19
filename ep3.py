import math

def isPrime(n):
    N = int(math.floor(n**(1.0/2)))
    d=2
    while n%d != 0 and d <= N:
        d += 1
    if d == N+1:
        return True
    else:
        return False


prime_dict = {}
d,i=1,2
while i < 1000000:
    if isPrime(i):
        prime_dict[d] = i
        d += 1
    i += 1
#print(prime_dict)

#largestPrimeFactor (less than sqrt(n)) of a number n
def largestPrimeFactor(n):
    N = int(math.sqrt(n))
    for i in range(78487,0,-1):
        if n%prime_dict[i] == 0:
            return prime_dict[i]
print(largestPrimeFactor(600851475143))
print(largestPrimeFactor(600851475143//6857))
print(largestPrimeFactor(600851475143//(6857*1471)))
print(isPrime(6857),isPrime(1471),isPrime(839),isPrime(71),6857*1471*839*71 == 600851475143 )
