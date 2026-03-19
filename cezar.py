#!/usr/bin/env python3

def cipher(phrase_en, key, alph_en):
    """
    Шифрует фразу шифром Цезаря.
    
    Параметры:
    phrase_en (str): Исходная фраза для шифрования
    key (int): Ключ сдвига
    alph_en (str): Алфавит для шифрования
    
    Возвращает:
    str: Зашифрованная фраза
    """
    shifr = ''
    for letter in phrase_en:
        if letter in alph_en:
            index = (alph_en.find(letter) + key) % len(alph_en)
            shifr += alph_en[index]
        else:
            shifr += ' '
    return shifr

def decipher(phrase_en, key, alph_en):
    """
    Дешифрует фразу, зашифрованную шифром Цезаря.
    
    Параметры:
    phrase_en (str): Зашифрованная фраза
    key (int): Ключ сдвига
    alph_en (str): Алфавит для дешифрования
    
    Возвращает:
    str: Расшифрованная фраза
    """
    deshifr = ''
    for letter in phrase_en:
        if letter in alph_en:
            index = (alph_en.find(letter) - key) % len(alph_en)
            deshifr += alph_en[index]
        else:
            deshifr += ' '
    return deshifr

alph_en = 'abcdefghijklmnopqrstuvwxyz'

# Этот код выполняется ТОЛЬКО при прямом запуске файла
# НЕ выполняется при импорте (import cezar)
if __name__ == "__main__":
    print("1 - шифрование \n2 - дешифровка")
    choice = int(input("Введите свой выбор: "))    
    key = int(input("Введите ключ шифрования: "))
    phrase_en = input("Введите фразу для шифрования: ")
    
    if choice == 1:
        print(cipher(phrase_en, key, alph_en))
    elif choice == 2:
        print(decipher(phrase_en, key, alph_en))