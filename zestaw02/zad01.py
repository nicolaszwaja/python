# Mamy zagnieżdżoną listę, która może zawierać różne heterogeniczne typy, na przykład inną listę, ale również 
# krotkę, słownik. Dodaj element o kolejnej wartości w najbardziej zagnieżdżonej liście. Napisz program, który 
# zrobi to uniwersalnie, dla dowolnego zagnieżdżenia, również jeśli pojawią się inne typy.

def dodaj_nastepny_element(struktura):
    
    najglebsze_listy = []
    max_glebokosc = 0
    
    def przegladaj(element, glebokosc=0):
        nonlocal najglebsze_listy
        nonlocal max_glebokosc

        if isinstance(element, list):
            if glebokosc > max_glebokosc:
                max_glebokosc = glebokosc
                najglebsze_listy = [element]
            elif glebokosc == max_glebokosc:
                najglebsze_listy.append(element)

            for sub_element in element:
                przegladaj(sub_element, glebokosc + 1)
                
        if isinstance(element, dict):
            for sub_element in element.values():
                przegladaj(sub_element, glebokosc)
        if isinstance(element, tuple):
            for sub_element in element:
                przegladaj(sub_element, glebokosc + 1)

    przegladaj(struktura)

    for sublist in najglebsze_listy:
        sublist.append(
            max((x for x in sublist if not isinstance(x, (dict, tuple))), default=0) + 1
        )
    return struktura

test1 = [1, [2, 3], 4]
print(dodaj_nastepny_element(test1))
test2 = [3, 4, [2, [1, 2, [7, 8], 3, 4], 3, 4], 5, 6, 7] 
print(dodaj_nastepny_element(test2))
test3 =  [1, [3], [2]]
print(dodaj_nastepny_element(test3))
test4 = [1, 2, [3, 4, [5, {'klucz':[5, 6, 7], 'tekst': [1, 2, 3]}], 5], 'hello', 3, [4, 5, 6], (5, [6, [7, 8, 9]])]
print(dodaj_nastepny_element(test4))