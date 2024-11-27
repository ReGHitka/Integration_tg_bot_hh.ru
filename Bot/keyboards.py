from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Поиск вакансий')]
])

name_vac = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Стажер разработчик Java'),
     KeyboardButton(text='Стажер разработчик C#'), KeyboardButton(text='Стажер разработчик Python')],
    [KeyboardButton(text='Стажер бизнес аналитик'),
     KeyboardButton(text='Стажер систменый аналитик'), KeyboardButton(text='Стажер инженер связи')]
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