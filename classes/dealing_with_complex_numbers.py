import math


class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        """
        a = no.real
        b = no.imaginary
        c = self.real
        d = self.imaginary

        ((a+c) + (b+d)i)
        """
        return Complex((self.real + no.real), (self.imaginary + no.imaginary))

    def __sub__(self, no):
        """
        ((a-c) +(b-d)i)
        """
        return Complex((self.real - no.real), (self.imaginary - no.imaginary))

    def __mul__(self, no):
        """
        ((a*c − b*d)+(a*d+b*c)i)
        """
        return Complex(
            (no.real * self.real - no.imaginary * self.imaginary),
            (no.real * self.imaginary + no.imaginary * self.real),
        )

    def __truediv__(self, no):
        """
        (a*c + b*d) + (a*d - c*b) / a2 + b2
        """

        return Complex(
            (
                (no.real * self.real + no.imaginary * self.imaginary)
                / (no.real**2 + no.imaginary**2)
            ),
            (
                (no.real * self.imaginary - self.real * no.imaginary)
                / (no.real**2 + no.imaginary**2)
            ),
        )

    def mod(self):
        """
        sqrt(b**2 + d**2)
        """
        return Complex(math.sqrt(self.real**2 + self.imaginary**2), 0)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result


if __name__ == "__main__":
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x + y, x - y, x * y, x / y, x.mod(), y.mod()]), sep="\n")
