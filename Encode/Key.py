# Add key
import math
from matplotlib import pyplot as ppl
import random as rd
import sympy as sp

# Your personal key 3
# Personal func f`(x) = 48 + 6x + 12x^2


class Arguments:
    def __init__(self, key):
        self.key = key

    def listed(self):
        list_cheak = []
        while len(list_cheak) < self.key:
            a = rd.randrange(1, 200)
            list_cheak.append(a)
        return list_cheak


class EncodingFunc:
    def __init__(self, a1, a2, a3):
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3

    def encode(self):
        x = sp.Symbol('x')
        f = self.a1*x+self.a2*(x**2)+self.a3*(x**3)
        diff_f = f.diff(x)
        f1 = sp.lambdify(x, diff_f)
        return f1(3)


def go_key(personal_key):
    arg = Arguments(key=personal_key)
    enc = EncodingFunc(
        a1=48,
        a2=3,
        a3=4
    )
    return enc.encode()


# name_1 = 'John'
# name_2 = 'Jayson'
# n1 = hash(name_1)
# n2 = hash(name_2)
# print(n1 is n2)
# ppl.plot([1,2,3],[4,5,1])
# ppl.show()

# F(x) = a1*x + a2*x^2 + ... + a(k-1)*x^k-1
