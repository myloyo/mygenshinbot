from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard = [
        [
        KeyboardButton(text='Мондштадт'),
        KeyboardButton(text='Ли Юэ'),
        KeyboardButton(text='Инадзума'),
        KeyboardButton(text='Снежная')
        ],
    ],
    resize_keyboard=True
)
