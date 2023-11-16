from abc import ABC, abstractmethod
import copy
import requests
import json


class API(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_vacancies(self):
        pass


    @abstractmethod
    def change_date(self):
        pass

    @abstractmethod
    def add_word(self):
        pass

    @abstractmethod
    def add_area(self):
        pass

    @abstractmethod
    def load_all_areas(self):
        pass


class HeadHunter_API(API):

    HH_API_URI = "https://api.hh.ru/vacancies"
    HH_API_URI_AREAS = "https://api.hh.ru/areas"

    param_zero = {
        "text": "python",
        "per_page": 100,
        "area": 67,
        "data": 14
    }

    def __init__(self):
        self.params = copy.deepcopy(self.param_zero)

    def get_vacancies(self):
        response = requests.get(self.HH_API_URI, self.params)
        response_data = json.loads(response.text)
        return response_data["items"]


    def change_date(self):
        pass


    def add_word(self):
        pass


    def add_area(self):
        pass


    def load_all_areas(self):
        response = requests.get(self.HH_API_URI_AREAS)
        response_data = json.loads(response.text)
        return response_data

class SuperJob_API(API):

    SJ_API_URI = "https://api.superjob.ru/2.0/vacancies"
    SJ_API_URI_AREAS = "https://api.superjob.ru/2.0/towns"
    SJ_TAKEN = ""

    param_zero = {
        "keyword": "python",
        "count": 100,
        "town": 67,
        "date_published_from": 14
    def __init__(self):
        self.param = copy.deepcopy(self.param_zero)

    def get_vacancies(self):
        headers = {
            "X-Api-App-Id": self.SJ_TAKEN}
        response = requests.get(self.SJ_API_URI, headers =headers, params =self.param)
        response_data = json.loads(response.text)
        return response_data
    def change_date(self):
        pass


    def add_word(self):
        pass


    def add_area(self):
        pass


    def load_all_areas(self):
        pass