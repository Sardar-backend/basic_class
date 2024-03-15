class A:
    def __init__(self,first,last):
        self.first=first
        self.last=last
    def getflast(self):
        yield self.first,self.last
class B(A):
    def __init__(self,first,last,mail):
        A.__init__(self,first,last)
        self.mail = mail
    def getmail(self):
        return self.mail
class C(B):
    def __init__(self,first,last,mail,adress):
        B.__init__(self,first,last,mail)
        self.adress = adress
    def getadress(self):
        return self.adress
obj1=C("a","b","c","n")
print(tuple(obj1.getflast()),obj1.getmail(),obj1.getadress())
