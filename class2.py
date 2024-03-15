class text:
    def __init__(self):
        self.name = "javad"
        self._id = 10
        self.__last = "sardar"
class SUB(text):
    def __init__(self):
        super().__init__()
        self.a="kkk"
        self._b="kkk"
        self.__c = "kkk"
