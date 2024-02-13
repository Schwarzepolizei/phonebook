from phonebook_model import PhonebookModel
from phonebook_view import PhonebookView
from phonebook_controller import PhonebookController


def main() -> None:
    """
    Основная функция программы, инициализирующая модель, представление и контроллер
    и обеспечивающая основной цикл взаимодействия с пользователем

    :return: None
    """
    model: PhonebookModel = PhonebookModel("phonebook.json")
    view: PhonebookView = PhonebookView()
    controller: PhonebookController = PhonebookController(model, view)

    while True:
        print("\nВыберите действие:")
        print("1. Вывести все контакты")
        print("2. Добавить новый контакт")
        print("3. Изменить запись")
        print("4. Поиск")
        print("5. Выйти")

        choice: str = input("Ваш выбор: ")

        if choice == "1":
            controller.display_contacts()
            if controller.page_num == 0:
                continue
        elif choice == "2":
            controller.add_contact()
        elif choice == "3":
            controller.edit_contact()
        elif choice == "4":
            controller.search_contacts()
        elif choice == "5":
            print("До свидания!")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
