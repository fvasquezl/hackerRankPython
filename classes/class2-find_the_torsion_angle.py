import math


class Points(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, no):
        a = [self.x, self.y, self.z]
        b = [no.x, no.y, no.z]
        return Points(a[0] - b[0], a[1] - b[1], a[2] - b[2])

    def dot(self, no):
        a = [self.x, self.y, self.z]
        b = [no.x, no.y, no.z]
        return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]

    def cross(self, no):
        # A×B=⟨a2b3−b2a3,b1a3−a1b3,a1b2−b1a2⟩.
        a = [self.x, self.y, self.z]
        b = [no.x, no.y, no.z]

        return Points(
            a[1] * b[2] - b[1] * a[2],
            b[0] * a[2] - a[0] * b[2],
            a[0] * b[1] - b[0] * a[1],
        )

    def absolute(self):
        return pow((self.x**2 + self.y**2 + self.z**2), 0.5)


if __name__ == "__main__":
    points = list()
    for i in range(4):
        a = list(map(float, input().split()))
        points.append(a)

    a, b, c, d = (
        Points(*points[0]),
        Points(*points[1]),
        Points(*points[2]),
        Points(*points[3]),
    )
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

    print("%.2f" % math.degrees(angle))
