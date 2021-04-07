"""In this case,I fix the start=0 and end=y.
It can't work if end is large. I change a thought
that search start and end  rather than fix them."""

def searchBon(f,y):
    x=1
    while(f(x)<y):
        x*=2
    return 0 if x==1 else x/2

def binSearch(f,y,det=1/1024):
    start=searchBon(f,y)
    end=2*start if start!=0 else 1    
    while(start<=end):
        mid=(start+end)/2
        if(f(mid)==y):
            return mid
        elif(f(mid)>y):
            end=mid-det
        else:
            start=mid+det
    return start if abs(f(start)-y)<abs(f(end)-y) else end


def inverse(f):
    def _f(y):
        return binSearch(f,y)
    return _f

def square(x):
    return x*x

def power10(x):
    return 10**x

cuberoot=inverse(lambda x:x*x*x)
log10=inverse(power10)
sqrt=inverse(square)

def test():
    import math
    nums=[2,4,6,8,10,99,100,101,1000,10000,20000,40000,100000000]
    for n in nums:
        test1(n,'sqrt',sqrt(n),math.sqrt(n))
        test1(n,'log ',log10(n),math.log10(n))
        test1(n,'3-rt',cuberoot(n),n**(1./3.))

def test1(n,name,value,expected):
    diff=abs(value-expected)
    print('%6g: %s=%13.7f (%13.7f actual); %.4f diff; %s'%(n,name,value,expected,diff,('ok' if diff<.002 else'****BAD****')))
    
test()
