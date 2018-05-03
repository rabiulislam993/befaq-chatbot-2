import re

bijoy_string_conversion_map = {
    # <JUKTAKHKHOR>
    "i¨": "র‌্য",
    "ª¨": "্র্য",
    "°": "ক্ক",
    "±": "ক্ট",
    "³": "ক্ত",
    "K¡": "ক্ব",
    "¯Œ": "স্ক্র",
    "µ": "ক্র",
    "K¬": "ক্ল",
    "ÿ": "ক্ষ",
    "¸": "গু",
    "»": "গ্ধ",
    "Mœ": "গ্ন",
    "M¥": "গ্ম",
    "Mø": "গ্ল",
    "¼": "ঙ্ক",
    "•¶": "ঙ্ক্ষ",
    "•L": "ঙ্খ",
    "½": "ঙ্গ",
    "•N": "ঙ্ঘ",
    "•": "ক্স",
    "”P": "চ্চ",
    "”Q": "চ্ছ",
    "”Q¡": "চ্ছ্ব",
    "”T": "চ্ঞ",
    "¾¡": "জ্জ্ব",
    "¾": "জ্জ",
    "À": "জ্ঝ",
    "Á": "জ্ঞ",
    "R¡": "জ্ব",
    "Â": "ঞ্চ",
    "Ã": "ঞ্ছ",
    "Ä": "ঞ্জ",
    "Å": "ঞ্ঝ",
    "Æ": "ট্ট",
    "U¡": "ট্ব",
    "U¥": "ট্ম",
    "Ç": "ড্ড",
    "È": "ণ্ট",
    "É": "ণ্ঠ",
    "Ý": "ন্স",
    "Ð": "ণ্ড",
    "š‘": "ন্তু",
    "Y^": "ণ্ব",
    "Ë": "ত্ত",
    "Ë¡": "ত্ত্ব",
    "Ì": "ত্থ",
    "Z¥": "ত্ম",
    "šÍ¡": "ন্ত্ব",
    "Z¡": "ত্ব",
    "Î": "ত্র",
    "_¡": "থ্ব",
    "˜M": "দ্গ",
    "˜N": "দ্ঘ",
    "Ï": "দ্দ",
    "×": "দ্ধ",
    "˜¡": "দ্ব",
    "Ø": "দ্ব",
    "™¢": "দ্ভ",
    "Ù": "দ্ম",
    "`ªæ": "দ্রু",
    "aŸ": "ধ্ব",
    "a¥": "ধ্ম",
    "›U": "ন্ট",
    "Ú": "ন্ঠ",
    "Û": "ন্ড",
    "šÍ": "ন্ত",
    "š¿": "ন্ত্র",
    "š’": "ন্থ",
    "›`": "ন্দ",
    "›Ø": "ন্দ্ব",
    "Ü": "ন্ধ",
    "bœ": "ন্ন",
    "š^": "ন্ব",
    "b¥": "ন্ম",
    "Þ": "প্ট",
    "ß": "প্ত",
    "cœ": "প্ন",
    "à": "প্প",
    "cø": "প্ল",
    "á": "প্স",
    "d¬": "ফ্ল",
    "â": "ব্জ",
    "ã": "ব্দ",
    "ä": "ব্ধ",
    "eŸ": "ব্ব",
    "eø": "ব্ল",
    "å": "ভ্র",
    "gœ": "ম্ন",
    "¤ú": "ম্প",
    "ç": "ম্ফ",
    "¤\\^": "ম্ব",  # ম্ব ¤\\^ #¤^
    "¤¢": "ম্ভ",
    "¤£": "ম্ভ্র",
    "¤§": "ম্ম",
    "¤ø": "ম্ল",
    "iæ": "রু",
    "iƒ": "রূ",
    "é": "ল্ক",
    "ê": "ল্গ",
    "ë": "ল্ট",
    "ì": "ল্ড",
    "í": "ল্প",
    "î": "ল্ফ",
    "j¦": "ল্ব",
    "j¥": "ল্ম",
    "jø": "ল্ল",
    "ï": "শু",
    "ð": "শ্চ",
    "kœ": "শ্ন",
    "k¦": "শ্ব",
    "k¥": "শ্ম",
    "kø": "শ্ল",
    "®‹": "ষ্ক",
    "®Œ": "ষ্ক্র",
    "ó": "ষ্ট",
    "ô": "ষ্ঠ",
    "ò": "ষ্ণ",
    "®ú": "ষ্প",
    "õ": "ষ্ফ",
    "®§": "ষ্ম",
    "¯‹": "স্ক",
    "÷": "স্ট",
    "ö": "স্খ",
    "¯Í": "স্ত",
    "¯‘": "স্তু",
    "¯¿": "স্ত্র",
    "¯’": "স্থ",
    "mœ": "স্ন",
    "¯ú": "স্প",
    "ù": "স্ফ",
    "¯^": "স্ব",
    "¯§": "স্ম",
    "mø": "স্ল",
    "û": "হু",
    "nè": "হ্ণ",
    "ý": "হ্ন",
    "þ": "হ্ম",
    "n¬": "হ্ল",
    "ü": "হৃ",
    "©": "র্",

    # <VOWELS>
    "Av": "আ",
    "A": "অ",
    "B": "ই",
    "C": "ঈ",
    "D": "উ",
    "E": "ঊ",
    "F": "ঋ",
    "G": "এ",
    "H": "ঐ",
    "I": "ও",
    "J": "ঔ",

    # <CONSONANTS>
    "K": "ক",
    "L": "খ",
    "M": "গ",
    "N": "ঘ",
    "O": "ঙ",
    "P": "চ",
    "Q": "ছ",
    "R": "জ",
    "S": "ঝ",
    "T": "ঞ",
    "U": "ট",
    "V": "ঠ",
    "W": "ড",
    "X": "ঢ",
    "Y": "ণ",
    "Z": "ত",
    "_": "থ",
    "`": "দ",
    "a": "ধ",
    "b": "ন",
    "c": "প",
    "d": "ফ",
    "e": "ব",
    "f": "ভ",
    "g": "ম",
    "h": "য",
    "i": "র",
    "j": "ল",
    "k": "শ",
    "l": "ষ",
    "m": "স",
    "n": "হ",
    "o": "ড়",
    "p": "ঢ়",
    "q": "য়",
    "r": "ৎ",

    # <DIGITS>
    "0": "০",
    "1": "১",
    "2": "২",
    "3": "৩",
    "4": "৪",
    "5": "৫",
    "6": "৬",
    "7": "৭",
    "8": "৮",
    "9": "৯",

    # Kars
    "v": "া",
    "w": "ি",
    "x": "ী",
    "y": "ু",
    "z": "ু",
    "~": "ূ",
    "„": "ৃ",
    "‡": "ে",
    "†": "ে",
    "‰": "ৈ",
    "ˆ": "ৈ",
    "Š": "ৗ",

    # signs
    "Ô": "‘",
    "Õ": "’",
    "\\|": "।",
    "Ò": "“",
    "Ó": "”",

    # Complex
    "s": "ং",
    "t": "ঃ",
    "u": "ঁ",
    "ª": "্র",
    "Ö": "্র",
    "«": "্র",
    "¨": "্য",
    "\\&": "্",
    "…": "ৃ"
}

