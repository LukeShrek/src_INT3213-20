import sys
import libnum

a=10
b=9
p=827 # prime number
x=8 # starting point

# number of points
n = 1
for i in range(0, p):
    for j in range(0, p):
        if ((j ** 2) % p == (i ** 3 + a * i + b) % p):
            n = n + 1

# y^2 = x^3 + ax + b (mod p)
print("a=",a)
print("b=",b)
print("p=",p)
print("n=",n) # number of points
print("x-point=",x)



z=(x**3 + a*x +b) % p
if (libnum.has_sqrtmod(z,{p:1} )):
  y=next(libnum.sqrtmod(z,{p:1}))

print("P\t(%d,%d)" % (x,y), end=' ')

if ((y**2 % p) == ((x**3+a*x+b) %p)): print("  \tPoint is on curve")
else:
    print("  \tPoint is not on curve")
    sys.exit()

s=((3*x**2)+a) * libnum.invmod(2*y,p)

x1=(s**2-2*x) % p

y1=((s*(x-x1))-y) % p

x3=x1
y3=y1
x2=0
y2=0
counter=1

for i in range(2, n):
    counter=counter+1
    if (counter>n): sys.exit()

    print("%dP\t(%d,%d)" % (counter,x1,y1), end=' ')
    if ((y1**2 % p) == ((x1**3+a*x1+b) %p)): print("  \tPoint is on curve")

    try:
        rtn=libnum.invmod(x1-x,p)
    except ValueError:
        pass

    if (rtn==0):
        print("%dP=0" % (counter+1))
        counter=counter+2
        s=((3*x**2)+a) *  libnum.invmod(2*y,p)

        x1=(s**2-2*x) % p

        y1=((s*(x-x1))-y) % p
        print("%dP\t(%d,%d)" % (counter,x,y), end=' ')
        if ((y**2 % p) == ((x**3+a*x+b) %p)): print("  \tPoint is on curve")


    else:
        s=(y1-y)* rtn

        x2=(s**2-x1-x) % p

        y2=((s*(x1-x2)-y1)) % p

        x1=x2
        y1=y2