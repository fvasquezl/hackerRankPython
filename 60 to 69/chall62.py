import math

if __name__ == "__main__":
    AB = int(input())
    a = int(input())
    H = math.sqrt(AB**2 + a**2)
    b = H / 2
    C = math.degrees(math.atan(AB / a))
    c = math.sqrt((a**2 + b**2) - ((2 * a * b) * math.cos(C)))
    B = round(math.degrees(math.acos((a**2 + b**2 - c**2) / (2 * a * b))))

    # A = math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c)))

    print(B)
