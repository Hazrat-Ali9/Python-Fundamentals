class A(object):
    def method(*argv):
        return argv


a = A()
print(a.method)


