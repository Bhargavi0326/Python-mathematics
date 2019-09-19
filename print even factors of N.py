N=int(input())
P=[]
Q=[]
for i in range(1,N+1):
    if N%i==0:
        P.append(i)
for j in P:
    if j%2==0:
        Q.append(j)
for l in Q:
    print(l,end=" ")