def IsBanglaDigit(c):
    if c >= '০' and c <= '৯':
        return True
    return False


def IsBanglaPreKar(c):
    if c == 'ি' or c == 'ৈ' or c == 'ে':
        return True
    return False


def IsBanglaPostKar(c):
    if c == 'া' or c == 'ো' or c == 'ৌ' or c == 'ৗ' or c == 'ু' or c == 'ূ' or c == 'ী' or c == 'ৃ':
        return True
    return False


def IsBanglaKar(c):
    if IsBanglaPreKar(c) or IsBanglaPostKar(c):
        return True
    return False


def IsBanglaBanjonborno(c):
    if c == 'ক' or c == 'খ' or c == 'গ' or c == 'ঘ' or c == 'ঙ' or c == 'চ' or c == 'ছ' or c == 'জ' or c == 'ঝ' or c == 'ঞ' or c == 'ট' or c == 'ঠ' or c == 'ড' or c == 'ঢ' or c == 'ণ' or c == 'ত' or c == 'থ' or c == 'দ' or c == 'ধ' or c == 'ন' or c == 'প' or c == 'ফ' or c == 'ব' or c == 'ভ' or c == 'ম' or c == 'য' or c == 'র' or c == 'ল' or c == 'শ' or c == 'ষ' or c == 'স' or c == 'হ' or c == 'ড়' or c == 'ঢ়' or c == 'য়' or c == 'ৎ' or c == 'ং' or c == 'ঃ' or c == 'ঁ':
        return True
    return False


