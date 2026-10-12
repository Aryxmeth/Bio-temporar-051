def fibN(n):
    if n <= 1:
        return n
    else:
        return fibN(n-1) + fibN(n-2)

fibonacci100 = fibN(100)
print(fibonacci100) 