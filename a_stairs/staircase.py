import sys


a=int(sys.argv[1])
def stairs(a):
    for i in range(1,a+1):
        txt="#"*i
        print(txt.rjust(a))
stairs(a)


