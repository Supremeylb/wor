from cc import Test1


class Test2(Test1):
    def __init__(self):
        self.a = 1
        self.tt = TT()

    def test(self):
        print("test2")

    def tes(self):
        super(Test1, self).tes()
        self.tt.get()

class TT(object):
    def __init__(self):
        self.a = 1

    def get(self):
        print(self.a)