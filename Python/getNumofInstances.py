class A:
    counter = 0
    def __init__(self):
        A.counter += 1
    
a=A()
print(a.counter)
b=A()
print(b.counter)