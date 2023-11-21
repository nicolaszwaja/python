import json
with open('tramwaje.json', "r", encoding='utf-8') as plik_wejsciowy:
    dane = json.load(plik_wejsciowy)

trams = {}
wszystkie_przystanki = set() 
for tramwaj in dane['tramwaje']:
    numer_linii = int(tramwaj['linia'])
    przystanki = tuple(przystanek['nazwa'].split()[0].lower() for przystanek in tramwaj['przystanek'])
    wszystkie_przystanki.update(przystanki)
    trams[numer_linii] = przystanki

with open('tramwaje_out.json', 'w', encoding='utf-8') as plik_out:
    json.dump(trams, plik_out, ensure_ascii=False)

for numer_linii, przystanki in sorted(trams.items(), key=lambda x: len(x[1]), reverse=True):
    print(f'numer linii {numer_linii} - liczba przystanków: {len(przystanki)}')
    
print(f'\nliczba wszystkich przystanków obsługiwanych przez tramwaje: {len(wszystkie_przystanki)}')
