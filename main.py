from student_management.repository.student_repository import BazaStudentow
from student_management.ui.console_ui import InterfejsKonsoli

def main():
    """Główny punkt wejścia aplikacji."""
    baza = BazaStudentow()
    ui = InterfejsKonsoli(baza)
    ui.uruchom()

if __name__ == "__main__":
    main()
