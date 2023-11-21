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
        return (f"{self.__class__.__name__}('Профессия: {self.title}', 'Ссылка: {self.url}',"
                f" 'Зарплата: {self.salary}', 'Опыт: {self.requirement}')")

    def __repr__(self):
        return f""" ------------
    Название: {self.title},
    Ссылка: {self.url},
    Минимальная зарплата: {self.salary_from},
    Максимальная зарплата: {self.salary_to},
    Опыт: {self.requirement}
    """

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
