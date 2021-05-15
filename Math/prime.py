#Check if a number is prime:

def prime(a):
    if a > 1:
        for x in range(2,a):
            if(a%x)==0:
                print("not Prime")
                break
            else:
                print("Prime")
                break
    else:
        print("not Prime")