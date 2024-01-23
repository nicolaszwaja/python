# Shell sort

import time
from mtablica import MonitorowanaTablica
from sort1 import plot_sorting_animation
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

N = 50  

def shellsort(tablica: MonitorowanaTablica):
    h = 1
    while h <= (len(tablica) - 1) // 9:
        h = 3 * h + 1
    while h > 0:
        for i in range(h, len(tablica)):
            j = i
            item = tablica[i]
            while j >= h and item < tablica[j - h]:
                tablica[j] = tablica[j - h]
                j = j - h
            tablica[j] = item
        h = h // 3
            
tablica = MonitorowanaTablica(0, 1000, N)

print(f"Shell Sort")
for tryb in ("R", "S","A","T"):
    tablica = MonitorowanaTablica(0, 1000, N, tryb)
    t0 = time.perf_counter()
    shellsort(tablica)
    delta_t = time.perf_counter() - t0
    print(f"{tryb}:Array sorted in {delta_t*1000:.1f} ms. Number of operations: {len(tablica.pelne_kopie):.0f}.")