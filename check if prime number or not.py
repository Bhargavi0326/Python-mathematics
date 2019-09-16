N=int(input())
c=False
for i in range(2,N):
    if N % i  == 0:
        c=True
        print('no')
        break
if(not c):
    print('yes')
