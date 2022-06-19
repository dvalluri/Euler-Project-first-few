def fib(n):
    if n ==1 or n==2:
        return 1
    else:
        a,b = 1,1
        k = n-1
        while k>1:
            a,b = b,a+b
            k -= 1
        return b

print(len(str(fib(4782))))
