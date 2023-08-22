import math


def heron_area(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area


t_area = heron_area(5, 6, 7)
print("The area of the triangle is: ", t_area)
