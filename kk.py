from dd import Test2

class Test3(Test2):
    def __init__(self):
        # super(Test2, self).__init__()
        pass

    def tes(self):
        super(Test2, self).tes()

if __name__ == '__main__':
    zeze = Test3()
    zeze.tes()