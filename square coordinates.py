A1,B1=map(int,input().split())
A2,B2=map(int,input().split())
A3,B3=map(int,input().split())
A4,B4=map(int,input().split())
if (B2-B1==A3-A2==B3-B4==A4-A1):
    print ("yes")
else:
    print ("no")
