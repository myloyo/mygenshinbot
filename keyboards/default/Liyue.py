from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

Liyue = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='Гань Юй'),
            KeyboardButton(text='Ке Цин'),
            KeyboardButton(text='Нин Гуан'),
            KeyboardButton(text='Чжун Ли'),
        ],
        [
            KeyboardButton(text='Сяо'),
            KeyboardButton(text='Ху Тао'),
            KeyboardButton(text='Бей Доу'),
            KeyboardButton(text='Ци Ци'),
        ],
        [
            KeyboardButton(text='Сян Лин'),
            KeyboardButton(text='Синь Янь'),
            KeyboardButton(text='Янь Фей'),
            KeyboardButton(text='Юнь Цзинь'),
        ],
        [
            KeyboardButton(text='Син Цю'),
            KeyboardButton(text='Чунь Юнь'),
            KeyboardButton(text='Шень Хэ'),
        ],
    ],
    resize_keyboard=True
)
