from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

Inazuma = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='Аратаки Итто'),
            KeyboardButton(text='Горо'),
            KeyboardButton(text='Каэдэхара Кадзуха'),
            KeyboardButton(text='Камисато Аяка'),
        ],
        [
            KeyboardButton(text='Куджоу Сара'),
            KeyboardButton(text='Райден Сегун'),
            KeyboardButton(text='Сангономия Кокоми'),
            KeyboardButton(text='Саю'),
        ],
        [
            KeyboardButton(text='Тома'),
            KeyboardButton(text='Ёимия'),
            KeyboardButton(text='Яэ Мико'),
        ],
    ],
    resize_keyboard=True
)
