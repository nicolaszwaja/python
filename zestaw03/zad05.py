class Bug:
    """
    Klasa reprezentująca obiekty typu Bug.

    Każdy obiekt Bug posiada unikalny identyfikator i współdzielony licznik,
    który zwiększa się przy tworzeniu obiektu i zmniejsza przy jego niszczeniu.
    """
    licznik = 0

    def __init__(self):
        """
        Konstruktor inicjalizujący nowy obiekt Bug.

        Zwiększa współdzielony licznik i przypisuje identyfikator obiektu.
        """
        Bug.licznik += 1
        self.id = Bug.licznik

    def __del__(self):
        """
        Destruktor niszczący obiekt Bug.

        Zmniejsza współdzielony licznik i wypisuje informację o zniszczeniu obiektu.
        """
        Bug.licznik -= 1
        print(f'koniec, licznik: {Bug.licznik}, identyfikator: {self.id}')

    def __str__(self):
        """
        Metoda zwracająca string z licznikiem i identyfikatorem obiektu Bug.
        """
        return f'licznik: {Bug.licznik}, identyfikator: {self.id}'

bugs = []
for i in range(100):
    bugs.append(Bug())
    print(bugs[-1])
