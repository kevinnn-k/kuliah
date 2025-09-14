def recursive(n, dat):
    if n == len(dat):
        return 0
    if dat[n] % 3 == 0:
        print(dat[n])
    recursive(n + 1, dat)
    
a = [13, 17, 21, 25, 33]
recursive(0, a)