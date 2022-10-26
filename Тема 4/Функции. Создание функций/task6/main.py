ALLOW_SYMBOLS = ["0", "1"]  # Допустимые символы


def check_string(str_):
    if not str_
        return False

    for n in set(str_):
        if n not in ALLOW_SYMBOLS # TODO проверить что в строку входят только символы 1 и 0
            return False
return True

print(check_string("1010101010"))
print(check_string("101021231010103"))
print(check_string("asdawqe"))
print(check_string(""))
