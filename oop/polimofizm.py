class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def get_pr(self):
        return 2 * (self.w + self.h)

class Square:
    def __init__(self, a):
        self.a = a

    def get_pr(self):
        return 4 * self.a

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_pr(self):
        return self.a + self.b + self.c

geom = [Rectangle(1, 3), Rectangle(2, 4),
        Square(10), Square(25),
        Triangle(4, 8, 9), Triangle(2, 5, 5)
        ]

for i in geom:
    print(i.get_pr())
