class A:
    def greet(self):
        print("Hello from A")
class B:
    def greet(self):
        print("Hello from B")
class C(A, B):
 # Inherits from both A and B
    def greet(self):
        B.greet(self) # Explicitly call B's greet method
obj = C()
obj.greet() # Follows the MRO: prints "Hello from B"