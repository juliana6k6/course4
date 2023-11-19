from src.class_userinput import UserInput
from src.class_api import API, HeadHunter_API, SuperJob_API
from src.class_vacancy import Vacancy
from pprint import pprint


if __name__ == '__main__':
    # userinput = UserInput()
    # userinput()
    # hh_api = HeadHunter_API()
    # data_hh = hh_api.get_requests()
    # vacancies_hh = hh_api.get_vacancies(data_hh)
    # pprint(vacancies_hh)



    # pprint(data, indent=2)
    # print(len(data))
    # areas = hh_api.load_all_areas()
    # pprint(areas, indent=2)
    sj_api = SuperJob_API()
    data_sj = sj_api.get_requests()
    vacancies_sj = sj_api.get_vacancies(data_sj)
    pprint(vacancies_sj)
    # pprint(data, indent=2)
    # print(len(data))



