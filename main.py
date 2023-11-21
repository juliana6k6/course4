from src.class_userinput import UserInput



if __name__ == '__main__':
    userinput = UserInput()
    number = userinput.start_communication_with_user()
    if number:
        vacancies = userinput.form_list_of_vacancies(number)
        userinput.print_vacancies(vacancies)
        userinput.sort_vacancies_by_salary(vacancies)








