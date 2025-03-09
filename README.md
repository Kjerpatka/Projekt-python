# Projekt-python
Projekt: akademicka baza danych studentów

Celem zadania jest stworzenie od podstaw aplikacji, która będzie prostą akademicką "bazą danych", przechowującą informacje o studentach. Program powinien umożliwiać wykonywanie podstawowych operacji na danych, takich jak dodawanie, wyświetlanie, sortowanie, aktualizowanie czy usuwanie rekordów.

Minimalne wymagania funkcjonalne:
Przechowywanie informacji o studentach
Każdy student powinien mieć następujące dane (wymyślone na użytek zadania):
• Imię
• Nazwisko
• Adres zamieszkania
• Numer indeksu
• Numer PESEL
• Płeć

Funkcjonalność aplikacji

Aplikacja musi posiadać następujące funkcjonalności:
• Dodawanie nowych studentów do bazy danych
• Wyświetlanie wszystkich studentów
• Wyszukiwanie studentów:
o według nazwiska
o według numeru PESEL
• Sortowanie bazy danych:
o według numeru PESEL
o według nazwiska
• Usuwanie studentów według numeru indeksu
• Aktualizacja informacji o studentach
• Walidacja poprawności numeru PESEL obejmująca:
o Sprawdzenie sumy kontrolnej
o Weryfikację daty urodzenia zakodowanej w numerze PESEL
o Weryfikację płci zakodowanej w numerze PESEL z wprowadzoną płcią studenta

Przechowywanie danych:
Program powinien umożliwiać zapis bazy danych do pliku oraz wczytywanie danych z pliku przy ponownym uruchomieniu aplikacji. Zaleca się użycie formatu JSON ze względu na jego czytelność i łatwość obsługi w Pythonie.

Obsługa błędów
Należy zadbać o odpowiednią obsługę błędów i wyjątków, zwłaszcza podczas:
• Wprowadzania danych przez użytkownika.
• Zapisu i odczytu plików.
• Walidacji numeru PESEL.

Interfejs użytkownika
Aplikacja może być zrealizowana jako (do wyboru):
• Aplikacja konsolowa (tekstowa).
• Aplikacja z graficznym interfejsem użytkownika (GUI).

Wymagania dodatkowe
Modularność i rozszerzalność:
Program powinien być zorganizowany w taki sposób, aby jego rozwój w przyszłości był prosty.
Przykładami rozszerzeń mogą być:
• Dodanie dodatkowych danych dla studentów, takich jak kierunek studiów, oceny lub
zapisane przedmioty.
• Dodanie innych operacji na danych, np. aktualizacja informacji o studentach.

Dobra praktyka programistyczna
Należy stosować zasady modularności i enkapsulacji. Proszę zadbać o to, aby kod był dobrze zorganizowany, czytelny i łatwy do utrzymania. Na przykład:
• Każda funkcjonalność (dodawanie, sortowanie, wyszukiwanie itp.) powinna być umieszczona w osobnych modułach/funkcjach/metodach.
• Unikanie pisania kodu, który trudno będzie rozszerzyć o nowe funkcje.
• Należy zadbać o odpowiednią strukturę danych, aby w przyszłości łatwo było ją
rozbudowywać.

Wskazówki techniczne
Kilka wskazówek i zasad:
• Walidacja PESEL - numer PESEL (wymyślony na użytek zadania – przykładowy generator online: https://pesel.cstudios.pl/o-generatorze/generator-on-line) ma ustaloną długość (11 cyfr) oraz określone zasady wyliczania sumy kontrolnej. Należy wykorzystać algorytm do weryfikacji poprawności numeru PESEL i zaimplementować go w programie.

• Pliki do przechowywania bazy danych możesz wykorzystać prosty format tekstowy (np. pliki CSV, JSON, XML). Proszę zweryfikować czy wczytywanie i zapis danych są poprawnie obsługiwane.
• Sortowanie i wyszukiwanie, można użyć wbudowanych funkcji sortowania i wyszukiwania lub zaimplementować własne algorytmy.
• Można korzystać z wbudowanych modułów, takich jak json, datetime czy re (do wyrażeń regularnych).

Ocena projektu
Projekt będzie oceniany na podstawie następujących kryteriów:

• Poprawność działania aplikacji (maks. 40 punktów)
o Czy aplikacja spełnia wszystkie wymagania funkcjonalne?
o Czy walidacja numeru PESEL jest poprawnie zaimplementowana?
• Organizacja kodu (maks. 20 punktów)
o Czy kod jest modularny i dobrze zaprojektowany?
o Czy struktura danych jest odpowiednio zaprojektowana?
• Jakość i czytelność kodu (maks. 20 punktów)
o Czy kod jest czytelny i zgodny z konwencjami PEP 8?
o Czy są dodane komentarze i docstringi?
• Obsługa błędów i wyjątków (maks. 20 punktów)
o Czy program poprawnie obsługuje błędy podczas wprowadzania danych?
o Czy są zaimplementowane mechanizmy obsługi wyjątków?
• Dodatkowe funkcjonalności (maks. 10 punktów)
o Za implementację funkcji wykraczających poza minimalne wymagania, np.
dodatkowe pola, funkcje, testy jednostkowe czy użycie bazy danych.
