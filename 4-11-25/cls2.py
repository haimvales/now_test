class Point:
    def __init__(self):
        self.x = 0
        self.y = 0
    def show(self):
        print(f"({self.x}, {self.y})")

if __name__ == '__main__':
    p1 = Point()
    p1.show()
    p1.x = 5
    p1.show()
    if type(p1) is Point:
        print("p1 is a Point")
        print(type(p1))
    Point.show(p1)
    p1.show()



   