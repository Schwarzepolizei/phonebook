import json
from typing import List, Dict


class PhonebookModel:
    """ Модель телефонного справочника """
    def __init__(self, filename: str):
        """
        Инициализация модели

        :param filename: Имя файла для сохранения телефонного справочника
        """
        self.filename: str = filename
        self.contacts: List[Dict[str, str]] = self.load_phonebook()

    def load_phonebook(self) -> List[Dict[str, str]]:
        """
        Загрузка данных справочника из файла

        :return: Список контактов из телефонного справочника
        """
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                contacts: List[Dict[str, str]] = json.load(file)
        except FileNotFoundError:
            contacts = []
        return contacts

    def save_phonebook(self) -> None:
        """ Сохранение данных справочника в файл """
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(self.contacts, file, ensure_ascii=False)

    def add_contact(self, contact: Dict[str, str]) -> None:
        """
        Добавление контакта в справочник

        :param contact: Данные нового контакта
        :return: None
        """
        self.contacts.append(contact)
        self.save_phonebook()
