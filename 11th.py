def pattern(n):
    if(n==0):
        return
    else:
        print("*"*n)
        pattern(n-1)

pattern(173)