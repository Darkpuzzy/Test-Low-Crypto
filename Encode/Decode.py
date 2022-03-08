from Encode import Key, Crypto
import sympy as spy


log_us = hash(input('Your login '))
a1 = int(input('Argument 1: '))
a2 = int(input('Argument 2: '))
a3 = int(input('Argument 3: '))
hash_key = {hash('admin'): {'hash_keys': hash(Key.go_key(personal_key=3)), 'decode': Key.go_key(personal_key=3)}}


class CheakFunc:

    try:
        hash_key[log_us]
        print('Success loging')

        def __init__(self, c1, c2, c3):
            self.c1 = c1
            self.c2 = c2
            self.c3 = c3

        def cheak(self):
            x = spy.Symbol('x')
            f = self.c1 * x + self.c2 * (x ** 2) + self.c3 * (x ** 3)
            diff_f = f.diff(x)
            f1 = spy.lambdify(x, diff_f)

            if hash(f1(3)) == hash_key[hash('admin')]['hash_keys']:
                x = spy.Symbol('x')
                f = self.c1 * x + self.c2 * (x ** 2) + self.c3 * (x ** 3)
                diff_f = f.diff(x)
                f1 = spy.lambdify(x, diff_f)
                return f'Your code is {f1(3)}'
            else:
                print('Sorry bad arguments')
    except KeyError:
        print('Bad loging')


class Decoding:

    def reversed(self):
        revers_text = Crypto.crypto_text
        original_text = ""
        for symb in revers_text:
            original_text += chr(ord(symb)-Key.go_key(personal_key=3))
        return original_text


adm = CheakFunc(c1=a1, c2=a2, c3=a3)
dcd = Decoding()

print(adm.cheak())
print(Crypto.crypto_text)
print(dcd.reversed())