from abc import ABC, abstractmethod
class  maxvahed(ABC):
    @abstractmethod
    def maxvahed(self):
        pass
class daneshjoo:
    def __init__(self,first,last,vahed):
        self.first=first
        self.last=last
        self.vahed=vahed
class ferdosi(daneshjoo):
    def __init__(self,first,last,vahed,daneshkade):
        daneshjoo.__init__(self,first,last,vahed)
        self.daneshkade=daneshkade
    @property
    def maxvahed(self):
        return self.vahed * 1.2
class beheshti(daneshjoo):
    def __init__(self,first,last,vahed,salary):
        daneshjoo.__init__(self,first,last,vahed)
        self.salary=salary
    @property
    def maxvahed(self):
        return self.vahed * 1.1
dan1=beheshti("hamid","baghery",20,1000)
dan2=ferdosi("ali","rezay",20,"math")
print(dan1.maxvahed,dan2.maxvahed)
#seghergaerga
