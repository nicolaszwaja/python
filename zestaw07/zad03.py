# Merge sort
import time
from mtablica import MonitorowanaTablica
from sort1 import plot_sorting_animation
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

N = 50  
def mergesort(tablica: MonitorowanaTablica):
    def merge(L, left, middle, right):
        n1 = middle - left + 1
        n2 = right - middle
        A = [None] * (n1 + 1)   # o jeden więcej
        B = [None] * (n2 + 1)   # o jeden więcej
        for i in range(n1):
            A[i] = L[left + i]
        for i in range(n2):
            B[i] = L[middle + 1 + i]
        A[n1] = float("inf")   
        B[n2] = float("inf")
        i, j = 0, 0
        for k in range(left, right + 1):
            if A[i] <= B[j]:
                L[k] = A[i]
                i += 1
            else:
                L[k] = B[j]
                j += 1
    
    def _mergesort(L, left, right):
        if left < right:
            middle = (left + right) // 2   # wyznaczanie środka 
            _mergesort(L, left, middle)
            _mergesort(L, middle + 1, right)
            merge(L, left, middle, right)   # scalanie
    _mergesort(tablica, 0, len(tablica) - 1)


tablica = MonitorowanaTablica(0, 1000, N)

print(f"Merge Sort")
for tryb in ("R", "S","A","T"):
    tablica = MonitorowanaTablica(0, 1000, N, tryb)
    t0 = time.perf_counter()
    mergesort(tablica)
    delta_t = time.perf_counter() - t0
    print(f"{tryb}:Array sorted in {delta_t*1000:.1f} ms. Number of operations: {len(tablica.pelne_kopie):.0f}.")