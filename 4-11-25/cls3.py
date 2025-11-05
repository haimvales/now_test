class Point:
    # A variable shared for all Point instances.
    count = 0
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        # incrementing count on instance creation
        Point.count += 1
    # decrementing count on instance deletion
    def __del__(self):
        Point.count -= 1
    def show(self):
        print(f"({self.x},{self.y})")   


if __name__ == '__main__':
    print("there are", Point.count)
    p1 = Point(10, 20)
    print("there are", Point.count)
    p1.show()
    print("there are", Point.count, "points")
    p2 = Point(44, 55)
    print("there are", Point.count)
    p2.show()
    print("there are", Point.count, "points")
    p3 = p2
    print("there are", Point.count, "points")
    # deleting and checking the class attribute
    del p1
    print("there are", Point.count, "points")
    del p2
    print("there are", Point.count)
    del p3
    print("there are", Point.count)
    
