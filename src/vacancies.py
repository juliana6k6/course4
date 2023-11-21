

class Vacancies:
    """Класс для хранения и обработки вакансий"""

    def __init__(self):
        self.all_vacancies = []

    def add_vacancies(self, new_vacancies):
        self.all_vacancies += new_vacancies

    def delete_vacancies(self, old_vacancies):
        for i in old_vacancies:
            self.all_vacancies.remove(i)

    def sort_vacancies_by_salary(self):
        self.all_vacancies.sort(reverse=True)

    def to_list_dict_vacancies(self):
        list_vac = []
        for vac in self.all_vacancies:
            list_vac.append(vac.to_dict_vacancy())
        return list_vac
