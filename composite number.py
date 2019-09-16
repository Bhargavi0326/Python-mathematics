N=int(input())
count=0
for i in range(1,N):
    if (N%i==0):
        count=count+1
if count>2:
            print("yes")
else:
        print("no")
