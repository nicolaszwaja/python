# Quick sort

import time
from mtablica import MonitorowanaTablica
from sort1 import plot_sorting_animation
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

N = 50  

def quicksort(tablica: MonitorowanaTablica):
    def partition(L, left, right):
        """Zwraca indeks elementu rozdzielającego."""
        x = L[right]   # element rozdzielający
        i = left
        for j in range(left, right):
            if L[j] <= x:
                L[i], L[j] = L[j], L[i]
                i += 1
        L[i], L[right] = L[right], L[i]
        return i

    def _quicksort(L, left, right):
        if left < right:
            pivot = partition(L, left, right)
            _quicksort(L, left, pivot - 1)
            _quicksort(L, pivot + 1, right)

    _quicksort(tablica, 0, len(tablica) - 1)

tablica = MonitorowanaTablica(0, 1000, N)

print(f"Quick Sort")
for tryb in ("R", "S","A","T"):
    tablica = MonitorowanaTablica(0, 1000, N, tryb)
    t0 = time.perf_counter()
    quicksort(tablica)
    delta_t = time.perf_counter() - t0
    print(f"{tryb}:Array sorted in {delta_t*1000:.1f} ms. Number of operations: {len(tablica.pelne_kopie):.0f}.")