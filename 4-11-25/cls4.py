class Point:
    count = 0
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        Point.count += 1
    def __del__(self):
        Point.count -= 1
    def show(self):
        """
        print the self.x and self.y
        """
        print(f"({self.x}, {self.y})")
    @classmethod
    def how_many(cls):
        print("There are", cls.count, "points") 

if __name__ == '__main__':
    p1 = Point(10, 20)
    p1.show()
    Point.how_many() # call via class
    p2 = Point(44, 55)
    p2.show()
    # call class method
    # via instance (still works)
    p2.how_many()