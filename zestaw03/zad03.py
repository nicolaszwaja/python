import numpy as np
import matplotlib as plt

def rysuj(wielomian, x_min, x_max):
    x_val = np.linspace(x_min, x_max, 200)
    y_val = np.array([eval(wielomian) for x in x_val])

    plt.plot(x_val, y_val)
    plt.title('Wielomian: ' + wielomian)
    plt.xlabel('Oś X')
    plt.ylabel('Oś Y')
    plt.grid(True)
    plt.show()

# przykład
wielomian_input = input("Podaj wielomian (np. 5*x**4+2*x**3-x+6): ")
x_min_input = float(input("Podaj x_min: "))
x_max_input = float(input("Podaj x_max: "))

rysuj(wielomian_input, x_min_input, x_max_input)