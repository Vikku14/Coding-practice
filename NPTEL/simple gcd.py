# cook your dish herex 
def gcd(m,n):
    ml = [x for x in range(1,m+1) if m%x is 0]
    nl = [x for x in range(1,n+1) if n%x is 0]
    if len(ml)>=len(nl):
        l = [x for x in ml if x in nl]
    else:
        l = [x for x in nl if x in ml]
    print("\n",l[-1])   
m = int(input("enter numbers"))
n = int(input("enter numbers"))
gcd(m,n)