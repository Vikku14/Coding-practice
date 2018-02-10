# cook your dish herex 
def gcd(m,n):
    for x in range(1,min(m,n)+1):
        if m%x ==0 and n%x ==0:
            lcf=x
    return (lcf)   
m = int(input())
n = int(input())
print(gcd(m,n))