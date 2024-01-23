import time
from mtablica import MonitorowanaTablica
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

################################################################
################################################################
def insertion_sort(tablica: MonitorowanaTablica):
    '''Performs the insertion sort on the given array.
    
    Args:
    tablica (MonitorowanaTablica): The array to be sorted.
    '''
    i = 1
    while i < len(tablica):
        j = i
        while j > 0 and tablica[j-1] > tablica[j]:
            tablica[j-1], tablica[j] = tablica[j], tablica[j-1]
            j -= 1
        i += 1
################################################################


################################################################
def plot_sorting_animation(tablica: MonitorowanaTablica, algorithm_name: str, fps=60):
    '''Plots the sorting animation for the given data.
    
    Args:
    tablica (MonitorowanaTablica): The array being sorted.
    algorithm_name (str): Name of the sorting algorithm.
    fps (int): Frames per second for the animation.
    '''
    plt.rcParams['font.size'] = 16
    fig, ax = plt.subplots(figsize=(16, 8))
    container = ax.bar(range(len(tablica)), tablica.pelne_kopie[0], align='edge', width=0.8)
    fig.suptitle(f'Sorting: {algorithm_name}')
    ax.set(xlabel='Index', ylabel='Value')
    ax.set_xlim([0, len(tablica)])
    txt = ax.text(0.01, 0.99, '', ha='left', va='top', transform=ax.transAxes)

    def update(frame: int):
        '''Updates the histogram for each frame of the animation.
        
        Args:
        frame (int): The current frame number.
        '''
        txt.set_text(f'Operations = {frame}')
        for rectangle, height in zip(container.patches, tablica.pelne_kopie[frame]):
            rectangle.set_height(height)
            rectangle.set_color('darkblue')

        idx, op = tablica.aktywnosc(frame)
        if op == 'get':
            container.patches[idx].set_color('green')
        elif op == 'set':
            container.patches[idx].set_color('red')

        return (txt, *container)

    ani = FuncAnimation(fig, update, frames=range(len(tablica.pelne_kopie)), blit=True, interval=1000./fps, repeat=False)
    plt.show()
################################################################


################################################################
def main():
    N = 50  # Number of elements, can be changed
    FPS = 60  # Frames per second for the animation

    # Initialize the array
    tablica = MonitorowanaTablica(0, 1000, N, "R")  # Explore other options: "S", "A", "T"

    # Perform the sorting
    t0 = time.perf_counter()
    insertion_sort(tablica)
    delta_t = time.perf_counter() - t0

    print(f"Sorting: Insertion")
    print(f"Array sorted in {delta_t*1000:.1f} ms. Number of operations: {len(tablica.pelne_kopie):.0f}.")

    # Plot the sorting animation
    plot_sorting_animation(tablica, "Insertion", FPS)
################################################################


################################################################
# Call the main function
if __name__ == '__main__':
    main()
