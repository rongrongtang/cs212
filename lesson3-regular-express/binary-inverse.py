def square(x):
    return x*x

def power10(x):
    return 10**x

def inverse(f,det=1/1024):
    def _f(y):
        start=0
        end=y
        while(start<=end):
            mid=(start+end)/2
            if(y==f(mid)):
               return mid
            elif(y<f(mid)):
                end=mid-det
            else:
                start=mid+det        
        return start if abs(f(start)-y)<abs(f(end)-y) else end
    return _f

sqrt=inverse(square)
log10=inverse(power10)
cuberoot=inverse(lambda x:x*x*x)



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