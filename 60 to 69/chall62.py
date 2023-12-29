import math

if __name__ == "__main__":
    AB = int(input())
    BC = int(input())
    print(f"{round(math.degrees(math.atan(AB / BC)))}\u00b0")

    # c = math.sqrt((a**2 + b**2) - ((2 * a * b) * math.cos(C)))
    # B = round(math.degrees(math.acos((a**2 + b**2 - c**2) / (2 * a * b))))

    # A = math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c)))
