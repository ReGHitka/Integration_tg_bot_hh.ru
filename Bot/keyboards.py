from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Поиск вакансий'), KeyboardButton(text='Поиск 5 - ти вакансий')],
    [KeyboardButton(text='Пройти опрос'), KeyboardButton(text='Пример хорошего резюме'), KeyboardButton(text='Официальные сайты компаний')]
])

main_search = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Поиск вакансий')]
])

name_vac = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Разработчик Java'),
     KeyboardButton(text='Разработчик C#'), KeyboardButton(text='Разработчик Python')],
    [KeyboardButton(text='Бизнес аналитик'),
     KeyboardButton(text='Систменый аналитик'), KeyboardButton(text='Инженер связи')]
])

metro = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Авиамоторная'), KeyboardButton(text='Марксистская'),
     KeyboardButton(text='Народное ополчение')],
    [KeyboardButton(text='Бульвар Дмитрия Донского'),
     KeyboardButton(text='Нагатинская'), KeyboardButton(text='Кленовый бульвар')]
])

salary = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='30000'), KeyboardButton(text='40000'), KeyboardButton(text='50000')]
])

back = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Вернуться в главное меню')]
])