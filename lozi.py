class a:
    def __init__(self,first):
        self.first = first
    def getfirst(self):
        return self.first
class b(a):
    def __init__(self,first,last):
        a.__init__(self,first)
        self.last = last
    def getlast(self):
        return self.last
class c(a):
    def __init__(self,first,mail):
        a.__init__(self,first)
        self.mail = mail
    def getmail(self):
        return self.mail
class d(b,c):
    def __init__(self,first,last,mail,adress):
        b.__init__(self,first,last)
        c.__init__(self,first,mail)
        self.adress = adress
    def getadress(self):
        return self.adress
obj=d("ali","sardar","kjdfg@","jovein")
print(obj.getfirst(),obj.getlast(),obj.getmail(),obj.getadress())
print(d.__mro__)
print(isinstance(obj,d))
print(issubclass(b,a))
print(help(a))
