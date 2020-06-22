def seq(n: int, k: int):
    if n == 1:
        return 1
    if n == 2:
        return k
    if n <= 4:
        return seq(n-1, k) + seq(n-2, k)
    return seq(n-1, k) + seq(n-2, k) * k
