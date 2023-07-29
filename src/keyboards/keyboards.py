from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

menu = [
    [
        InlineKeyboardButton(text="Последнее селфи", callback_data="last_self_photo"),
        InlineKeyboardButton(
            text="Фото из старшей школы", callback_data="school_self_photo"
        ),
    ],
    [
        InlineKeyboardButton(text="Мое увлечение", callback_data="my_hobby"),
        InlineKeyboardButton(
            text="Что такое GPT для бабушки", callback_data="what_is_gpt_for_grandma"
        ),
    ],
    [
        InlineKeyboardButton(
            text="Разницу между SQL и NoSQL", callback_data="sql_or_nosql_differences"
        ),
        InlineKeyboardButton(
            text="История первой любви", callback_data="sql_or_nosql_differences"
        ),
    ],
    [
        InlineKeyboardButton(text="Ссылка на github", callback_data="github_link"),
        InlineKeyboardButton(text="Ссылка на habr", callback_data="github_link"),
    ],
]
menu = InlineKeyboardMarkup(inline_keyboard=menu)
