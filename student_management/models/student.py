from dataclasses import dataclass
from .pesel import PESEL, Plec

@dataclass
class Student:
    imie: str
    nazwisko: str
    adres: str
    numer_indeksu: str
    pesel: PESEL

    @property
    def plec(self) -> Plec:
        return self.pesel.pobierz_plec()

    def do_slownika(self) -> dict:
        """Konwertuje obiekt studenta do słownika do serializacji JSON."""
        return {
            "first_name": self.imie,
            "last_name": self.nazwisko,
            "address": self.adres,
            "index_number": self.numer_indeksu,
            "pesel": self.pesel.wartosc,
            "gender": self.plec.value
        }

    @classmethod
    def ze_slownika(cls, dane: dict) -> 'Student':
        """Tworzy instancję Studenta ze słownika."""
        return cls(
            imie=dane["first_name"],
            nazwisko=dane["last_name"],
            adres=dane["address"],
            numer_indeksu=dane["index_number"],
            pesel=PESEL(dane["pesel"])
        ) 