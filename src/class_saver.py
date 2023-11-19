from abc import ABC, abstractmethod
import json


class Saver(ABC):
    class Saver(ABC):
        """Абстрактный класс для редактирования и обработки списка вакансий"""

        @abstractmethod
        def save_vacancies(self):
            pass

        def read_vacancies(self):
            pass

    class JSONSaver(Vacancies, Saver):
        """Класс для обработки списка вакансий в JSON формате"""

        def save_vacancies(self):
            """
            Сохраняет список вакансий в формате JSON
            """
            with open('vacancies.json', 'w', encoding="utf-8") as file:
                json.dump(cls.all_vacancies, file, indent=4)

    ???    def read_vacancies(self):
            with open('vacancies.json', 'r') as file:
                list_dict = json.load(file)
            self.__all_vacancies = []
            for i in list_dict:
                self.all_vacancies.append(Vacancy.from_dict(i))




class TXT_Saver(Vacancies, Saver):
    def save_vacancies(self):
        """
        Сохраняет список вакансий в формате TXT
        """
        with open('vacancies.txt', 'w', encoding="utf-8") as file:
            for i in cls.all_vacancies:
                file.write(f"{i['платформа']}\n"
                           f"{i['должность']}\n"
                           f"{i['зарплата_от']}\n"
                           f"{i['описание']}\n"
                           f"{i['ссылка']}\n\n")


class CSV_Saver(Vacancies, Saver):

    def save_vacancies(self):
        """
        Сохраняет список вакансий в формате CSV
        """
        with open('vacancies.scv', 'w', encoding="utf-8") as file:
            names = ['платформа', 'должность', 'зарплата_от', 'описание', 'ссылка']
            filewriter = csv.DictWriter(file, delimiter=",",
                                         lineterminator="\r", fieldnames=names)
            file_writer.writeheader()
            for i in cls.all_vacansis:
                file_writer.writerow(i)