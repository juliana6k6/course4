from src.class_api import HeadHunter_API, SuperJob_API
from src.class_saver import JSONSaver
import copy


class UserInput:
    """
    Класс для работы с пользователем
    """
    param_zero = {}

    def __init__(self):
        self.hh_api = HeadHunter_API()
        self.sj_api = SuperJob_API()
        self.param = copy.deepcopy(self.param_zero)

    def __call__(self):
        pass

    @staticmethod
    def start_communication_with_user():
        print("Добрый день, как Вас зовут?")
        user_name = input().title()
        print(f"{user_name}, рад Вас видеть.\nХотите ознакомится со списком вакансий?\n")
        print(f"Eсли да, то введите '+' либо 'enter'. Eсли нет, введите '-'.")
        user_answer = input()
        if user_answer == "+" or user_answer == "":
            print("Приступим.")
            print("\nГде вы хотите искать вакансии \n1 - HeadHunter \n2 - SuperJob \n3 - HeadHunter и SuperJob")
            user_input = int(input())
            return user_input
        elif user_answer == "-":
            print('Приходите в следующий раз')
            return None

    def form_list_of_vacancies(self, user_input):
        list_of_vacancies = []
        if int(user_input) == 1:
            search_word = input("Введите поисковое слово\n")
            hh_response = self.hh_api.get_requests(search_word)
            hh_info = self.hh_api.get_vacancies(hh_response)
            list_of_vacancies.extend(hh_info)
        if int(user_input) == 2:
            search_word = input("Введите поисковое слово\n")
            sj_response = self.sj_api.get_requests(search_word)
            sj_info = self.sj_api.get_vacancies(sj_response)
            list_of_vacancies.extend(sj_info)
        if int(user_input) == 3:
            search_word = input("Введите поисковое слово\n")
            hh_response = self.hh_api.get_requests(search_word)
            sj_response = self.sj_api.get_requests(search_word)
            hh_info = self.hh_api.get_vacancies(hh_response)
            sj_info = self.sj_api.get_vacancies(sj_response)
            list_of_vacancies.extend(hh_info)
            list_of_vacancies.extend(sj_info)
        return list_of_vacancies

    @staticmethod
    def print_vacancies(list_of_vacancies):
        """
        Выводит краткую информацию о вакансиях
        """
        number = int(input("Ведите количество вакансий, которое хотите посмотреть\n"))
        print("Найдена следующая информация о вакансиях")
        vac_list = list_of_vacancies[:number]
        for item in vac_list:
            print(item)

    @staticmethod
    def sort_vacancies_by_salary(list_of_vacancies):
        """
        Сортирует вакансии по зарплате
        """
        print("""Хотите ли отсортировать вакансии по зарплате?
            Если да, нажмите 1. Если нет, нажмите 2""")
        user_variant = int(input())
        if user_variant == 1:
            list_of_vacancies.sort(reverse=True)
            for item in list_of_vacancies[:7]:
                print(item)
            print("Информация по вакансиям сохранена в файл")
            json_saver = JSONSaver()
            list_dict_vacancies = [vacancy.to_dict_vacancy() for vacancy in list_of_vacancies]
            json_saver.save_vacancies(list_dict_vacancies)
            print("Выведим информацию по топ 5 вакансий")
            top_5_vacancies = list_of_vacancies[:5]
            for item in top_5_vacancies:
                print(item)
        else:
            print("Приходите в другой раз")
