from datetime import datetime
from dataclasses import dataclass
from enum import Enum

class Plec(Enum):
    MEZCZYZNA = 'M'
    KOBIETA = 'K'

@dataclass
class PESEL:
    wartosc: str
    
    def __post_init__(self):
        if not self.czy_poprawny():
            raise ValueError("Niepoprawny numer PESEL")

    def czy_poprawny(self) -> bool:
        """Sprawdza, czy numer PESEL jest poprawny."""
        if len(self.wartosc) != 11 or not self.wartosc.isdigit():
            return False
        
        return self._sprawdz_sume_kontrolna() and self._sprawdz_date_urodzenia()

    def _sprawdz_sume_kontrolna(self) -> bool:
        """Sprawdza sumę kontrolną numeru PESEL."""
        wagi = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
        suma_kontrolna = sum(int(self.wartosc[i]) * wagi[i] for i in range(10))
        cyfra_kontrolna = (10 - (suma_kontrolna % 10)) % 10
        return cyfra_kontrolna == int(self.wartosc[10])

    def _sprawdz_date_urodzenia(self) -> bool:
        """Sprawdza, czy data urodzenia zakodowana w PESEL jest poprawna."""
        try:
            rok = int(self.wartosc[0:2])
            miesiac = int(self.wartosc[2:4])
            dzien = int(self.wartosc[4:6])

            stulecie = self._pobierz_stulecie(miesiac)
            if stulecie is None:
                return False

            miesiac = self._dostosuj_miesiac(miesiac)
            rok = stulecie + rok

            datetime(rok, miesiac, dzien)
            return True
        except ValueError:
            return False

    def _pobierz_stulecie(self, miesiac: int) -> int:
        """Zwraca stulecie na podstawie kodowania miesiąca w PESEL."""
        if 1 <= miesiac <= 12:
            return 1900
        elif 21 <= miesiac <= 32:
            return 2000
        elif 41 <= miesiac <= 52:
            return 2100
        elif 61 <= miesiac <= 72:
            return 2200
        elif 81 <= miesiac <= 92:
            return 1800
        return None

    def _dostosuj_miesiac(self, miesiac: int) -> int:
        """Dostosowuje numer miesiąca na podstawie kodowania stulecia."""
        if 21 <= miesiac <= 32:
            return miesiac - 20
        elif 41 <= miesiac <= 52:
            return miesiac - 40
        elif 61 <= miesiac <= 72:
            return miesiac - 60
        elif 81 <= miesiac <= 92:
            return miesiac - 80
        return miesiac

    def pobierz_plec(self) -> Plec:
        """Zwraca płeć na podstawie numeru PESEL."""
        return Plec.MEZCZYZNA if int(self.wartosc[9]) % 2 != 0 else Plec.KOBIETA

    def pobierz_date_urodzenia(self) -> datetime:
        """Zwraca datę urodzenia z numeru PESEL."""
        rok = int(self.wartosc[0:2])
        miesiac = int(self.wartosc[2:4])
        dzien = int(self.wartosc[4:6])
        
        stulecie = self._pobierz_stulecie(miesiac)
        miesiac = self._dostosuj_miesiac(miesiac)
        rok = stulecie + rok
        
        return datetime(rok, miesiac, dzien) 