def IsBanglaSoroborno(c):
    if c == 'অ' or c == 'আ' or c == 'ই' or c == 'ঈ' or c == 'উ' or c == 'ঊ' or c == 'ঋ' or c == 'ঌ' or c == 'এ' or c == 'ঐ' or c == 'ও' or c == 'ঔ':
        return True
    return False


def IsBanglaNukta(c):
    if c == 'ঁ':
        return True
    return False


def IsBanglaHalant(c):
    if c == '্':
        return True
    return False


def IsSpace(c):
    if c == ' ' or c == '\t' or c == '\n' or c == '\r':
        return True
    return False

# def IsBanglaDigit(c):
#     if (c == '০' or c == '১' or c == '২' or c == '৩' or c == '৪' or c == '৫' or c == '৬' or c == '৭' or c == '৮' or c == '৯'):
#         return True
#     return False
#
#
# def IsBanglaPreKar(c):
#     if (c == 'ি' or c == 'ৈ' or c == 'ে'):
#         return True
#
#     return False
#
#
# def IsBanglaPostKar(c):
#     if (c == 'া' or c == 'ো' or c == 'ৌ' or c == 'ৗ' or c == 'ু' or c == 'ূ' or c == 'ী' or c == 'ৃ'):
#         return True
#     return False
#
#
# def IsBanglaKar(c):
#     if (IsBanglaPreKar(c) or IsBanglaPostKar(c)):
#         return True
#     return False
#
#
# def IsBanglaBanjonborno(c):
#     if (
#                                                                                                                                                                 c == 'ক' or c == 'খ' or c == 'গ' or c == 'ঘ' or c == 'ঙ' or c == 'চ' or c == 'ছ' or c == 'জ' or c == 'ঝ' or c == 'ঞ' or c == 'ট' or c == 'ঠ' or c == 'ড' or c == 'ঢ' or c == 'ণ' or c == 'ত' or c == 'থ' or c == 'দ' or c == 'ধ' or c == 'ন' or c == 'প' or c == 'ফ' or c == 'ব' or c == 'ভ' or c == 'ম' or c == 'শ' or c == 'ষ' or c == 'স' or c == 'হ' or c == 'য' or c == 'র' or c == 'ল' or c == 'য়' or c == 'ং' or c == 'ঃ' or c == 'ঁ' or c == 'ৎ'):
#         return True
#     return False


# def IsBanglaSoroborno(c):
#     if (c == 'অ' or c == 'আ' or c == 'ই' or c == 'ঈ' or c == 'উ' or c == 'ঊ' or c == 'ঋ' or c == 'ঌ' or c == 'এ' or c == 'ঐ' or c == 'ও' or c == 'ঔ'):
#         return True
#     return False
#
#
# def IsBanglaNukta(c):
#     if (c == 'ং' or c == 'ঃ' or c == 'ঁ'):
#         return True
#     return False

#
# def IsBanglaFola(c):
#     if (c == "্য" or c == "্র"):
#         return True
#     return False


# def IsBanglaHalant(c):
#     if (c == '্'):
#         return True
#     return False

#
# def IsBangla(c):
#     if (IsBanglaDigit(c) or IsBanglaKar(c) or IsBanglaBanjonborno(c) or IsBanglaSoroborno(c) or IsBanglaNukta(
#             c) or IsBanglaFola(c) or IsBanglaHalant(c)):
#         return True
#     return False


# def IsASCII(CH):
#     if (CH >= 0 and CH < 128):
#         return True
#     return False

#
# def IsSpace(C):
#     if (C == ' ' or C == '\t' or C == '\n' or C == '\r'):
#         return True
#     return False


