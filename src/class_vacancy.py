
class Vacancy:
    """
    Для работы с вакансиями
    """

    def __init__(self, title, url, salary_from, salary_to, requirement):
        self.title = title
        self.url = url
        self.salary_from = salary_from if salary_from else 0
        self.salary_to = salary_to if salary_to else 0
        self.requirement = requirement

        self.salary = (self.salary_from + self.salary_to)/2

    def __str__(self):
        """Возвращаем метод str для отображения"""
        return (f"{self.__class__.__name__}('Професия: {self.title}', 'Ссылка: {self.url}',"
                f" 'Зарплата: {self.salary}', 'Опыт: {self.requirement}')")


    def __repr__(self):
        return f""" ------------
    Название: {self.title},
    Ссылка: {self.url},
    Минимальная зарплата: {self.salary_from},
    Максимальная зарплата: {self.salary_to},
    Опыт: {self.requirement}
    """
#     def __init__(self, title: str, url: str, salary_from: int, salary_to: int, employer, requirements: str, area: str,
#                  data_published: str, currency: str):
#         self.title = title
#         if not isinstance(self.title, str):
#             raise TypeError("Название вакансии должно быть типа 'str'")
#         self.url = url
#         if self.url[:8] != 'https://':
#             raise UrlError("Ссылка должна начинаться с https://")
#         # self.salary_to = salary_to
#         # if self.salary_to is None:
#         #     raise AttributeError('Поле не может быть пустым')
#         self.salary_from = salary_from
#         if self.salary_from is None:
#             raise AttributeError('Поле не может быть пустым')
#         self.employer = employer
#         if self.employer is None:
#             raise AttributeError('Поле не может быть пустым')
#         self.requirements = requirements
#         # if self.requirement is None:
#         #     raise AttributeError('Поле не может быть пустым')
#         self.area = area
#         self.data_published = data_published
#         self.currency = currency
#
#     def __str__(self):
#         return f'{self.title}({self.url})'
#
#     def form_vacancy(self):
#         return {
#             'Профессия': self.title,
#             'Ссылка': self.url,
#             'З/п от': self.salary_from,
#             'З/п до': self.salary_to,
#             'Работодатель': self.employer,
#             'Требования': self.requirements
#
#         }
#
#     def __ge__(self, other):
#         return (self.salary_from + self.salary_to) / 2 >= (other.salary_from + other.salary_to) / 2
#
#     def __le__(self, other):
#         return (self.salary_from + self.salary_to) / 2 >= (other.salary_from + other.salary_to) / 2
#
#     def __eq__(self, other):
#         return (self.salary_from + self.salary_to) / 2 == (other.salary_from + other.salary_to) / 2
#
#     def __str__(self):
#         return f'Название вакансии - {self.name}\n' \
#                f'Ссылка - {self.url}\n' \
#                f'З/п до {self.salary} RUR\n' \
#                f'Требования - {self.requirement}\n'
#

    def __eq__(self, other):
        return self.salary == other.salary

    def __ne__(self, other):
        return self.salary != other.salary

    def __lt__(self, other):
        return self.salary < other.salary

    def __le__(self, other):
        return self.salary <= other.salary

    def __gt__(self, other):
        return self.salary > other.salary

    def __ge__(self, other):
        return self.salary >= other.salary

    def to_dict_vacancy(self):
        """
        Функция представляющая вакансию в виде словаря
        """
        return {
            "title": self.title,
            "url": self.url,
            "salary_from": self.salary_from,
            "salary_to": self.salary_to,
            "requirements": self.requirement
        }




#
#     @classmethod
#     def get_from_headhunter(cls, vacancy_info_hh: dict):
#         """
#         Функция для инициализации вакансий с платформы HeadHunter
#         """
#         vacancies_list = []
#         for item in vacancy_info_hh:
#             title = item["name"]
#             data_published = item["published_at"]
#             salary_from = item["salary"]["from"]
#             salary_to = item["salary"]["to"]
#             currency = item["salary"]["currency"]
#             area = item["area"]["name"]
#             url = item["alternate_url"]
#             employer = item["employer"]["name"]
#             requirement = item["snippet"]["requirement"]
#             vacancy = Vacancy(title, url, salary_from, salary_to, employer, requirement, area, data_published, currency)
#             vacancies_list.append(vacancy)
#             print(vacancies_list)
#
# #
# # def get_from_superjob(vacancies: dict_vacancies):
# #     """
# #     Функция для инициализации вакансий с платформы SuperJob
# #     """
# #     vacancies_list = []
# #     for item in dict_vacancies:
# #         if item['candidat']:
# #             if item['payment_to']:
# #                 if item['currency'] == 'rub':
# #                     vacancy = Vacancy(item['profession'], item['link'], item['payment_to'],
# #                                       item['candidat'])
# #                     vacancies_list.append(vacancy)
# #     return vacancies_list
# #
# #   result = {
# #             "id": cls.check_for_availability(vacancy_info_hh,"id"),
# #             "website": 'HeadHunter',
# #             "type": cls.check_for_availability(vacancy_info_hh,"type","name"),
# #             "name": cls.check_for_availability(vacancy_info_hh,"name"),
# #             "data_published": datetime.datetime.strptime(vacancy_info_hh["published_at"],
# #                                                          '%Y-%m-%dT%H:%M:%S+%f').timestamp(),
# #             "salary_from": cls.check_for_availability(vacancy_info_hh, "salary", "from"),
# #             "salary_to": cls.check_for_availability(vacancy_info_hh, "salary", "to"),
# #             "currency": cls.check_for_availability(vacancy_info_hh, "salary", "currency"),
# #             "area": cls.check_for_availability(vacancy_info_hh,"area", "name"),
# #             "url": cls.check_for_availability(vacancy_info_hh,"alternate_url"),
# #             "employer": cls.check_for_availability(vacancy_info_hh,"employer","name"),
# #             "employer_url": cls.check_for_availability(vacancy_info_hh,"employer","alternate_url"),
# #             "requirement": cls.check_for_availability(vacancy_info_hh,"snippet","requirement"),
# #             "experience": cls.check_for_availability(vacancy_info_hh,"experience","name"),
# #             "employment": cls.check_for_availability(vacancy_info_hh,"employment","name")