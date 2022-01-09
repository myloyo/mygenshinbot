from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

Mondstadt = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='Альбедо'),
            KeyboardButton(text='Эмбер'),
            KeyboardButton(text='Барбара'),
            KeyboardButton(text='Беннет'),
            KeyboardButton(text='Дилюк'),
        ],
        [
            KeyboardButton(text='Диона'),
            KeyboardButton(text='Эола'),
            KeyboardButton(text='Фишль'),
            KeyboardButton(text='Джинн'),
            KeyboardButton(text='Кэйа'),
        ],
        [
            KeyboardButton(text='Кли'),
            KeyboardButton(text='Лиза'),
            KeyboardButton(text='Мона'),
            KeyboardButton(text='Ноэлль'),
            KeyboardButton(text='Рэйзор')
        ],
        [
            KeyboardButton(text='Розария'),
            KeyboardButton(text='Сахароза'),
            KeyboardButton(text='Венти')
        ],
    ],
    resize_keyboard=True
)
