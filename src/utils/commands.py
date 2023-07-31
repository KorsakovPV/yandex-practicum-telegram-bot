from aiogram.types import BufferedInputFile, FSInputFile, Message

import text
from keyboards import keyboards
from logger import logger
from utils import levenshtein, utils


async def menu(message: Message):
    logger.info("menu")
    await message.answer(text.menu, reply_markup=keyboards.menu)


async def send_last_self_photo(message: Message):
    logger.info("send_last_self_photo")
    photo = FSInputFile("images/last_self_photo.jpg")
    await message.answer_photo(photo=photo)


async def send_school_self_photo(message: Message):
    logger.info("send_school_self_photo")
    photo = FSInputFile("images/school_self_photo.png")
    await message.answer_photo(photo=photo)


async def send_my_hobby(message: Message):
    logger.info("send_my_hobby")
    photo = FSInputFile("images/old_road.jpg")
    await message.answer_photo(
        photo=photo,
        caption=text.my_hobby,
    )
    voice = BufferedInputFile(
        file=utils.generate_voice(text.my_hobby), filename="voice.wav"
    )
    await message.answer_voice(voice=voice)


async def send_what_is_gpt_for_grandma(message: Message):
    logger.info("send_what_is_gpt_for_grandma")
    voice = FSInputFile("voices/what_is_gpt_for_grandma.ogg")
    await message.answer_voice(voice=voice)


async def send_sql_or_nosql_differences(message: Message):
    logger.info("send_sql_or_nosql_differences")
    voice = FSInputFile("voices/sql_or_nosql_differences.ogg")
    await message.answer_voice(voice=voice)


async def send_first_love(message: Message):
    logger.info("send_first_love")
    voice = FSInputFile("voices/first_love.ogg")
    await message.answer_voice(voice=voice)


async def send_github_link(message: Message):
    logger.info("send_github_link")
    await message.answer(text=text.github_link)


async def send_habr_link(message: Message):
    logger.info("send_github_link")
    await message.answer(text=text.habr_link)


class Command:
    def __init__(self, command, fn):
        self.levenshtein_distance = 0
        self.command = command
        self.fn = fn

    def __gt__(self, other):
        return self.levenshtein_distance > other.levenshtein_distance


commands = [
    Command("меню", menu),
    Command("последнее селфи", send_last_self_photo),
    Command("фото из старшей школы", send_school_self_photo),
    Command("мое увлечение", send_my_hobby),
    Command("что такое джи пи ти для бабушки", send_what_is_gpt_for_grandma),
    Command("разница между эскюэль и нойскюэль", send_sql_or_nosql_differences),
    Command("история первой любви", send_first_love),
    Command("ссылка на гитхаб", send_github_link),
    Command("ссылка на хабр", send_habr_link),
]


def call_command(recognize_command: str):
    for command in commands:
        command.levenshtein_distance = levenshtein.levenshtein(
            command.command, recognize_command
        )

    commands.sort()
    logger.info(
        f"recognize_command '{recognize_command}'. "
        f"Command '{commands[0].command}'. "
        f"Levenshtein_distance={commands[0].levenshtein_distance}"
    )
    return commands[0]
