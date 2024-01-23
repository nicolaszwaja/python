# Bubble sort

import time
from mtablica import MonitorowanaTablica
from sort1 import plot_sorting_animation
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

N = 50  

def bubble_sort(tablica: MonitorowanaTablica):
    n = len(tablica)
    limit = n
    while True:
        k = -1
        for i in range(0, limit - 1):
            if tablica[i] > tablica[i+1]:
                tablica[i], tablica[i+1] = tablica[i+1], tablica[i]
                k = i
        if k > -1:
            limit = k
        else:
            break
            

tablica = MonitorowanaTablica(0, 1000, N)

print(f"Bubble Sort")
for tryb in ("R", "S","A","T"):
    tablica = MonitorowanaTablica(0, 1000, N, tryb)
    t0 = time.perf_counter()
    bubble_sort(tablica)
    delta_t = time.perf_counter() - t0
    print(f"{tryb}:Array sorted in {delta_t*1000:.1f} ms. Number of operations: {len(tablica.pelne_kopie):.0f}.")