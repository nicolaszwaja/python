# Tim sort

import time
from mtablica import MonitorowanaTablica
from sort1 import plot_sorting_animation
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

N = 50  


def insertion_sort(tablica: MonitorowanaTablica, left, right):
    for i in range(left + 1, right + 1):
        j = i
        while j > left and tablica[j] < tablica[j - 1]:
            tablica[j], tablica[j - 1] = tablica[j - 1], tablica[j]
            j -= 1

def merge(left, right, tablica: MonitorowanaTablica):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

def timsort(tablica: MonitorowanaTablica):
    min_run = 32
    n = len(tablica)

    for i in range(0, n, min_run):
        insertion_sort(tablica, i, min((i + min_run - 1), n - 1))

    size = min_run
    while size < n:
        for start in range(0, n, size * 2):
            midpoint = start + size - 1
            end = min((start + size * 2 - 1), (n-1))

            merge(
                left=tablica[start:midpoint + 1],
                right=tablica[midpoint + 1:end + 1],
                tablica=tablica)

        size *= 2
            

tablica = MonitorowanaTablica(0, 1000, N)

print(f"Tim Sort")
for tryb in ("R", "S","A","T"):
    tablica = MonitorowanaTablica(0, 1000, N, tryb)
    t0 = time.perf_counter()
    timsort(tablica)
    delta_t = time.perf_counter() - t0
    print(f"{tryb}:Array sorted in {delta_t*1000:.1f} ms. Number of operations: {len(tablica.pelne_kopie):.0f}.")
    
print(tablica)