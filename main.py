def fibN(n):
    if n <= 1:
        return n
    else:
        return fibN(n-1) + fibN(n-2)