# def MapKarToSorborno(c):
#     CSorborno = c
#     if (c == 'া'):
#         CSorborno = 'আ'
#     elif (c == 'ি'):
#         CSorborno = 'ই'
#     elif (c == 'ী'):
#         CSorborno = 'ঈ'
#     elif (c == 'ু'):
#         CSorborno = 'উ'
#     elif (c == 'ূ'):
#         CSorborno = 'ঊ'
#     elif (c == 'ৃ'):
#         CSorborno = 'ঋ'
#     elif (c == 'ে'):
#         CSorborno = 'এ'
#     elif (c == 'ৈ'):
#         CSorborno = 'ঐ'
#     elif (c == 'ো'):
#         CSorborno = 'ও'
#     elif (c == "ো"):
#         CSorborno = 'ও'
#     elif (c == 'ৌ'):
#         CSorborno = 'ঔ'
#     elif (c == "ৌ"):
#         CSorborno = 'ঔ'
#
#     return CSorborno
#
#
# def MapSorbornoToKar(c):
#     CKar = c
#     if (c == 'আ'):
#         CKar = 'া'
#     elif (c == 'ই'):
#         CKar = 'ি'
#     elif (c == 'ঈ'):
#         CKar = 'ী'
#     elif (c == 'উ'):
#         CKar = 'ু'
#     elif (c == 'ঊ'):
#         CKar = 'ূ'
#     elif (c == 'ঋ'):
#         CKar = 'ৃ'
#     elif (c == 'এ'):
#         CKar = 'ে'
#     elif (c == 'ঐ'):
#         CKar = 'ৈ'
#     elif (c == 'ও'):
#         CKar = 'ো'
#     elif (c == 'ঔ'):
#         CKar = 'ৌ'
#
#     return CKar


def ReArrangeUnicodeConvertedText(str_):
    for i in range(len(str_)):
        # for 'Vowel + HALANT + Consonant'
        # it should be 'HALANT + Consonant + Vowel'
        if i > 0 and str_[i] == '\u09CD' and (IsBanglaKar(str_[i - 1]) or IsBanglaNukta(str_[i - 1])) and i < len(
                str_) - 1:
            temp = str_[0: i - 1]
            temp += str_[i]
            temp += str_[i + 1]
            temp += str_[i - 1]
            temp += str_[i + 2: len(str_)]
            str_ = temp

        # for 'RA (\u09B0) + HALANT + Vowel'
        # it should be 'Vowel + RA (\u09B0) + HALANT'
        if i > 0 and i < len(str_) - 1 and str_[i] == '\u09CD' and str_[i - 1] == '\u09B0' and str_[
                    i - 2] != '\u09CD' and IsBanglaKar(str_[i + 1]):
            temp = str_[0: i - 1]
            temp += str_[i + 1]
            temp += str_[i - 1]
            temp += str_[i]
            temp += str_[i + 2: len(str_)]
            str_ = temp

        # Change refs
        if i < len(str_) - 1 and str_[i] == 'র' and IsBanglaHalant(str_[i + 1]) and (not IsBanglaHalant(str_[i - 1])):
            j = 1
            while True:
                if i - j < 0:
                    break
                if IsBanglaBanjonborno(str_[i - j]) and IsBanglaHalant(str_[i - j - 1]):
                    j += 2
                elif j == 1 and IsBanglaKar(str_[i - j]):
                    j += 1
                else:
                    break

            temp = str_[0: i - j]
            temp += str_[i]
            temp += str_[i + 1]
            temp += str_[i - j: i]
            temp += str_[i + 2: len(str_)]
            str_ = temp
            i += 1
            continue

        # Change pre-kar to post format suitable for unicode
        if i < len(str_) - 1 and IsBanglaPreKar(str_[i]) and IsSpace(str_[i + 1]) == False:
            temp = str_[0: i]
            j = 1

            while IsBanglaBanjonborno(str_[i + j]):
                try:
                    if IsBanglaHalant(str_[i+j+1]):
                        j += 2
                    else:
                        break
                except:
                    break

            temp += str_[i + 1: i + j + 1]

            l = 0
            if str_[i] == 'ে' and str_[i + j + 1] == 'া':
                temp += "ো"
                l = 1
            elif str_[i] == 'ে' and str_[i + j + 1] == "ৗ":
                temp += "ৌ"
                l = 1
            else:
                temp += str_[i]
                temp += str_[i + j + l + 1: len(str_)]
                str_ = temp
                i += j

            # nukta should be placed after kars
            # if(i<len(str_)-1 and IsBanglaNukta(str_[i]) and IsBanglaPostKar(str_[i+1]))
            if i < len(str_) - 1 and str_[i] == 'ঁ' and IsBanglaPostKar(str_[i + 1]):
                temp = str_[0: i]
                temp += str_[i + 1]
                temp += str_[i]
                temp += str_[i + 2: len(str_)]
                str_ = temp

    return str_


# ======================================================
def ConvertToUnicode(line):
    conversion_map = bijoy_string_conversion_map

    for k, v in conversion_map.items():
        myRegExp = re.compile(k, re.U)
        line = re.sub(myRegExp, v, line)

    line = ReArrangeUnicodeConvertedText(line)

    myRegExp = re.compile("অা", re.U)
    line = re.sub(myRegExp, "আ", line)

    return line
