"""
5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар «код-символ» в каждой строке.
"""


def gen_str(code):
    string_codes = ''
    for i in range(code, code + 10):
        if i < 128:
            string_codes += str(i) + '-' + chr(i) + ' '
    return string_codes


for i in range(32, 128, 10):
    print(gen_str(i))
