from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from hh_ru_api.model.dto.vacancies_dto import VacanciesDTO
from hh_ru_api.processes import VacanciesProcess, MetroProcess
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
import keyboards

router = Router()

class Vac(StatesGroup):
    vac_name = State()
    vac_metro = State()
    vac_salary = State()


@router.message(CommandStart())
async def start_handler(msg: Message):
    await msg.answer("Привет!", reply_markup=keyboards.main_menu)

@router.message(F.text == 'Вернуться в главное меню')
async def handler_back(msg: Message):
    await msg.answer("Главное меню", reply_markup=keyboards.main_menu)

@router.message(F.text == 'Поиск вакансий')
async def vac_name(message : Message, state: FSMContext):
    await state.set_state(Vac.vac_name)
    await message.answer('Выбери или напиши название вакансии', reply_markup=keyboards.name_vac)

@router.message(Vac.vac_name)
async def vac_metro(message : Message, state: FSMContext):
    await state.update_data(vac_name=message.text)
    await state.set_state(Vac.vac_metro)
    await message.answer('Выберите или введите станцию метро', reply_markup=keyboards.metro)

@router.message(Vac.vac_metro)
async def vac_salary(message : Message, state: FSMContext):
    await state.update_data(vac_metro=message.text)
    await state.set_state(Vac.vac_salary)
    await message.answer('Выберите или напишите желаемую зарплату', reply_markup=keyboards.salary)

@router.message(Vac.vac_salary)
async def vac_stop(message : Message, state: FSMContext):
    await state.update_data(vac_salary=message.text)
    data = await state.get_data()
    user_city = "1"
    id_metro = MetroProcess().equalsTo(data["vac_metro"], user_city)


    # json_data = VacanciesProcess(vacancies_dto).get_vacancies()
    # vacancies_dto = VacanciesDTO().set_text("Python разработчик").set_salary(100000).set_area("1").set_metro("")
    # # await msg.answer(vacancies_dto.get_vacancies_url_attributes())

    print(int(data["vac_salary"]))

    vacancies_dto = VacanciesDTO().set_text(data["vac_name"]).set_salary(data["vac_salary"]).set_area("1").set_metro(id_metro)
    print(vacancies_dto.get_vacancies_url_attributes())
    json_data = VacanciesProcess(vacancies_dto).get_vacancies()
    print(len(json_data.items))

    if len(json_data.items) == 0:
        print("!!!!!!!!!!!")
        vacancies_dto = VacanciesDTO().set_text(data["vac_name"]).set_area("1")
        json_data = VacanciesProcess(vacancies_dto).get_vacancies()
        print(json_data.items[0].name)
        print(json_data.items[0].area.name)
        print(json_data.items[0].alternate_url)
        if len(json_data.items) != 0:
            await message.answer("Вакансия:\n" + "Город: " + json_data.items[0].area.name + "\nНазвание вакансии: " + json_data.items[0].name + "\nСсылка на вакансию: " + json_data.items[0].alternate_url, reply_markup=keyboards.back)
        else:
            await message.answer("Ничего не нашлось", reply_markup=keyboards.back)
    else:
        if len(json_data.items) != 0:
            if json_data.items[0].address.metro.station_name is not None:
                await message.answer("Вакансия:\n" + "Город: " + json_data.items[0].area.name + "\nНазвание вакансии: " + json_data.items[0].name + "\nСтанция метро: " + json_data.items[0].address.metro.station_name + "\nСсылка на вакансию: " + json_data.items[0].alternate_url, reply_markup=keyboards.back)
            else:
                await message.answer(
                    json_data.items[0].area.name + " " + json_data.items[0].name + " " + json_data.items[0].alternate_url, reply_markup=keyboards.back)
        else:
            await message.answer("Ничего не нашлось", reply_markup=keyboards.back)

    # finally:
    #     await message.answer("Ничего не нашлось... Мы работаем над этим.")
    # await message.answer(json_data.items[0].area.name + " "
    #                      + json_data.items[0].name + " " + json_data.items[0].address)

