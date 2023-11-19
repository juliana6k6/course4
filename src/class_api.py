from abc import ABC, abstractmethod
from src.class_vacancy import Vacancy
import copy
import requests
import json


class API(ABC):
    """
    Абстрактный класс для работы с API-сайтов c вакансиями
    """
    all_vacancies = []

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_requests(self):
        pass

    @abstractmethod
    def get_vacancies(self):
        pass


    # @abstractmethod
    # def change_date(self):
    #     pass

    # @abstractmethod
    # def add_word(self):
    #     pass
    #
    # @abstractmethod
    # def add_area(self):
    #     pass
    #
    # @abstractmethod
    # def load_all_areas(self):
    #     pass


class HeadHunter_API(API):

    HH_API_URI = "https://api.hh.ru/vacancies"
    # HH_API_URI_AREAS = "https://api.hh.ru/areas"

    param_zero = {
        "text": "python",
    }
    # params = {
    #     "text": text.lower(),
    #     "page": 5,
    #     "per_page": 100
    # }
    def __init__(self):
        self.params = copy.deepcopy(self.param_zero)

    def get_requests(self):
        response_hh = requests.get(self.HH_API_URI, self.params)
        return response_hh

    def get_vacancies(self, response_hh):
        info_hh = json.loads(response_hh.text)["items"]

        vacancies_hh = []
        for vacancy in info_hh:
            name = vacancy['name']
            url = vacancy['alternate_url']
            if vacancy['salary']:
                salary_from = vacancy['salary']['from']
                salary_to = vacancy['salary']['to']
            else:
                salary_from = None
                salary_to = None
            vacancies_hh.append(Vacancy(name, url, salary_from, salary_to))
        return vacancies_hh

    # def change_date(self):
    #     pass
    #
    # def add_word(self):
    #     pass
    #
    # def add_area(self):
    #     pass
    #
    # def load_all_areas(self):
    #     response = requests.get(self.HH_API_URI_AREAS)
    #     response_data = json.loads(response.text)
    #     return response_data["objects"]


class SuperJob_API(API):
    SJ_API_URI = "https://api.superjob.ru/2.0/vacancies"
    # SJ_API_URI_AREAS = "https://api.superjob.ru/2.0/towns"
    SJ_TAKEN = "v3.h.4556608.87bd54522b1c94b1a04a7a21a39251e19db2d567.d72e3df5ea2b2d980214c36977d0eaa2143378c7"

    param_zero = {
        "keyword": "python",
    }

    def __init__(self):
        self.params = copy.deepcopy(self.param_zero)

    def get_requests(self):
        headers = {
            "X-Api-App-Id":
                "v3.h.4556608.87bd54522b1c94b1a04a7a21a39251e19db2d567.d72e3df5ea2b2d980214c36977d0eaa2143378c7"}
        # params = {
        #     "keyword": text.lower(),
        #     "page": 5,
        #     "count": 100
        # }

        response_sj = requests.get(self.SJ_API_URI, headers=headers, params=self.params)
        return response_sj

    def get_vacancies(self, response_sj):
        info_sj = json.loads(response_sj.text)['objects']

        vacancies_sj = []
        for vacancy in info_sj:
            name = vacancy['profession']
            url = vacancy['link']
            salary_from = vacancy['payment_from']
            salary_to = vacancy['payment_to']
            vacancies_sj.append(Vacancy(name, url, salary_from, salary_to))
        return vacancies_sj
    # def change_date(self):
    #     pass
    #
    # def add_word(self):
    #     pass
    #
    # def add_area(self):
    #     pass
    #
    # def load_all_areas(self):
    #     pass
