from src.class_api import HeadHunter_API, SuperJob_API
from src.class_saver import JSONSaver
from src.class_my_list import My_List
import copy

class UserInput:
    """
    Класс для работы с пользователем
    """
    param_zero = {}

    def __init__(self):
        self.hh_api = HeadHunter_API()
        self.sj_api = SuperJob_API()
       # self.all_list = My_List()
       # self.favorite_list = My_List()
        self.param = copy.deepcopy(self.param_zero)


    def __call__(self):
        pass

    def start_communication_with_user(self):
         print("Добрый день, как Вас зовут?")
         user_name = input().title()
         print("""{user_name}, рад Вас видеть.\nХотите ознакомится со списком вакансий?\n
         Eсли да, то введите '+' либо 'enter'. Eсли нет, введите '-'.""")
         user_answer = input()
         if user_answer == "+":
            print("Приступим.")
         elif user_answer == "-":
            print('Приходите в следующий раз')
            print("\nГде вы хотите искать вакансии \n1 - HeadHunter \n2 - SuperJob \n 3 - HeadHunter и SuperJob")
            user_input = int(input())
            return user_name, user_input

    def form_list_of_vacancies(self, user_input):
        list_of_vacancies = []
         if int(user_input) == 1:
            search_word = input("Введите поисковое слово")
            hh_response = self.hh_api.get_requests()
            hh_info = self.sj_api.get_vacancies(hh_response)
            list_of_vacancies.append(hh_info)
         if int(user_input) == 2:
            search_word = input("Введите поисковое слово")
            sj_response = self.sj_api.get_requests
            sj_info = self.sj_api.get_vacancies(sj_response)
            list_vacancies = sj_info
            list_of_vacancies.append(sj_info)
         if int(user_input) == 3:
            search_word = input("Введите поисковое слово")
            hh_response = self.hh_api.get_requests()
            sj_response = self.sj_api.get_requests()
            hh_info = self.sj_api.get_vacancies(hh_response)
            sj_info = self.sj_api.get_vacancies(sj_response)
            list_of_vacancies.append(hh_info)
            list_of_vacancies.append(sj_info)
            return list_of_vacancies
        def print_vacancies(self, list_of_vacancies):
            """
            Выводит краткую информацию о вакансиях
            """
            print("Найдена следующая информация о вакансиях")
            for item in list_of_vacanсies:
                print(item)

        def sort_vacancies_by_salary(self, list_of_vacancies):
            """
            Сортирует вакансии по зарплате
            """
            print("""Хотите ли отсортировать вакансии по зарплате?
            Если да, нажмите 1. Если нет, нажмите 2""")
            user_variant = input()
            if user_variant == 1:
                filtered_data = list_of_vacancies.sort(reverse=True)
                for item in list_of_vacanсies:
                    print(item)
                print("Информация по вакансиям сохранена в файл")
                JSONSaver.save_vacancies(filtered_data)
                print("Выведим информацию по топ 5 вакансий")
                top_5_vacancies = filtered_data[:5]
                for item in list_of_vacanсies:
                    print(item)



            else:
                print("Приходите в другой раз")
















    #     if search.HeadHunter_or_SuperJob() == "HeadHunter":
    #         data = search.head_hunter()
    #         y = 0
    #         for value in data:
    #             print("-------------------------------")
    #             print(f"Вакансия по счету: {y}")
    #             print(f"Name: {value['name']}")
    #             print(f"Price: {value['price']} Руб.")
    #             print(f"Employment: {value['employment']}")
    #             print(f"Url: {value['alternate_url']}")
    #             print(f"Requirement: {value['requirement']}")
    #             print(f"Experience: {value['experience']}")
    #             y += 1
    #
    #     elif search.HeadHunter_or_SuperJob() == "SuperJob":
    #         data = search.super_job(api_key)
    #         y = 0
    #         for value in data:
    #             print("-------------------------------")
    #             print(f"Вакансия по счету: {y}")
    #             print(f"Name: {value['name']} Руб.")
    #             print(f"Price: {value['price']}")
    #             print(f"Employment: {value['employment']}")
    #             print(f"Url: {value['alternate_url']}")
    #             print(f"Requirement: {value['requirement']}")
    #             print(f"Experience: {value['experience']}")
    #             y += 1
    #
    #     def dell_Function(data, user_input):
    #         y = 0
    #         for value in data:
    #             if value == {}:
    #                 print("\nВы уже удаляли данную вакансию")
    #             elif y == user_input:
    #                 del value['name'],
    #                 del value['price'],
    #                 del value['employment'],
    #                 del value['alternate_url'],
    #                 del value['requirement'],
    #                 del value['experience']
    #                 print(f"Вакансия под номером {user_input} удалена")
    #             y += 1
    #
    #         return data
    #
    #     while True:
    #         print(
    #             "-------------------------------\nХотите удалить из списка какую-то вакансию перед добавлением в Json_File? \nEсли да то просто напишите '+' \nесли же нет '-'")
    #         user_input = input()
    #         if user_input == "-":
    #             break
    #         elif user_input == "+":
    #             print("Укажите нумерацию той вакансии которую хотите удалить")
    #             user_input = input()
    #             data = dell_Function(data, int(user_input))
    #         else:
    #             print("\nНеизвестный знак, выберите среди предложенных")
    #
    #     while True:
    #         print("Хотите сравнить вакансии между собой по зарплате? \nЕсли хотите пишите '+' , если не хотите '-' ")
    #         user_input = input()
    #         if user_input == "-":
    #             break
    #         elif user_input == "+":
    #             print("Какой язык програмирования?")
    #             user_input = input()
    #             data_HeadHunter = Search(user_input, "HeadHunter")
    #             data_SuperJob = Search(user_input, "SuperJob")
    #
    #             if data_HeadHunter.HeadHunter_or_SuperJob() == "HeadHunter":
    #                 data_hh = search.head_hunter()
    #
    #             if data_SuperJob.HeadHunter_or_SuperJob() == "SuperJob":
    #                 data_sj = search.super_job(api_key)
    #
    #             print("Какою нумерацию вакансий хотите сравнить из предложеных")
    #             print("Нажмите 'Enter' чтоб показать варианты вакансий")
    #             input()
    #             y = 0
    #             for value in data_hh:
    #                 if value == {}:
    #                     continue
    #                 print("\n-------------------------------")
    #                 print(f"Вакансия по счету: {y}")
    #                 print(f"Name: {value['name']} Руб.")
    #                 print(f"Price: {value['price']}")
    #                 print(f"Employment: {value['employment']}")
    #                 print(f"Url: {value['alternate_url']}")
    #                 print(f"Requirement: {value['requirement']}")
    #                 print(f"Experience: {value['experience']}")
    #                 y += 1
    #
    #             print("\nИз выше перечисленых вакансий выберите нужную указав цифру")
    #
    #             user_input_number = input()
    #             vacancy1 = Vacancy(data_hh[int(user_input_number)]["name"], data_hh[int(user_input_number)]["price"],
    #                                data_hh[int(user_input_number)]["alternate_url"],
    #                                data_hh[int(user_input_number)]["experience"],
    #                                data_hh[int(user_input_number)]["requirement"],
    #                                data_hh[int(user_input_number)]["employment"])
    #             vacancy2 = Vacancy(data_sj[int(user_input_number)]["name"], data_sj[int(user_input_number)]["price"],
    #                                data_sj[int(user_input_number)]["alternate_url"],
    #                                data_sj[int(user_input_number)]["experience"],
    #                                data_sj[int(user_input_number)]["requirement"],
    #                                data_sj[int(user_input_number)]["employment"])
    #
    #             print("Хотите сравнить > или <")
    #
    #             user_input = input()
    #             if user_input == ">":
    #                 is_gt = vacancy1 > vacancy2
    #                 if is_gt == False:
    #                     print("\nЗарплата на HeadHunter под данным номером меньше чем на SuperJob с таким же номером")
    #                 elif is_gt == True:
    #                     print("\nЗарплата на SuperJob под данным номером меньше чем на HeadHunter с таким же номером")
    #
    #             elif user_input == "<":
    #                 is_lt = vacancy1 < vacancy2
    #                 if is_lt == True:
    #                     print("\nЗарплата на HeadHunter под данным номером меньше чем на SuperJob с таким же номером")
    #                 elif is_lt == False:
    #                     print("\nЗарплата на SuperJob под данным номером меньше чем на HeadHunter с таким же номером")
    #
    #             else:
    #                 print("\nНеизвестный знак, выберите среди предложенных")
    #         else:
    #             print("\nНеизвестный знак, выберите среди предложенных")
    #
    #     print("\nВот и все, добавляем готовые данные в Json_File")
    #     print("Придумайте название Json_File")
    #     print("loading...")
    #     user_name_file = input()
    #
    #     if user_name_file == "":
    #         print("Oops... Вы не указали название файла, название будет стандартным")
    #         user1 = JsonFile(data, "file.json")
    #         user1.save_to_JSON()
    #         print("Все готова, Json_File должен появится, спасибо за уделенное время")
    #         return
    #
    #     user1 = JsonFile(data, user_name_file)
    #     user1.save_to_JSON()
    #     print("Все готова, Json_File должен появится, спасибо за уделенное время")
    #
    # if __name__ == '__main__':
    #     user_Function()