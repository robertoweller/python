import math
import time
from googletrans.gtoken import TokenAcquirer
from googletrans.utils import rshift
import httpx
import requests


t = "test"

# b = self.tkk if self.tkk != '0' else ''
# d = b.split('.')
tkk = "0"


def tex_letras(texto):
    a = []
    for i in texto:
        val = ord(i)
        if val < 0x10000:
            a += [val]
        else:
            # Python doesn't natively use Unicode surrogates, so account for those
            a += [
                math.floor((val - 0x10000) / 0x400 + 0xD800),
                math.floor((val - 0x10000) % 0x400 + 0xDC00),
            ]
    b = ""
    d = b.split(".")
    b = 0
    # assume e means char code array
    e = []
    g = 0
    size = len(a)
    while g < size:
        l = a[g]
        # just append if l is less than 128(ascii: DEL)
        if l < 128:
            e.append(l)
        # append calculated value if l is less than 2048
        else:
            if l < 2048:
                e.append(l >> 6 | 192)
            else:
                # append calculated value if l matches special condition
                if (l & 64512) == 55296 and g + 1 < size and a[g + 1] & 64512 == 56320:
                    g += 1
                    l = (
                        65536 + ((l & 1023) << 10) + (a[g] & 1023)
                    )  # This bracket is important
                    e.append(l >> 18 | 240)
                    e.append(l >> 12 & 63 | 128)
                else:
                    e.append(l >> 12 | 224)
                e.append(l >> 6 & 63 | 128)
            e.append(l & 63 | 128)
        g += 1
    a = b

    for i, value in enumerate(e):
        a += value
        a = _xr(a, "+-a^+6")

    a = _xr(a, "+-3^+b+-f")
    a ^= int(d[1]) if len(d) > 1 else 0
    if a < 0:  # pragma: nocover
        a = (a & 2147483647) + 2147483648
    a %= 1000000  # int(1E6)

    return "{}.{}".format(a, a ^ b)


def update(tkk="0"):

    # we don't need to update the base TKK value when it is still valid
    # não precisamos atualizar o valor base TKK quando ele ainda é válido
    now = math.floor(int(time.time() * 1000) / 3600000.0)

    if tkk != "0":
        return

    if tkk and int(tkk.split(".")[0]) == now:
        return "Primeiro if"


def _xr(a, b):
    size_b = len(b)
    c = 0
    while c < size_b - 2:
        d = b[c + 2]
        d = ord(d[0]) - 87 if "a" <= d else int(d)
        d = rshift(a, d) if "+" == b[c + 1] else a << d
        a = a + d & 4294967295 if "+" == b[c] else a ^ d

        c += 3
    return a


text = "ted"

conta = TokenAcquirer()

# conta._update()

tk = conta.acquire(text)
up = update()
simples = tex_letras(text)


cliente = httpx.Client()


"""
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36
"""

url = "https://translate.google.com.br/?sl=en&tl=pt&text=Hi&op=translate"

user_agent = {"User-agent": "Mozilla/5.0"}

ree = requests.get(url, headers=user_agent)

us = cliente

r = cliente.get("https://translate.google.com.br/?sl=en&tl=pt&text=Hi&op=translate")

print(tk)
print(ree.text)

salva = open("estudos_python/exibi_palavras/index.html", "w")
salva.write(ree.text)
salva.close()
print(simples)