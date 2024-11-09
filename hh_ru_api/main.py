from hh_ru_api.model.dto.vacancies_dto import VacanciesDTO
from hh_ru_api.processes import VacanciesProcess

vacancies_dto = VacanciesDTO().set_text("Разработчик Java").set_salary(100000).set_area("40")

json_data = VacanciesProcess(vacancies_dto).get_vacancies()

print(json_data)