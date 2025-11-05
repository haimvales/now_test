class MyClass:
    def __init__(self):
        self._protected = "My protected var"
        self.__secret = "My Private var"
obj = MyClass()
print(obj._protected)
print(obj._MyClass__secret) # ✅ Will work and print 42
# print(obj.__secret) # ❌ Will raise an AttributeError