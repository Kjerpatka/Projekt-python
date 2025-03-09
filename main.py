import json
from datetime import datetime

DATA_FILE = "database.json"

def load_data():
    """
    Wczytuje dane studentów z pliku JSON.
    Jeśli plik nie istnieje lub jest pusty, zwraca pustą listę.
    """
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_data(students):
    """
    Zapisuje listę studentów do pliku JSON.
    """
    try:
        with open(DATA_FILE, 'w', encoding='utf-8') as file:
            json.dump(students, file, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Wystąpił błąd podczas zapisu do pliku: {e}")

def validate_pesel(pesel, gender):
    """
    Waliduje numer PESEL.
    Sprawdza:
    1) Czy długość to 11 cyfr
    2) Suma kontrolna
    3) Poprawność daty urodzenia
    4) Płeć wynikająca z PESEL (parzysta cyfra = kobieta, nieparzysta = mężczyzna)
       porównywana z wprowadzonym parametrem 'gender'.
    Zwraca True, jeśli PESEL jest poprawny, w przeciwnym wypadku False.
    """

    if len(pesel) != 11 or not pesel.isdigit():
        return False

    # 1) Suma kontrolna
    weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    sum_ = 0
    for i in range(10):
        sum_ += int(pesel[i]) * weights[i]
    check_digit = (10 - (sum_ % 10)) % 10
    if check_digit != int(pesel[10]):
        return False

    # 2) Walidacja daty urodzenia
    # PESEL: RRMMDDxxxx
    # Miesiąc urodzenia jest zapisany w cyfrach [2..3] z dołożoną setką:
    #   80 -> 1800, 00 -> 1900, 20 -> 2000, 40 -> 2100, 60 -> 2200
    year = int(pesel[0:2])
    month = int(pesel[2:4])
    day = int(pesel[4:6])

    # Określenie stulecia
    century = 1900
    if 1 <= month <= 12:
        century = 1900
    elif 21 <= month <= 32:
        century = 2000
        month -= 20
    elif 41 <= month <= 52:
        century = 2100
        month -= 40
    elif 61 <= month <= 72:
        century = 2200
        month -= 60
    elif 81 <= month <= 92:
        century = 1800
        month -= 80
    else:
        # Jeśli miesiąc nie mieści się w tych widełkach, data jest błędna
        return False

    year_full = century + year

    # Sprawdzamy, czy data jest poprawna (np. 31.02. jest błędne)
    try:
        datetime(year_full, month, day)
    except ValueError:
        return False

    # 3) Sprawdzenie płci
    # 10. cyfra (indeks 9 w peselu) określa płeć: parzysta - kobieta, nieparzysta - mężczyzna
    gender_digit = int(pesel[9])
    pesel_gender = "M" if (gender_digit % 2 != 0) else "K"
    # Porównujemy z wprowadzoną płcią: przyjmijmy, że w programie
    # użytkownik wpisuje "M" albo "K" (można to dostosować).
    if gender.upper() != pesel_gender:
        return False

    return True

def add_student(students):
    """
    Dodaje nowego studenta do listy 'students'.
    Pobiera dane od użytkownika z konsoli i przeprowadza walidację PESEL.
    """
    print("\n[DODAWANIE STUDENTA]")
    first_name = input("Podaj imię: ")
    last_name = input("Podaj nazwisko: ")
    address = input("Podaj adres zamieszkania: ")
    index_number = input("Podaj numer indeksu: ")
    pesel = input("Podaj numer PESEL (11 cyfr): ")
    gender = input("Podaj płeć (M/K): ")

    if validate_pesel(pesel, gender):
        # Jeśli PESEL poprawny, dodajemy studenta do listy
        student = {
            "first_name": first_name,
            "last_name": last_name,
            "address": address,
            "index_number": index_number,
            "pesel": pesel,
            "gender": gender.upper()
        }
        students.append(student)
        save_data(students)
        print("Student został dodany do bazy.\n")
    else:
        print("BŁĄD: Niepoprawny numer PESEL lub niezgodna płeć!")

def display_students(students):
    """
    Wyświetla listę wszystkich studentów w czytelnej formie.
    """
    print("\n[LISTA STUDENTÓW]")
    if not students:
        print("Brak studentów w bazie.")
        return

    for idx, s in enumerate(students, start=1):
        print(f"{idx}. {s['first_name']} {s['last_name']} | Adres: {s['address']} "
              f"| Indeks: {s['index_number']} | PESEL: {s['pesel']} | Płeć: {s['gender']}")
    print()

def search_by_last_name(students):
    """
    Wyszukuje studentów po nazwisku i wyświetla ich dane.
    """
    print("\n[WYSZUKIWANIE WEDŁUG NAZWISKA]")
    last_name = input("Podaj nazwisko: ")
    found = [s for s in students if s['last_name'].lower() == last_name.lower()]

    if not found:
        print("Nie znaleziono studentów o podanym nazwisku.")
    else:
        print(f"Znaleziono {len(found)} student(ów):")
        for s in found:
            print(f"- {s['first_name']} {s['last_name']} (indeks: {s['index_number']}, PESEL: {s['pesel']})")
    print()

def search_by_pesel(students):
    """
    Wyszukuje studenta po numerze PESEL i wyświetla jego dane.
    """
    print("\n[WYSZUKIWANIE WEDŁUG PESEL]")
    pesel = input("Podaj numer PESEL: ")
    found = [s for s in students if s['pesel'] == pesel]

    if not found:
        print("Nie znaleziono studenta o podanym numerze PESEL.")
    else:
        print("Znaleziono:")
        for s in found:
            print(f"- {s['first_name']} {s['last_name']} (indeks: {s['index_number']}, adres: {s['address']})")
    print()

def sort_by_pesel(students):
    """
    Sortuje studentów według numeru PESEL (rosnąco).
    """
    print("\n[SORTOWANIE WEDŁUG PESEL]")
    students.sort(key=lambda s: s['pesel'])
    save_data(students)
    print("Baza została posortowana według numeru PESEL.\n")

def sort_by_last_name(students):
    """
    Sortuje studentów według nazwiska (rosnąco).
    """
    print("\n[SORTOWANIE WEDŁUG NAZWISKA]")
    students.sort(key=lambda s: s['last_name'].lower())
    save_data(students)
    print("Baza została posortowana według nazwiska.\n")

def delete_student_by_index(students):
    """
    Usuwa studenta na podstawie numeru indeksu.
    """
    print("\n[USUWANIE STUDENTA]")
    index_number = input("Podaj numer indeksu studenta do usunięcia: ")
    initial_count = len(students)
    # Usuwamy wszystkich, którzy pasują do podanego numeru indeksu
    students[:] = [s for s in students if s['index_number'] != index_number]
    final_count = len(students)

    if final_count < initial_count:
        print("Usunięto studenta/ów.")
        save_data(students)
    else:
        print("Nie znaleziono studenta o podanym numerze indeksu.")
    print()

def update_student_data(students):
    """
    Aktualizuje dane studenta na podstawie numeru indeksu.
    """
    print("\n[AKTUALIZACJA DANYCH STUDENTA]")
    index_number = input("Podaj numer indeksu studenta do aktualizacji: ")
    found = False

    for student in students:
        if student['index_number'] == index_number:
            found = True
            print("Zostaw puste pole, jeśli nie chcesz zmienić danej informacji.")
            new_first_name = input(f"Nowe imię (obecne: {student['first_name']}): ")
            new_last_name = input(f"Nowe nazwisko (obecne: {student['last_name']}): ")
            new_address = input(f"Nowy adres (obecny: {student['address']}): ")
            new_pesel = input(f"Nowy PESEL (obecny: {student['pesel']}): ")
            new_gender = input(f"Nowa płeć (obecna: {student['gender']}) (M/K): ")

            # Aktualizujemy tylko te pola, które nie są puste
            if new_first_name.strip():
                student['first_name'] = new_first_name
            if new_last_name.strip():
                student['last_name'] = new_last_name
            if new_address.strip():
                student['address'] = new_address
            if new_gender.strip():
                # tutaj można sprawdzić, czy nadal zgadza się płeć z PESEL, jeśli został zmieniony PESEL
                student['gender'] = new_gender.upper()

            if new_pesel.strip():
                # Musimy na nowo zweryfikować PESEL
                if validate_pesel(new_pesel, student['gender']):
                    student['pesel'] = new_pesel
                else:
                    print("Niepoprawny PESEL – aktualizacja przerwana dla PESEL, powracam do starej wartości.")
            
            save_data(students)
            print("Dane studenta zostały zaktualizowane.")
            break

    if not found:
        print("Nie znaleziono studenta o podanym numerze indeksu.")
    print()

def main():
    students = load_data()

    while True:
        print("============ MENU ============")
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

        choice = input("Wybierz opcję: ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            display_students(students)
        elif choice == "3":
            search_by_last_name(students)
        elif choice == "4":
            search_by_pesel(students)
        elif choice == "5":
            sort_by_pesel(students)
        elif choice == "6":
            sort_by_last_name(students)
        elif choice == "7":
            delete_student_by_index(students)
        elif choice == "8":
            update_student_data(students)
        elif choice == "0":
            print("Koniec programu.")
            break
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.\n")

if __name__ == "__main__":
    main()
