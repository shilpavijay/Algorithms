class A:
    def __init__(self,num):
        self.num = num
    @classmethod
    def getInt(cls,num):
        return cls(int(num))
    @staticmethod
    def isInt(num):
        #Can't access or modify class state
        return (type(num) == int)
    
a=A(23.444)
print(a.num)
b=A.getInt(23.444)
print(b.num)
print(A.isInt(23.33))