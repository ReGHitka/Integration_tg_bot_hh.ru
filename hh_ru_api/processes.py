import json

import requests

from hh_ru_api.model.decoder.metro_decoder import Metro, AllMetro
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

        if request.status_code == 200 and data is not None:
            return Vacancies.from_dict(json.loads(data))
        else:
            return None


class MetroProcess:
    metro_url = 'https://api.hh.ru/metro'

    def get_all_metros(self):
        request = requests.get(self.metro_url)

        data = request.content.decode()
        request.close()

        if request.status_code == 200 and data is not None:
            return AllMetro.from_dict(json.loads(data))
        else:
            return None

    def equalsTo(self, user_metro, user_city):
        all_metros : AllMetro = self.get_all_metros()

        if all_metros is not None:
            for city in all_metros.allMetro:
                if city.id == user_city:
                    for lines in city.lines:
                        for station in lines.stations:
                            if station.name == user_metro:
                                return station.id

        return "Метро " + user_metro + " не найдено"