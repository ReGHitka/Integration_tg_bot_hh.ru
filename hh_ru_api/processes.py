import json

import requests

from hh_ru_api.model.decoder.vacancies_decoder import Vacancies
from hh_ru_api.model.dto.vacancies_dto import VacanciesDTO

class VacanciesProcess:
    vacancies_url = 'https://api.hh.ru/vacancies'

    def __init__(self, vacancies_dto : VacanciesDTO):
        self.vacancies_dto = vacancies_dto

    def get_vacancies(self):
        self.vacancies_url += self.vacancies_dto.get_vacancies_url_attributes()

        request = requests.get(self.vacancies_url)

        data = request.content.decode()
        request.close()

        return Vacancies.from_dict(json.loads(data))