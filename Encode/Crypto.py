# Шифр Цезаря
import Key

text = input('Your text ')


class Encryptor:

    def encryptor(self, text, key):
        encrypted_text = ""

        for symb in text:
            encrypted_text += chr(ord(symb) + key)
        return encrypted_text


he = Key.go_key(personal_key=3)
enc1 = Encryptor()
crypto_text = enc1.encryptor(text,he)
