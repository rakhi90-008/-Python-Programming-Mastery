from file_manager import load_expenses
from menu import show_menu

def main():
    expenses = load_expenses()
    show_menu()

if __name__ == "__main__":
    main()
