from typing import Optional
from ..models.student import Student
from ..models.pesel import PESEL, Plec
from ..repository.student_repository import BazaStudentow

class InterfejsKonsoli:
    def __init__(self, baza: BazaStudentow):
        self.baza = baza

    def uruchom(self) -> None:
        """Uruchamia główną pętlę aplikacji."""
        while True:
            self._wyswietl_menu()
            wybor = input("Wybierz opcję: ")

            if wybor == "0":
                print("Koniec programu.")
                break

            akcje = {
                "1": self._dodaj_studenta,
                "2": self._wyswietl_studentow,
                "3": self._szukaj_po_nazwisku,
                "4": self._szukaj_po_peselu,
                "5": self._sortuj_po_peselu,
                "6": self._sortuj_po_nazwisku,
                "7": self._usun_studenta,
                "8": self._aktualizuj_studenta
            }

            akcja = akcje.get(wybor)
            if akcja:
                try:
                    akcja()
                except Exception as e:
                    print(f"Wystąpił błąd: {e}")
            else:
                print("Nieprawidłowy wybór. Spróbuj ponownie.\n")

    def _wyswietl_menu(self) -> None:
        """Wyświetla główne menu."""
        print("\n============ MENU ============")
        print("1. Dodaj nowego studenta")
        print("2. Wyświetl wszystkich studentów")
        print("3. Wyszukaj studenta po nazwisku")
        print("4. Wyszukaj studenta po PESEL")
        print("5. Posortuj według PESEL")
        print("6. Posortuj według nazwiska")
        print("7. Usuń studenta (po numerze indeksu)")
        print("8. Zaktualizuj dane studenta")
        print("0. Zakończ program")
        print("==============================")

    def _dodaj_studenta(self) -> None:
        """Obsługuje dodawanie nowego studenta."""
        print("\n[DODAWANIE STUDENTA]")
        try:
            student = self._pobierz_dane_studenta()
            if student:
                self.baza.dodaj_studenta(student)
                print("Student został dodany do bazy.")
        except ValueError as e:
            print(f"Błąd: {e}")

    def _pobierz_dane_studenta(self, istniejacy_student: Optional[Student] = None) -> Optional[Student]:
        """Pobiera dane studenta z wejścia użytkownika."""
        try:
            imie = input("Podaj imię: ") if not istniejacy_student else \
                   input(f"Nowe imię (obecne: {istniejacy_student.imie}): ") or istniejacy_student.imie
            
            nazwisko = input("Podaj nazwisko: ") if not istniejacy_student else \
                      input(f"Nowe nazwisko (obecne: {istniejacy_student.nazwisko}): ") or istniejacy_student.nazwisko
            
            adres = input("Podaj adres zamieszkania: ") if not istniejacy_student else \
                   input(f"Nowy adres (obecny: {istniejacy_student.adres}): ") or istniejacy_student.adres
            
            numer_indeksu = input("Podaj numer indeksu: ") if not istniejacy_student else \
                           input(f"Nowy numer indeksu (obecny: {istniejacy_student.numer_indeksu}): ") or istniejacy_student.numer_indeksu
            
            pesel_str = input("Podaj numer PESEL (11 cyfr): ") if not istniejacy_student else \
                       input(f"Nowy PESEL (obecny: {istniejacy_student.pesel.wartosc}): ") or istniejacy_student.pesel.wartosc

            pesel = PESEL(pesel_str)
            
            return Student(
                imie=imie,
                nazwisko=nazwisko,
                adres=adres,
                numer_indeksu=numer_indeksu,
                pesel=pesel
            )
        except ValueError as e:
            print(f"Błąd: {e}")
            return None

    def _wyswietl_studentow(self) -> None:
        """Wyświetla wszystkich studentów."""
        studenci = self.baza.pobierz_wszystkich_studentow()
        print("\n[LISTA STUDENTÓW]")
        if not studenci:
            print("Brak studentów w bazie.")
            return

        for idx, student in enumerate(studenci, start=1):
            print(f"{idx}. {student.imie} {student.nazwisko} | "
                  f"Adres: {student.adres} | "
                  f"Indeks: {student.numer_indeksu} | "
                  f"PESEL: {student.pesel.wartosc} | "
                  f"Płeć: {student.plec.value}")

    def _szukaj_po_nazwisku(self) -> None:
        """Wyszukuje studentów po nazwisku."""
        print("\n[WYSZUKIWANIE WEDŁUG NAZWISKA]")
        nazwisko = input("Podaj nazwisko: ")
        studenci = self.baza.znajdz_po_nazwisku(nazwisko)
        
        if not studenci:
            print("Nie znaleziono studentów o podanym nazwisku.")
        else:
            print(f"Znaleziono {len(studenci)} student(ów):")
            for student in studenci:
                print(f"- {student.imie} {student.nazwisko} "
                      f"(indeks: {student.numer_indeksu}, PESEL: {student.pesel.wartosc})")

    def _szukaj_po_peselu(self) -> None:
        """Wyszukuje studenta po numerze PESEL."""
        print("\n[WYSZUKIWANIE WEDŁUG PESEL]")
        pesel = input("Podaj numer PESEL: ")
        student = self.baza.znajdz_po_peselu(pesel)
        
        if not student:
            print("Nie znaleziono studenta o podanym numerze PESEL.")
        else:
            print("Znaleziono:")
            print(f"- {student.imie} {student.nazwisko} "
                  f"(indeks: {student.numer_indeksu}, adres: {student.adres})")

    def _sortuj_po_peselu(self) -> None:
        """Sortuje studentów po numerze PESEL."""
        print("\n[SORTOWANIE WEDŁUG PESEL]")
        self.baza.sortuj_po_peselu()
        print("Baza została posortowana według numeru PESEL.")

    def _sortuj_po_nazwisku(self) -> None:
        """Sortuje studentów po nazwisku."""
        print("\n[SORTOWANIE WEDŁUG NAZWISKA]")
        self.baza.sortuj_po_nazwisku()
        print("Baza została posortowana według nazwiska.")

    def _usun_studenta(self) -> None:
        """Usuwa studenta po numerze indeksu."""
        print("\n[USUWANIE STUDENTA]")
        numer_indeksu = input("Podaj numer indeksu studenta do usunięcia: ")
        if self.baza.usun_po_numerze_indeksu(numer_indeksu):
            print("Usunięto studenta/ów.")
        else:
            print("Nie znaleziono studenta o podanym numerze indeksu.")

    def _aktualizuj_studenta(self) -> None:
        """Aktualizuje dane studenta."""
        print("\n[AKTUALIZACJA DANYCH STUDENTA]")
        numer_indeksu = input("Podaj numer indeksu studenta do aktualizacji: ")
        
        studenci = [s for s in self.baza.pobierz_wszystkich_studentow() if s.numer_indeksu == numer_indeksu]
        if not studenci:
            print("Nie znaleziono studenta o podanym numerze indeksu.")
            return

        student = studenci[0]
        zaktualizowany_student = self._pobierz_dane_studenta(student)
        if zaktualizowany_student and self.baza.aktualizuj_studenta(numer_indeksu, zaktualizowany_student):
            print("Dane studenta zostały zaktualizowane.") 