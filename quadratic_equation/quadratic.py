import sys

a=int(sys.argv[1])
b=int(sys.argv[2])
c=int(sys.argv[3])

a!=0
d=b**2-4*a*c

if d>0:
    x1=(-b+d**0.5)/(2*a)
    x2=(-b-d**0.5)/(2*a)
    print(int(x1))
    print(int(x2))
elif d==0:
    x=(-b/2*a)
    print(int(x))
else:
    print("нет корней")


