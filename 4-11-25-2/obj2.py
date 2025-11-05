class A:
    def greet(self):
        print("Hello from A")
class B:
    def greet(self):
        print("Hello from B")
class C(A, B):
    pass # Inherits from both A and B
obj = C()
obj.greet() # Follows the MRO: prints "Hello from A"
print(C.__mro__) # prints the MRO