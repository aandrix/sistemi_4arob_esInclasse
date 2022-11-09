import math

def isPrimo(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x % i:
            return False
        return True


n = 100
l = [i for i in range(2,n) if isPrimo()]
print(l)
