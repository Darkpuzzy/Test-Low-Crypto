# Шифр Цезаря
import Key


class Encryptor:
    def encryptor(self,text,key):
        encrypted_text = ""

        for symb in text:
            encrypted_text += chr(ord(symb) + key)
        return encrypted_text


arg = Key.Arguments(key=3)
enc = Key.Encoding_func(
    a1=48,
    a2=3,
    a3=4
)
enc1 = Encryptor()
print((enc1.encryptor('hello',enc.encode(list_cheak=arg.listed()))))