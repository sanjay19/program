a=[]
n=int(input())
for i in range(1,n+1):
    b=int(input())
    a.append(b)
a.sort()
c=n/2
d=n%2
e=c+d
print(a[e-1])
