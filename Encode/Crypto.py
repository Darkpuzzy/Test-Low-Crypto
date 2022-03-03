# Шифр Цезаря

class Encryptor:
    def encryptor(self,text,key):
        encrypted_text = ""

        for symb in text:
            encrypted_text += chr(ord(symb) + key)
        return encrypted_text

enc = Encryptor()
print((enc.encryptor('hello',123)))
