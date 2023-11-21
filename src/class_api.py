from abc import ABC, abstractmethod
from src.class_vacancy import Vacancy
import copy
import requests


class API(ABC):
    """
    Абстрактный класс для работы с API-сайтов с вакансиями
    """
    all_vacancies = []

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_requests(self, keyword):
        pass

    @abstractmethod
    def get_vacancies(self, response):
        pass


class HeadHunter_API(API):

    HH_API_URI = "https://api.hh.ru/vacancies"

    param_zero = {
        "text": "python",
    }

    def __init__(self):
        self.params = copy.deepcopy(self.param_zero)

    def get_requests(self, keyword):
        self.params["text"] = keyword
        response_hh = requests.get(self.HH_API_URI, self.params)
        return response_hh

    def get_vacancies(self, response_hh):
        info_hh = response_hh.json()["items"]

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
            if vacancy['snippet']['requirement']:
                requirement = vacancy['snippet']['requirement']
            else:
                requirement = None

            vacancies_hh.append(Vacancy(name, url, salary_from, salary_to, requirement))
        return vacancies_hh


class SuperJob_API(API):
    SJ_API_URI = "https://api.superjob.ru/2.0/vacancies"
    SJ_TAKEN = "v3.h.4556608.87bd54522b1c94b1a04a7a21a39251e19db2d567.d72e3df5ea2b2d980214c36977d0eaa2143378c7"

    param_zero = {
        "keyword": "python",
    }

    def __init__(self):
        self.params = copy.deepcopy(self.param_zero)

    def get_requests(self, keyword):
        self.params["keyword"] = keyword
        headers = {
            "X-Api-App-Id":
                "v3.h.4556608.87bd54522b1c94b1a04a7a21a39251e19db2d567.d72e3df5ea2b2d980214c36977d0eaa2143378c7"}

        response_sj = requests.get(self.SJ_API_URI, headers=headers, params=self.params)
        return response_sj

    def get_vacancies(self, response_sj):
        info_sj = response_sj.json()['objects']

        vacancies_sj = []
        for vacancy in info_sj:
            name = vacancy['profession']
            url = vacancy['link']
            salary_from = vacancy['payment_from']
            salary_to = vacancy['payment_to']
            if vacancy['experience']['title']:
                requirement = vacancy['experience']['title']
            else:
                requirement = None
            vacancies_sj.append(Vacancy(name, url, salary_from, salary_to, requirement))
        return vacancies_sj
