# Napisać program konwertujący liczby zapisane w systemie rzymskim (wielkimi literami I, V, X, L, C, D, M) 
# na liczby arabskie w zakresie liczb 1-3999, i odwrotnie. Proszę kontrolować poprawność danych wejściowy, 
# również w formacie rzymskim. Proszę spróbować napisać najbardziej kompaktowy (krótki) kod

def czy_poprawna_rzymska(rzymska):
    poprawne_znaki = set('IVXLCDM')
    niedozwolone = {'IL', 'IC', 'ID', 'IM', 'XD', 'XM', 'VX', 'VL', 'VC', 'VD', 'VM', 'IM', 'VM', 'XM', 'LM', 'DM', 'DD', 'LL', 'VV', 'IIII', 'XXXX', 'CCCC', 'MMMM'}

    if not all(znak in poprawne_znaki for znak in rzymska):
        return False

    for x in niedozwolone:
        if x in rzymska:
            # print(x)
            return False

    return True

def rzymska_na_arabska(rzymska):
    rzymskie_cyfry = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50,
                      'XC': 90, 'C': 100, 'CD': 400, 'D': 500, 'CM': 900, 'M': 1000}
    arabska = 0
    i = 0
    while i < len(rzymska):
        if i + 1 < len(rzymska) and rzymska[i:i + 2] in rzymskie_cyfry:
            arabska += rzymskie_cyfry[rzymska[i:i + 2]]
            i += 2
        else:
            arabska += rzymskie_cyfry[rzymska[i]]
            i += 1
    return arabska

rzymska_input = input("podaj liczbę rzymską: ")
rzymska_input = rzymska_input.upper()
if not czy_poprawna_rzymska(rzymska_input):
    print("niepoprawne dane wejściowe")
    exit(1)
else:
    arabska_output = rzymska_na_arabska(rzymska_input)
    print(f"liczba arabska: {arabska_output}")
    