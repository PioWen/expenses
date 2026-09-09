from pathlib import Path
file_path = Path(r"D:\Python\pliki\Projekt\expenses.txt")

def add_expense():
    #dodawanie wydatku
    name = input("nazwa wydatku:")
    category = input("kategoria wydatku:")
    cost = float(input("kwota wydatku:"))

    with open (file_path, "a") as file:
        file.write (f"{name};{category};{cost}\n")

def show_expenses():
    #wyświetlanie wydatków
    if file_path.exists():
        with open (file_path, "r") as file:
            for lines in file:
                expense = lines.split(";")
                result = (f"Nazwa: {expense[0]} | Kategoria: {expense[1]} | Kwota: {expense[2].strip()}")
                print (result)
    else:
        print("Brak zapisanych wydatków")

def show_summary():
    #wyświetlanie podsumowania
    total_cost = 0
    expense_count = 0
    average_cost = 0
    categories = {}
    if file_path.exists():
        with open (file_path, "r") as file:
            for lines in file:
                expense_count += 1
                expense = lines.split(";")
                price = float(expense[2])
                total_cost += price
                category = expense[1]
                if category not in categories:
                    categories [category] = 0
                categories [category] += price
            if expense_count > 0:
                average_cost = total_cost/expense_count
            print (f"Liczba wydatków: {expense_count}\nŁączna suma: {total_cost:.2f}\nŚredni wydatek: {average_cost:.2f}\n")
        for category, total in categories.items():
            print(f"{category}: {total:.2f}")
    else:
        print("Brak zapisanych wydatków")

while True:
    menu_option = int(input(
        "1 - Dodaj wydatek\n"
        "2 - Pokaż wydatki\n"
        "3 - Pokaż podsumowanie\n"
        "4 - Zakończ\n"
    ))
    if menu_option == 1:
        add_expense()
    elif menu_option == 2:
        show_expenses()
    elif menu_option == 3:
        show_summary()
    elif menu_option == 4:
        break
    else:
        print("Nieprawidłowa opcja")
