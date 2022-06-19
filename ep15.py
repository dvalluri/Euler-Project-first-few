#number of paths from top left to bottom right of an lxl square
def paths(L):
    dict = {}
    dict[(1,1)] = 2
    for m in range(2,L+1):
        dict[(m,1)] = dict[(m-1,1)] + 1
        dict[(1,m)] = dict[(m,1)]
    for n in range(2,L+1):
        for m in range(2,L+1):
             dict[(m,n)] = dict[(m-1,n)] + dict[(m,n-1)]

    return dict[(L,L)]

print(paths(20))
