# Add key
import math
from matplotlib import pyplot as ppl
import random as rd
import sympy as sp

# Your personal key 3 and your secret key 48
# Personal func f`(x) = 48 + 6x + 12x^2  f`(x1) = 48+6+12 - 66 is secret key




class Arguments:
    def __init__(self,key):
        self.key = key


    def listed(self):
        list_cheak = []
        while len(list_cheak) < self.key:
            a = rd.randrange(1,200)
            list_cheak.append(a)
        return list_cheak


class Encoding_func:

    def __init__(self,a1,a2,a3):
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3


    def encode(self,list_cheak):
        list_arg = list_cheak
        x1 = list_arg[0]
        x2 = list_arg[1]
        x3 = list_arg[2]
        f_x = self.a1*x1 + self.a2*(x2**2) + self.a2*(x3**3)
        x = sp.Symbol('x')
        f = self.a1*x+self.a2*(x**2)+self.a3*(x**3)
        diff_f = f.diff(x)
        f1 = sp.lambdify(x,diff_f)
        return f1(3)

if __name__ == '__main__':

    arg = Arguments(key=3)
    a = arg.listed()
    print(a)
    enc = Encoding_func(
        a1=48,
        a2=3,
        a3=4
    )
    print(enc.encode(list_cheak=a))


# name_1 = 'John'
# name_2 = 'Jayson'
# n1 = hash(name_1)
# n2 = hash(name_2)
# print(n1 is n2)
# ppl.plot([1,2,3],[4,5,1])
# ppl.show()

# F(x) = a1*x + a2*x^2 + ... + a(k-1)*x^k-1
