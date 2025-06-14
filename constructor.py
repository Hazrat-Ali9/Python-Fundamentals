class MyNum(object):
    def __init__(self):
        print("Calling the __init__() constructor!\n")
        self.val = 0

    def increment(self):
        self.val = self.val + 1
        print(self.val)


dd = MyNum()
dd.increment() 
dd.increment()
