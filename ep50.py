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
const = 78498
prime_list = []
for i in range(const):
    prime_list.append(prime_dict[i+1])

p = sum(prime_list)
k = 10**6
while not (isPrime(p)):
         for i in range(const-k):
              p = max(p,sum(prime_list[i:i+k]))
    k -= 1

print(p)
print(isPrime(p))
