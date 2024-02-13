from typing import List, Dict, Union


class PhonebookView:
    """ Представление телефонного справочника """
    @staticmethod
    def display_contacts(contacts: List[Dict[str, Union[str, int]]], page_num: int, page_size: int) -> None:
        """
        Отображает контакты на текущей странице справочника

        :param contacts: Список контактов
        :param page_num: Номер текущей страницы
        :param page_size: Размер страницы
        :return: None
        """
        if not contacts:
            print("Телефонный справочник пуст")
            return

        total_pages: int = (len(contacts) - 1) // page_size + 1
        if page_num < 1 or page_num > total_pages:
            print(f"Страницы {page_num} не существует.")
            return

        start_index: int = (page_num - 1) * page_size
        end_index: int = min(start_index + page_size, len(contacts))

        print(f"Страница {page_num}/{total_pages}:")
        for i in range(start_index, end_index):
            contact: Dict[str, Union[str, int]] = contacts[i]
            print(f"{i + 1}. {contact['Фамилия']} {contact['Имя']} {contact['Отчество']}, "
                  f"{contact['Организация']}, "
                  f"рабочий: {contact['Рабочий телефон']}, "
                  f"личный: {contact['Личный телефон']}")

        if total_pages > 1:
            next_page: str = input("\nНажмите 'n' для следующей страницы, 'p' для предыдущей или 'Enter' для выхода: ")
            if next_page.lower() == 'n' and page_num < total_pages:
                PhonebookView.display_contacts(contacts, page_num + 1, page_size)
            elif next_page.lower() == 'p' and page_num > 1:
                PhonebookView.display_contacts(contacts, page_num - 1, page_size)

    @staticmethod
    def get_contact_info() -> Dict[str, str]:
        """
        Получает информацию о новом контакте

        :return: Словарь с информацией о новом контакте
        """
        last_name: str = input("Введите фамилию: ")
        first_name: str = input("Введите имя: ")
        middle_name: str = input("Введите отчество: ")

        organization: str = input("Введите название организации: ")

        while True:
            work_phone: str = input("Введите рабочий телефон: ")
            if not work_phone.isdigit():
                print("Рабочий телефон должен содержать только цифры.")
                continue
            break

        while True:
            personal_phone: str = input("Введите личный телефон (сотовый) в формате +79999999999: ")
            if not personal_phone.startswith('+7') or not personal_phone[1:].isdigit():
                print("Личный телефон (сотовый) должен начинаться с '+7' и содержать только цифры.")
                continue
            break

        return {
            "Фамилия": last_name,
            "Имя": first_name,
            "Отчество": middle_name,
            "Организация": organization,
            "Рабочий телефон": work_phone,
            "Личный телефон": personal_phone
        }
