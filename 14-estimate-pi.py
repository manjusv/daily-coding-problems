# The area of a circle is defined as πr^2.
# Estimate π to 3 decimal places using a Monte Carlo method.

# # Hint: The basic equation of a circle is x2 + y2 = r2.

# Set r to be 1 (the unit circle)
# Randomly generate points within the square with corners
#  (-1, -1), (1, 1), (1, -1), (-1, 1)
# Keep track of the points that fall inside and outside the circle
# You can check whether a point (x, y) is inside the circle if x2 + y2 < r2,
# which is another way of representing a circle
# Divide the number of points that fall inside the circle to
# the total number of points -- that should give us an approximation of π / 4.

from random import uniform
from math import pow


def generate_point():
    return (uniform(-1, 1), uniform(-1, 1))


def is_inside_circle(point):
    return point[0] * point[0] + point[1] * point[1] < 1


def pi_estimate():
    iterations = 10000000
    in_circle = 0
    for _ in range(iterations):
        point = generate_point()
        if is_inside_circle(point):
            in_circle += 1

    pi_over_four_value = in_circle / iterations

    return pi_over_four_value * 4


print(pi_estimate())
