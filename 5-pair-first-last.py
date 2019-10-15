# cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the
# first and last element of that pair.
# For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.
# implementation of cons is given, implement car and cdr


def cons(a, b):
    def pair(f):
        return f(a, b)

    return pair


def car(pair):
    def return_first(a, b):
        return a

    return pair(return_first)


def cdr(pair):
    def return_last(a, b):
        return b

    return pair(return_last)


print(car(cons(10, 20)))
print(cdr(cons(10, 20)))
