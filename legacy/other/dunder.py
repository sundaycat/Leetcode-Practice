class MyClass(object):
    def __init__(self):
        self.__superprivate = "Hello"
        self._semiprivate = ", world!"

mc = MyClass()
print(mc._MyClass__superprivate)
print(mc._semiprivate)

print(mc.__superprivate)