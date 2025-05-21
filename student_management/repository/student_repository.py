import json
from typing import List, Optional
from ..models.student import Student

class BazaStudentow:
    def __init__(self, plik_danych: str = "database.json"):
        self.plik_danych = plik_danych
        self._studenci: List[Student] = []
        self.wczytaj_dane()

    def wczytaj_dane(self) -> None:
        """Wczytuje dane studentów z pliku JSON."""
        try:
            with open(self.plik_danych, 'r', encoding='utf-8') as plik:
                dane = json.load(plik)
                self._studenci = [Student.ze_slownika(dane_studenta) for dane_studenta in dane]
        except (FileNotFoundError, json.JSONDecodeError):
            self._studenci = []

    def zapisz_dane(self) -> None:
        """Zapisuje dane studentów do pliku JSON."""
        try:
            with open(self.plik_danych, 'w', encoding='utf-8') as plik:
                dane = [student.do_slownika() for student in self._studenci]
                json.dump(dane, plik, ensure_ascii=False, indent=4)
        except Exception as e:
            raise IOError(f"Błąd podczas zapisu do pliku: {e}")

    def dodaj_studenta(self, student: Student) -> None:
        """Dodaje nowego studenta do bazy."""
        self._studenci.append(student)
        self.zapisz_dane()

    def pobierz_wszystkich_studentow(self) -> List[Student]:
        """Zwraca wszystkich studentów."""
        return self._studenci.copy()

    def znajdz_po_nazwisku(self, nazwisko: str) -> List[Student]:
        """Znajduje studentów po nazwisku."""
        return [s for s in self._studenci if s.nazwisko.lower() == nazwisko.lower()]

    def znajdz_po_peselu(self, pesel: str) -> Optional[Student]:
        """Znajduje studenta po numerze PESEL."""
        return next((s for s in self._studenci if s.pesel.wartosc == pesel), None)

    def usun_po_numerze_indeksu(self, numer_indeksu: str) -> bool:
        """Usuwa studenta(ów) po numerze indeksu."""
        poczatkowa_liczba = len(self._studenci)
        self._studenci = [s for s in self._studenci if s.numer_indeksu != numer_indeksu]
        if len(self._studenci) < poczatkowa_liczba:
            self.zapisz_dane()
            return True
        return False

    def aktualizuj_studenta(self, numer_indeksu: str, zaktualizowany_student: Student) -> bool:
        """Aktualizuje dane studenta."""
        for i, student in enumerate(self._studenci):
            if student.numer_indeksu == numer_indeksu:
                self._studenci[i] = zaktualizowany_student
                self.zapisz_dane()
                return True
        return False

    def sortuj_po_peselu(self) -> None:
        """Sortuje studentów po numerze PESEL."""
        self._studenci.sort(key=lambda s: s.pesel.wartosc)
        self.zapisz_dane()

    def sortuj_po_nazwisku(self) -> None:
        """Sortuje studentów po nazwisku."""
        self._studenci.sort(key=lambda s: s.nazwisko.lower())
        self.zapisz_dane() 