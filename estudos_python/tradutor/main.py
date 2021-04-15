# from googletrans import Translator
from googletrans.gtoken import TokenAcquirer


# idioma = translator.detect(frases[0])
# frases = ["I was wondering if after all.", "To go over everything."]
# texto = traduzir(frases).text


def usuario():
    linguas = [
        "translate.google.com",
        "translate.google.co.za",
        "translate.google.co.ao",
        "translate.google.com.ar",
        "translate.google.com.au",
        "translate.google.com.br",
        "translate.google.com.cn",
        "translate.google.co.cr",
        "translate.google.com.sv",
        "translate.google.com.ec",
        "translate.google.com.ru",
        "translate.google.com.ph",
        "translate.google.com.gt",
        "translate.google.com.hk",
        "translate.google.co.id",
        "translate.google.co.il",
        "translate.google.com.my",
        "translate.google.co.nz",
        "translate.google.com.pa",
        "translate.google.com.pk",
        "translate.google.com.pe",
        "translate.google.com.pr",
        "translate.google.com.qa",
        "translate.google.co.ke",
        "translate.google.co.uk",
        "translate.google.com.do",
        "translate.google.com.sg",
        "translate.google.com.tw",
        "translate.google.com.uy",
        "translate.google.com.vn",
    ]
    user = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"

    return Translator(service_urls=linguas, user_agent=user, timeout=None)


def traduzir(frase):

    traducao = usuario().translate(frases, dest="pt")

    return traducao


frases = ["I was wondering if after all.", "To go over everything."]

# translator = Translator()

text = "test"

conta = TokenAcquirer()

# conta._update()

tk = conta.acquire(text)

print(tk)
