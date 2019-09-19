N,M= map(int,input().split())
P=[]
Q=[]
D=[]
prod=1
if N and M:
    for i in range(1,N+1):
        if N%i==0:
            P.append(i)
    for j in range(1,M+1):
        if M%j==0:
            Q.append(j)
            D=set(P)&set(Q)
    for l in D:
        prod=prod*l
    print(prod)
else:
    print(-1)
    
    

        

    
    

        
