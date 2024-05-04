

#Została utworzona klasa Statystyka
class Statystyka:
    """
    Utworzony konstruktor zawierający listy:
    wartosci przechowujący wartości liczb dla jednej zmiennej.
    sortowane_wartosci to lista, która przechowuję posortowane wartości, została ona użyta w metodzie mediany.
    """
    def __init__(self):
        self.wartosci = []
        self.sortowane_wartosci = []
        self.wartosci2 = []
    """
    Metoda dodaj_dane1 zawierająca się w klasie Statystyka wprowadza wartości do listy wartosci.
    """
    def dodaj_dane1(self, nowe_wartosci):
        self.wartosci.append(nowe_wartosci)
    """
    Metoda dodaj_dane2 zawierająca się w klasie Statystyka wprowadza wartości do listy wartosci2.
    """
    def dodaj_dane2(self, nowe_wartosci2):
        self.wartosci2.append(nowe_wartosci2)

    """
    Metoda wyczysc_dane zawierająca się w klasie Statystyka ustawia listy na puste.
    Użyta po wyknonaniu obliczeń zeruje dane zawarte w listach.
    Można po powrocie do menu zrobić obliczenia na nowym zestawie danych.
    """
    def wyczysc_dane (self):
        self.wartosci = []
        self.sortowane_wartosci = []
        self.wartosci2 = []


    """
    Metoda srednia_arytmetyczna zawierająca się w klasie Statystyka oblicza średnią arytmetyczną.
    Odwołuje się do wartości zawartych w liście wartosci. srednia = sum(self.wartosci) oblicza do zmiennej srednia
    sumę wszystkich wartości zawartych w liście. Następnie / len(self.wartosci) określa długość, ilość elementów
    zawartych w liście. srednia = sum(self.wartosci) / len(self.wartosci) oblicza średnią artmetyczną dzieląc sumę
    wszystkich wartości przez ilość tych elementów. 
    return srednia Zwraca obliczoną średnią artymetyczną.
    """

    def srednia_arytmetyczna(self):
        srednia = sum(self.wartosci) / len(self.wartosci)
        return srednia

    """
    Metoda srednia_geometryczna zawierająca się w klasie Statystyka oblicza średnią geometryczną dla wartości 
    przechowywanych w liście wartosci.
    Zmienna iloczyn przechowuję wynik mnożenia wszystkich wartości z listy.
    Jest ustawiona na cyfrę 1, a nie na 0. Inaczej wynik zawsze wychodził by 0.
    for wartosc in self.wartosci: iteruje przez wszystkie wartości w liście wartosci.
    iloczyn = iloczyn * wartosc: do zmiennej iloczyn przypisuję mnożenie przez wartosc z listy.
    srednia_geo = iloczyn ** (1/len(self.wartosci)).Do zmiennej srednia_geo oblicza pierwiastek z liczby elementów
     z iloczynu liczb. (1/len(self.wartosci)) odpowiada za stopień pierwiastka
    zależącego od liczby elementów. 
    """
    def srednia_geometryczna(self):
        iloczyn = 1
        for wartosc in self.wartosci:
            iloczyn = iloczyn * wartosc
        srednia_geo = iloczyn ** (1/len(self.wartosci))
        return srednia_geo
    """
    Metoda mediana zawierająca się w klasie Statystyka oblicza medianę ze zbioru liczb.
    self.sortowane_wartosci = sorted(self.wartosci) pod zmienną self.sortowane_wartosci: 
    sortuje wartości rosnąco z listy self.wartosci.
    dlugosc_listy = len(self.sortowane_wartosci) pod zmienną dlugosc_listy przypisuję długość posortowanej listy.
    if dlugosc_listy % 2 == 0: sprawdza długość listy, jeśli jest liczbą parzystą, to bierze dwie środkowe wartości 
    prawy = self.sortowane_wartosci[dlugosc_listy // 2 - 1] oblicza indeks środkowego elementu z posorotowanej listy. 
    -1 odnosi się do jednego elementu do przodu od elementu środkowego.
    lewy = self.sortowane_wartosci[dlugosc_listy // 2] oblicza indeks środkowego elementu z posorotowanej listy. 
    mediana = (prawy+lewy)/2 pod zmienną mediana liczy średnią z tych dwóch elementów
    return mediana: zwraca medianę w przypadku parzystej liczbie elementów.
    else:
    mediana = self.sortowane_wartosci[dlugosc_listy // 2]
    return mediana: warunek zwraca tylko środkową wartość z posortowanej listy jako medianę.
    """
    def mediana(self):
        self.sortowane_wartosci = sorted(self.wartosci)
        dlugosc_listy = len(self.sortowane_wartosci)
        if dlugosc_listy % 2 == 0:
            prawy = self.sortowane_wartosci[dlugosc_listy // 2 - 1]
            lewy = self.sortowane_wartosci[dlugosc_listy // 2]
            mediana = (prawy+lewy)/2
            return mediana
        else:
            mediana = self.sortowane_wartosci[dlugosc_listy // 2]
            return mediana
    """
    Metoda moda zawierająca się w klasie Statystyka podaję mode, czyli najczęściej występującą wartość w zbiorze.
    licznik = {}: tworzy słownik z unikatowymi wartościami.
    for wartosc in self.wartosci: pętla przechodzi przez każdą wartość w liście.
    if wartosc in licznik
    licznik[wartosc] = licznik[wartosc] + 1:
    else:
    licznik[wartosc] = 1:
    Warunek w pętli sprawdza czy wartość istnieje już jako dany klucz. 
    Jeśli jest to zwiększa liczbę wystąpień o 1, 
    jeśli nie ma to dodawany jest nowy klucz z wartością 1. 
    max_wystapien = max(licznik.values()) nadaję zmiennej max_wystapien największą wartość występowanych jakiś wartości.
    moda = [klucz for klucz, wartosc in licznik.items() if wartosc == max_wystapien] 
    Pod zmienną moda tworzy listę, w której każdy element to klucz ze słownika licznik.
    if wartosc == max_wystapien: warunek sprawia, że dany klucz jest wybierany tylko wtedy, gdy odpowiadająca mu liczba
    wystąpień danych jest równa max_wystapien.
    return moda: zwraca mode.
    """
    def moda(self):
            licznik = {}
            for wartosc in self.wartosci:

                if wartosc in licznik:
                    licznik[wartosc] = licznik[wartosc] + 1
                else:
                    licznik[wartosc] = 1

            max_wystapien = max(licznik.values())
            moda = [klucz for klucz, wartosc in licznik.items() if wartosc == max_wystapien]
            return moda

    """
    Metoda odchylenie_standardowe zawierająca się w klasie Statystyka oblicza odchylenie standardowe dla zbioru danych
    wartości.
    srednia = sum(self.wartosci) / len(self.wartosci) pod zmienną srednia oblicza średnią arytmetyczną.
    kwadrat_roznicy = sum((n - srednia) ** 2 for n in self.wartosci) pod zmienną kwadrat_roznicy zawiera się sumowanie
    kwadratów różnic. 
    odchylenie = (kwadrat_roznicy / len(self.wartosci)) ** 0.5: obliczenia pod zmienną odchylenie liczą pierwiastek
    kwadratowy ze średniej artmetycznej ze zbioru zsumowanych kwadratów różnic i liczby elementów w zbiorze. 
    return odchylenie: zwraca odchylenie standardowe.
    """
    def odchylenie_standardowe(self):
        srednia = sum(self.wartosci) / len(self.wartosci)
        kwadrat_roznicy = sum((n - srednia) ** 2 for n in self.wartosci)
        odchylenie = (kwadrat_roznicy / len(self.wartosci)) ** 0.5
        return odchylenie

    """
    Metoda korelacja zawierająca się w klasie Statystyka oblicza współczynnik korelacji liniowej między dwiema zmiennymi.
    if len(self.wartosci) != len(self.wartosci2): warunek sprawdza czy długość zbiorów/list jest nierówna. Jeśli jest to
    zwraca nic z komunikatem błędu.
    licznik = 0: to zmienna, która przechowuje sumę iloczynów różnic między odpowiadającymi sobie punktami w dwóch zbiorach danych.
    mianownik_x = 0: ta zmienna przechowuje sumę kwadratów różnic między wartościami zmiennej X, a jej średnią.
    mianownik_y = 0: ta zmienna przechowuje sumę kwadratów różnic między wartościami zmiennej Y, a jej średnią.
    srednia_x = sum(self.wartosci) / len(self.wartosci) to średnia wartość zmiennej x
    srednia_y = sum(self.wartosci2) / len(self.wartosci2) to średnia wartość zmiennej y
    W dalszej części programu mamy pętle. for x, y in zip(self.wartosci, self.wartosci2):
    Iterując po parach punktów x, y z obu zbiorów, obliczane są różnice między wartościami, 
    a średnimi dla obu zmiennych roznica_x i roznica_y.
    Do zmiennej licznik dodaję sumę iloczynów różnic między wartościami x i y dla danej pary punktów.
    mianownik_x = mianownik_x + (roznica_x ** 2) dodaje do zmiennej mianownik_x sumę kwadratów różnic między wartościami
    x i ich średnią wartością. 
    mianownik_y = mianownik_y + (roznica_y ** 2) dodaje do zmiennej mianownik_y sumę kwadratów różnic między 
    y i ich średnią wartością .
    korelacja = licznik / ((mianownik_x ** 0.5) * (mianownik_y ** 0.5))
    return korelacja:
    We zmiennej korelacja współczynnik korelacji jest obliczany jako dzielenie licznika przez pierwiastek mnożenia 
    mianowników.
    """
    def korelacja(self):
        if len(self.wartosci) != len(self.wartosci2):
            print("Długości obu zbiorów muszą być równe.")
            return None
        licznik = 0
        mianownik_x = 0
        mianownik_y = 0
        srednia_x = sum(self.wartosci) / len(self.wartosci)
        srednia_y = sum(self.wartosci2) / len(self.wartosci2)

        for x, y in zip(self.wartosci, self.wartosci2):
            roznica_x = x - srednia_x
            roznica_y = y - srednia_y
            licznik = licznik + roznica_x * roznica_y
            mianownik_x = mianownik_x + (roznica_x ** 2)
            mianownik_y = mianownik_y + (roznica_y ** 2)
        korelacja = licznik / ((mianownik_x ** 0.5) * (mianownik_y ** 0.5))
        return korelacja
    """
     Metoda regresja_liniowa zawierająca się w klasie Statystyka oblicza współczynnik regresji liniowej między 
     dwiema zmiennymi, gdzie obliczane są dwa współczynniki a i b, na podstawie dwóch wzorów.
     Podobnie jak w metodzie korelacji warunek sprawdza długość zbiorów. Następnie są obliczane średnie wartości 
     używając n jako dłguości elementów. 
     Licznik jest obliczany za pomocą sumy mnożenia różnic między wartościami zmiennej zależnej i odpowiadającymi 
     im wartościami zmiennej niezależnej.
     Mianownik jest obliczany jako suma kwadratów różnic między wartościami zmiennej niezależnej i jej średnią.
     Współczynniki a i b są obliczane na podstawie wcześniej policzonych wartości. Na końcu program zwraca oba
     współczynniki.
    """
    def regresja_liniowa(self):
        if len(self.wartosci) != len(self.wartosci2):
            print("Długości obu zbiorów muszą być równe.")
            return None
        n = len(self.wartosci)
        srednia_x = sum(self.wartosci) / n
        srednia_y = sum(self.wartosci2) / n
        licznik = sum((x - srednia_x) * (y - srednia_y) for x, y in zip(self.wartosci, self.wartosci2))
        mianownik = sum((x - srednia_x) ** 2 for x in self.wartosci)
        a = licznik / mianownik
        b = srednia_y - a * srednia_x
        return a, b


# Interfejs konsolowy (CLI)

"""
Tworzymy funkcję oraz zmienną menu ustawioną na wartość True. 
Dopóki taka wartość jest ustawiona to pętla menu będzie wykonywać instrukcje.
W pętli wyświetlany jest interfejs tekstowy kalkulatora statystycznego. Użytkownik za pomocą wpisania cyfry
jest w stanie wybrać operację statstyczną. 

"""
def kalkulator(stat):
    menu = True
    podkreslenie = "-" * 60
    while(menu):
        print(" ")
        print("* KALKULATOR STATYSTYCZNY *")
        print(" ")
        print("Operacje statystyczne:")
        print(" ")
        print("1.Średnia arytmetyczna")
        print("2.Średnia geometryczna")
        print("3.Mediana")
        print("4.Moda")
        print("5.Odchylenie standardowe")
        print("6.Współczynnik koleracji")
        print("7.Regresja liniowa")
        print(" ")
        wybor = input("Wybierz operację za pomocą cyfry: ")
        cyfry = [1, 2, 3, 4, 5, 6, 7]
        """
        try: wybor = int(wybor): Próbuje przekształcić wprowadzoną przez użytkownika wartość na liczbę całkowitą. 
        Gdy użytkownik wprowadzi coś innego niż liczbe, obsługiwany jest wyjątek ValueError.
        if wybor in cyfry: Sprawdza, czy przekształcona wartość wybor znajduje się na liście cyfry.
        Czy jest jednym z poprawnych wyborów operacji.
        if wybor == 1: Jeśli użytkownik wybrał operację Średnia arytmetyczna odpowiadającej cyfrze 1, kod wykonuje operacje
        dotyczące tej opcji.
        while (True):Rozpoczyna pętlę nieskończoną, która umożliwia użytkownikowi dodawanie wartości do obiektu stat za 
        pomocą metody dodaj_dane1. Wartości dodawane są tak długo, aż użytkownik wpisze "k", ta opcja kończy pętlę.
        Wewnątrz pętli while, kod próbuje przekształcić wprowadzoną wartość dodawaną przez użytkownika na liczbę zmiennoprzecinkową. 
        Użytkownik przy próbie wpisania tekstu zamiast liczby, obsługiwany jest wyjątek ValueError, 
        a użytkownik proszony jest o ponowne wprowadzenie poprawnej wartości.
        if len(stat.wartosci) > 0: Sprawdza, czy w obiekcie stat zostały dodane jakiekolwiek wartości.
        Jeśli tak, wykonuje operację obliczania średniej arytmetycznej i wyświetla wynik. Inaczej pokazuję błąd o braku danych.
        stat.wyczysc_dane(): Czyści dane w obiekcie stat po zakończeniu operacji, aby umożliwić użytkownikowi wprowadzenie nowych danych.
        while (True): Po wyświetleniu wyniku, program pyta użytkownika, czy chce powrócić do menu czy zakończyć działanie programu. 
        Jeśli użytkownik wybierze M, pętla główna będzie kontynuowana. Jeśli wybierze Z, pętla główna zakończy się.
        Generalnie menu zawiera zabezpieczenia przed niechcianymi czynnościami użytkownika. Inne wybory są podobne w składni
        kodu.
        """

        try:
            wybor = int(wybor)
            if wybor in cyfry:
                if wybor == 1:
                    while (True):
                        dodajWartosci = input("Dodawaj wartość lub wpisz k aby zakończyć uzupełnianie: ")
                        if dodajWartosci == "k":
                            break
                        try:
                            dodajWartosci = float(dodajWartosci)
                            stat.dodaj_dane1(dodajWartosci)
                        except ValueError:
                            print("Niepoprawny typ danych, spróbuj ponownie")

                    if len(stat.wartosci) > 0:
                        wynik = stat.srednia_arytmetyczna()
                        print(podkreslenie)
                        print(f"Średnia arytmetyczna wynosi: {wynik}")
                        print(podkreslenie)
                        stat.wyczysc_dane()
                        while (True):
                            menu = input("Powrót do menu-M, zakończ program-Z ").upper()
                            if menu == "M" or menu == "Z":
                                break
                            else:
                                print("Wprowadź poprawną literę")
                                print(" ")
                        if menu == "M":
                            menu = True
                        else:
                            menu = False
                    else:
                        print("Brak danych, spróbuj ponownie")

                elif wybor == 2:
                    while (True):
                        dodajWartosci = input("Dodawaj wartość lub wpisz k aby zakończyć uzupełnianie: ")
                        if dodajWartosci == "k":
                            break
                        try:
                            dodajWartosci = float(dodajWartosci)
                            stat.dodaj_dane1(dodajWartosci)
                        except ValueError:
                            print("Niepoprawny typ danych, spróbuj ponownie")

                    if len(stat.wartosci) > 0:
                        wynik = stat.srednia_geometryczna()
                        print(podkreslenie)
                        print(f"Średnia geometryczna wynosi: {wynik}")
                        print(podkreslenie)
                        stat.wyczysc_dane()
                        while (True):
                            menu = input("Powrót do menu-M, zakończ program-Z ").upper()
                            if menu == "M" or menu == "Z":
                                break
                            else:
                                print("Wprowadź poprawną literę")
                                print(" ")
                        if menu == "M":
                            menu = True
                        else:
                            menu = False
                    else:
                        print("Brak danych, spróbuj ponownie")
                        print(f"{podkreslenie}")

                elif wybor == 3:
                    while (True):
                        dodajWartosci = input("Dodawaj wartość lub wpisz k aby zakończyć uzupełnianie: ")
                        if dodajWartosci == "k":
                            break
                        try:
                            dodajWartosci = float(dodajWartosci)
                            stat.dodaj_dane1(dodajWartosci)
                        except ValueError:
                            print("Niepoprawny typ danych, spróbuj ponownie")

                    if len(stat.wartosci) > 0:
                        wynik = stat.mediana()
                        print(podkreslenie)
                        print(f"Mediana wynosi: {wynik}")
                        print(podkreslenie)
                        stat.wyczysc_dane()

                        while (True):
                            menu = input("Powrót do menu-M, zakończ program-Z ").upper()
                            if menu == "M" or menu == "Z":
                                break
                            else:
                                print("Wprowadź poprawną literę")
                                print(" ")
                        if menu == "M":
                            menu = True
                        else:
                            menu = False

                    else:
                        print("Brak danych, spróbuj ponownie")

                elif wybor == 4:
                    while (True):
                        dodajWartosci = input("Dodawaj wartość lub wpisz k aby zakończyć uzupełnianie: ")
                        if dodajWartosci == "k":
                            break
                        try:
                            dodajWartosci = float(dodajWartosci)
                            stat.dodaj_dane1(dodajWartosci)
                        except ValueError:
                            print("Niepoprawny typ danych, spróbuj ponownie")

                    if len(stat.wartosci) > 0:
                        wynik = stat.moda()
                        if len(wynik) == len(set(stat.wartosci)):
                            print("Nie można wyznaczyć dominującej wartości.")
                        else:
                            print(podkreslenie)
                            print(f"Moda wynosi: {wynik}")
                            print(podkreslenie)
                        stat.wyczysc_dane()
                        while (True):
                            menu = input("Powrót do menu-M, zakończ program-Z ").upper()
                            if menu == "M" or menu == "Z":
                                break
                            else:
                                print("Wprowadź poprawną literę")
                                print(" ")
                        if menu == "M":
                            menu = True
                        else:
                            menu = False
                    else:
                        print("Brak danych, spróbuj ponownie")

                elif wybor == 5:
                    while (True):
                        dodajWartosci = input("Dodawaj wartość lub wpisz k aby zakończyć uzupełnianie: ")
                        if dodajWartosci == "k":
                            break
                        try:
                            dodajWartosci = float(dodajWartosci)
                            stat.dodaj_dane1(dodajWartosci)
                        except ValueError:
                            print("Niepoprawny typ danych, spróbuj ponownie")

                    if len(stat.wartosci) > 1:
                        wynik = stat.odchylenie_standardowe()
                        print(podkreslenie)
                        print(f"Odchylenie standardowe wynosi: {wynik}")
                        print(podkreslenie)
                        stat.wyczysc_dane()
                        while (True):
                            menu = input("Powrót do menu-M, zakończ program-Z ").upper()
                            if menu == "M" or menu == "Z":
                                break
                            else:
                                print("Wprowadź poprawną literę")
                                print(" ")
                        if menu == "M":
                            menu = True
                        else:
                            menu = False
                    else:
                        print("Za mało danych, spróbuj ponownie")

                elif wybor == 6:
                    while (True):
                        dodajWartosci_x = input("Dodawaj wartość x lub wpisz k aby zakończyć uzupełnianie: ")
                        if dodajWartosci_x == "k":
                            break
                        try:
                            dodajWartosci_x = float(dodajWartosci_x)
                            stat.dodaj_dane1(dodajWartosci_x)
                        except ValueError:
                            print("Niepoprawny typ danych, spróbuj ponownie")
                    while (True):
                        dodajWartosci_y = input("Dodawaj wartość y lub wpisz k aby zakończyć uzupełnianie: ")
                        if dodajWartosci_y == "k":
                            break
                        try:
                            dodajWartosci_y = float(dodajWartosci_y)
                            stat.dodaj_dane2(dodajWartosci_y)
                        except ValueError:
                            print("Niepoprawny typ danych, spróbuj ponownie")
                    if len(stat.wartosci) > 1 and len(stat.wartosci2) > 1:
                        wynik = stat.korelacja()
                        print(podkreslenie)
                        print(f"Współczynnik korelacji liniowej wynosi: {wynik}")
                        print(podkreslenie)
                        stat.wyczysc_dane()
                        while (True):
                            menu = input("Powrót do menu-M, zakończ program-Z ").upper()
                            if menu == "M" or menu == "Z":
                                break
                            else:
                                print("Wprowadź poprawną literę")
                                print(" ")
                        if menu == "M":
                            menu = True
                        else:
                            menu = False
                    else:
                        print("Za mało danych, spróbuj ponownie")

                elif wybor == 7:
                    while (True):
                        dodajWartosci_x = input("Dodaj wartość x lub wpisz k, aby zakończyć uzupełnianie: ")
                        if dodajWartosci_x == "k":
                            break
                        try:
                            dodajWartosci_x = float(dodajWartosci_x)
                            stat.dodaj_dane1(dodajWartosci_x)
                        except ValueError:
                            print("Niepoprawny typ danych, spróbuj ponownie")
                    while (True):
                        dodajWartosci_y = input("Dodawaj wartość y lub wpisz k aby zakończyć uzupełnianie: ")
                        if dodajWartosci_y == "k":
                            break
                        try:
                            dodajWartosci_y = float(dodajWartosci_y)
                            stat.dodaj_dane2(dodajWartosci_y)
                        except ValueError:
                            print("Niepoprawny typ danych, spróbuj ponownie")

                    if len(stat.wartosci) > 1 and len(stat.wartosci2) > 1:
                        a, b = stat.regresja_liniowa()
                        print(podkreslenie)
                        print(f"Współczynniki regresji liniowej wynoszą: a = {a}, b = {b}")
                        print(podkreslenie)
                        stat.wyczysc_dane()
                        while (True):
                            menu = input("Powrót do menu-M, zakończ program-Z ").upper()
                            if menu == "M" or menu == "Z":
                                break
                            else:
                                print("Wprowadź poprawną literę")
                                print(" ")
                        if menu == "M":
                            menu = True
                        else:
                            menu = False
                    else:
                        print("Za mało danych, spróbuj ponownie")
        except ValueError:
            print("Błąd, wprowadź cyfrę odpowiadającą operacji.")
"""
Dzięki przypisaniu do zmiennej obiekt klasy Statystyka
Jesteśmy w stanie używać metody zawarte w tej klasie i dodawać dane.
Wywołujemy funkcję z obiektem jako argument funkcji kalkulator.
"""
stat = Statystyka()
kalkulator(stat)
