from abc import ABC, abstractmethod
import json


class Saver(ABC):
    """Абстрактный класс для редактирования и обработки списка вакансий"""

    @abstractmethod
    def save_vacancies(self, information):
        pass


class JSONSaver(Saver):
    """Класс для обработки списка вакансий в JSON формате"""

    def save_vacancies(self, vacant_information):
        """
        Сохраняет список вакансий в формате JSON
        """
        with open('vacancies.json', 'w', encoding="utf-8") as file:
            json.dump(vacant_information, file, indent=4)
