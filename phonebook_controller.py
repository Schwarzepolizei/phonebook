from typing import List, Dict
from phonebook_model import PhonebookModel
from phonebook_view import  PhonebookView


class PhonebookController:
    """ Контроллер для управления телефонным справочником """
    def __init__(self, model: PhonebookModel, view: PhonebookView):
        """
        Инициализация контроллера

        :param model: Модель телефонного справочника
        :param view: Представление телефонного справочника
        """
        self.model = model
        self.view = view
        self.page_size: int = 10
        self.page_num: int = 1

    def display_contacts(self) -> None:
        """ Отображает контакты на текущей странице """
        contacts: List[Dict[str, str]] = self.model.contacts
        self.view.display_contacts(contacts, self.page_num, self.page_size)

    def add_contact(self) -> None:
        """ Добавляет новый контакт в справочник """
        contact: Dict[str, str] = self.view.get_contact_info()
        self.model.add_contact(contact)

    def edit_contact(self) -> None:
        """ Редактирует контакт в справочнике """
        contacts: List[Dict[str, str]] = self.model.contacts
        self.view.display_contacts(contacts, self.page_num, self.page_size)
        contact_num: int = int(input("Введите номер записи для изменения: "))
        if 1 <= contact_num <= len(contacts):
            contact: Dict[str, str] = self.view.get_contact_info()
            contacts[contact_num - 1] = contact
            self.model.save_phonebook()
        else:
            print("Неверный номер записи.")

    def search_contacts(self):
        """ Поиск контакта """
        search_term: str = input("Введите фамилию, организацию, рабочий или личный номер телефона для поиска: ")
        search_results: List[Dict[str, str]] = []
        for contact in self.model.contacts:
            if (search_term.lower() in contact['Фамилия'].lower() or
                    search_term.lower() in contact['Организация'].lower() or
                    search_term in contact['Рабочий телефон'] or
                    search_term in contact['Личный телефон']):
                search_results.append(contact)
        if search_results:
            self.view.display_contacts(search_results, 1, len(search_results))
        else:
            print("Ничего не найдено.")
