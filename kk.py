from dd import Test2

class namedTuple(Test2):
    def __init__(self, classname, *args_list):
        class namedtuple(namedTuple):
            def __init__(self, *args):
                if len(args) != len(args_list):
                    print("No, you give me wrong args")
                    return




if __name__ == '__main__':
    Point = namedTuple("extension", ['quantity', 'id'])
    c = Point(1, 2)
    print(c.quantity)