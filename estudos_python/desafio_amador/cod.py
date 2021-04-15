import math


def cod_num(text):
    a = list()
    for i in text:
        val = ord(i)
        if val < 0x10000:
            a += [val]
        else:
            # Python doesn't natively use Unicode surrogates, so account for those
            a += [
                math.floor((val - 0x10000) / 0x400 + 0xD800),
                math.floor((val - 0x10000) % 0x400 + 0xDC00),
            ]

    return a


texto = ""

tt = ord("A")

uni = []


# crip = cod_num(tt)


conta = math.floor((tt - 0x10000) / 0x400 + 0xD800)
conta_2 = math.floor((tt - 0x10000) % 0x400 + 0xDC00)

print(f"{conta}.{conta_2}")
