import re

def check_dice(code):
    # <liczba rzutów kostką>d/D<liczba ścianek na kostce>+/-<modyfikator wyniku>
    # \d - dowolna cyfra [0-9]
    # * - oznacza zero lub więcej wystąpień poprzedającego wyrażenia
    # d - oznacza znak d
    # + oznacza jedno lub więcej wystąpień poprzedającego wyrażenia
    # [+|-] - znak specjalny + lub znak specjalny -
    if re.match(r"^\d*d\d+[+|-]*\d*$", code, re.I) is not None:
        return True
    else:
        return False


print(check_dice("8d7+10"))  # zwraca True
print(check_dice("8s7+10"))  # zwraca False
print(check_dice("8D7+10 abcdefghijk"))  # zwraca False
print(check_dice("8d-h"))  # zwraca False
print(check_dice("2d10+20"))  # zwraca True
print(check_dice("6D3-10"))  # zwraca True
print(check_dice("D6"))  # zwraca True
