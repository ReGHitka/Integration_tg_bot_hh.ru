class VacanciesBuilder:
    def set_page(self, inbound_page): # Номер страницы
        pass

    def get_page(self):
        pass

    def set_per_page(self, inbound_per_page): # Количество элементов
        pass

    def get_per_page(self):
        pass

    def set_text(self, inbound_text): # Переданное значение ищется в полях вакансии
        pass

    def get_text(self):
        pass

    def set_search_field(self, inbound_search_field): # Область поиска
        pass

    def get_search_field(self):
        pass

    def set_experience(self, inbound_experience): # Опыт работы
        pass

    def get_experience(self):
        pass

    def set_employment(self, inbound_employment): # Тип занятости
        pass

    def get_employment(self):
        pass

    def set_schedule(self, inbound_schedule): # График работы
        pass

    def get_schedule(self):
        pass

    def set_area(self, inbound_area): # Регион
        pass

    def get_area(self):
        pass

    def set_metro(self, inbound_metro): # Ветка или станция метро
        pass

    def get_metro(self):
        pass

    def set_professional_role(self, inbound_professional_role): # Профессиональная область
        pass

    def get_professional_role(self):
        pass

    def set_currency(self, inbound_currency): # Код валюты
        pass

    def get_currency(self):
        pass

    def set_salary(self, inbound_salary): # Размер заработной платы
        pass

    def get_salary(self):
        pass

    def get_vacancies_url_attributes(self):
        pass


class VacanciesDTO(VacanciesBuilder):
    def __init__(self):
        self.per_page = None
        self.page = None
        self.salary = None
        self.currency = None
        self.professional_role = None
        self.metro = None
        self.area = None
        self.schedule = None
        self.employment = None
        self.experience = None
        self.search_field = None
        self.text = None
        self.builder = VacanciesBuilder()
        self.vacancies_url_attributes = '?host=hh.ru'

    def set_page(self, inbound_page):
        self.page = inbound_page
        self.vacancies_url_attributes += '&page={0}'.format(self.page)
        return self

    def get_page(self):
        return self.page

    def set_per_page(self, inbound_per_page):
        self.per_page = inbound_per_page
        self.vacancies_url_attributes += '&per_page={0}'.format(self.per_page)
        return self

    def get_per_page(self):
        return self.per_page

    def set_text(self, inbound_text):
        self.text = inbound_text
        self.vacancies_url_attributes += '&text={0}'.format(self.text)
        return self

    def get_text(self):
        return self.text

    def set_search_field(self, inbound_search_field): # Область поиска
        self.search_field = inbound_search_field
        self.vacancies_url_attributes += '&search_field={0}'.format(self.search_field)
        return self

    def get_search_field(self):
        return self.search_field

    def set_experience(self, inbound_experience): # Опыт работы
        self.experience = inbound_experience
        self.vacancies_url_attributes += '&experience={0}'.format(self.experience)
        return self

    def get_experience(self):
        return self.experience

    def set_employment(self, inbound_employment): # Тип занятости
        self.employment = inbound_employment
        self.vacancies_url_attributes += '&employment={0}'.format(self.employment)
        return self

    def get_employment(self):
        return self.employment

    def set_schedule(self, inbound_schedule): # График работы
        self.schedule = inbound_schedule
        self.vacancies_url_attributes += '&schedule={0}'.format(self.schedule)
        return self

    def get_schedule(self):
        return self.schedule

    def set_area(self, inbound_area): # Регион
        self.area = inbound_area
        self.vacancies_url_attributes += '&area={0}'.format(self.area)
        return self

    def get_area(self):
        return self.area

    def set_metro(self, inbound_metro): # Ветка или станция метро
        self.metro = inbound_metro
        self.vacancies_url_attributes += '&metro={0}'.format(self.metro)
        return self

    def get_metro(self):
        return self.metro

    def set_professional_role(self, inbound_professional_role): # Профессиональная область
        self.professional_role = inbound_professional_role
        self.vacancies_url_attributes += '&metro={0}'.format(self.professional_role)
        return self

    def get_professional_role(self):
        return self.professional_role

    def set_currency(self, inbound_currency): # Код валюты
        self.currency = inbound_currency
        self.vacancies_url_attributes += '&currency={0}'.format(self.currency)
        return self

    def get_currency(self):
        return self.currency

    def set_salary(self, inbound_salary): # Размер заработной платы
        self.salary = inbound_salary
        self.vacancies_url_attributes += '&salary={0}'.format(self.salary)
        return self

    def get_salary(self):
        return self.salary

    def get_vacancies_url_attributes(self):
        return self.vacancies_url_attributes

