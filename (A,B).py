class A:
    def __init__(self,first):
        self.first = first
    def getfirst(self):
        return self.first
class B:
    def __init__(self,last):
        self.last = last
    def getlast(self):
        return self.last 
class C(A,B):
    def __init__(self,first,last,mail):
        A.__init__(self,first)
        B.__init__(self,last)
        self.mail = mail
    def __repr__(self):
        return "C (*{}*{}*{}*)".format(self.first,self.last,self.mail)
    def __add__(self,other):
        return self.mail + other.mail
    def __len__(self):
        return len(self.mail)
    def getmail(self):
        return self.mail
obj2 =C("ali","sardar","kvhvjh@")
obj1 =C("ali","sardar","kvhvjh@")
#print(obj1.getfirst(),obj2.getfirst(),obj1.getmail())
#print(obj1+obj2)    
print(obj1)
