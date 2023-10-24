# Napisać program, który będzie wyświetlał bieżący czas (tak ma to wyglądać: ► 14:48:31 ◄), 
# aktualizowany dynamicznie. Czas można odczytać na wiele sposobów, użyjmy moduł datetime, 
# wtedy, bieżący punkt w czasie dostaniemy: now = datetime.now() i za pomocą składowych now.hour, 
# now.minute, now.second mamy potrzebne wartości. Przy czym dla sekund należy sprytnie podmienić 
# sekundy w zakresie 0..9 tak, żeby przed nimi wyświetlało się zero (np. nie 5, tylko 05). Znaczki na początku 
# i końcu mają kod chr(16) i chr(17). Zegar musi być wyświetlany w nieskończonej pętli funkcją print(), 
# argument end='\r' zapewni nadpisywanie. Potrzebne jest jeszcze (z modułu time) wołanie czegoś typu 
# time.sleep(0.5) w pętli, żeby niepotrzebnie nie odświeżać zbyt często bieżącego odczytu czasu.

import time
from datetime import datetime

last_second = 0
strzalka1 = chr(16)
strzalka2 = chr(17)

while True:
    now = datetime.now()
    if now.second != last_second:
        last_second = now.second
        current_time = f"{now.hour}:{now.minute}:{now.second:02d}"
        print(f"{strzalka1}  {current_time}  {strzalka2}", end="\r")
    time.sleep(0.5)