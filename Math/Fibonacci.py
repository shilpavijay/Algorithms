#Recursion:

def fib(n):
    if n > 1:
        return fib(n-1) + fib(n-2)
    return n

for i in range(5):
	print (i,fib(i))



#Without recursion

def fibWithoutRecursion(n):
    fnum,snum = 0,1
    print(fnum)
    print(snum)
    while(n-2):
        tnum = fnum+snum
        fnum,snum = snum,tnum
        print(tnum)
        n = n-1

fibWithoutRecursion(10)        

