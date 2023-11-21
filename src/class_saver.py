from abc import ABC, abstractmethod
from src.vacancies import Vacancies
from src.class_vacancy import Vacancy
import json
import os


class Saver(ABC):
    class Saver(ABC):
        """Абстрактный класс для редактирования и обработки списка вакансий"""

        @abstractmethod
        def save_vacancies(self):
            pass

        @abstractmethod
        def read_vacancies(self):
            pass

        @abstractmethod
        def delete_file(self):
            pass


class JSONSaver(Vacancies, Saver):
    """Класс для обработки списка вакансий в JSON формате"""

    def save_vacancies(self, vacant_information):
        """
        Сохраняет список вакансий в формате JSON
        """
        with open('vacancies.json', 'w', encoding="utf-8") as file:
            json.dump(vacant_information, file, indent=4)

    def read_vacancies(self):
        with open('vacancies.json', 'r') as file:
            list_vac = json.load(file)
        self.all_vacancies = []
        for vac in list_vac:
            self.all_vacancies.append(Vacancy.to_dict_vacancy(vac))

    def delete_file(self):
        """Удаляет файл"""
        if os.path.exists('vacancies.json'):
            os.remove('vacancies.json')




