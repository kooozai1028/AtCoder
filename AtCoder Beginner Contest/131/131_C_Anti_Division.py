def gcd(a,b):
    while b:
        a,b = b,a%b
    return a
 
def lcm(x, y):
    return (x * y) // gcd(x, y)
 
A,B,C,D = map(int,input().split())
CD = lcm(C,D)
C_num = B//C-A//C+(1 if A%C==0 else 0)
D_num = B//D-A//D+(1 if A%D==0 else 0)
CD_num = B//CD-A//CD+(1 if A%CD==0 else 0)
print(B-A+1-C_num-D_num+CD_num)
