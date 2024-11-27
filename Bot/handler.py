from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from hh_ru_api.model.dto.vacancies_dto import VacanciesDTO
from hh_ru_api.processes import VacanciesProcess
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
    await msg.answer("Привет!", reply_markup=keyboards.main)

@router.message(Command('test1'))
async def handler_1(msg: Message):
    vacancies_dto = VacanciesDTO().set_text("Водитель").set_salary(100000).set_area("1").set_metro("1")
    # await msg.answer(vacancies_dto.get_vacancies_url_attributes())
    json_data = VacanciesProcess(vacancies_dto).get_vacancies()
    if json_data is not None:
        await msg.answer(json_data.items[0].area.name + " "
                         + json_data.items[0].name + json_data.items[0].address.metro.station_name)
    else:
        await msg.answer("Ничего не нашлось")

    # await msg.answer(json_data.items[0].area.name + " "
    #                  + json_data.items[0].name + json_data.items[0].address.metro.station_name)

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
    vacancies_dto = (VacanciesDTO().set_text({data["vac_name"]})
                     .set_salary("1").set_area("1"))
    json_data = VacanciesProcess(vacancies_dto).get_vacancies()
    await message.answer(json_data.items[0].area.name + " "
                         + json_data.items[0].name + " " + json_data.items[0].address)
