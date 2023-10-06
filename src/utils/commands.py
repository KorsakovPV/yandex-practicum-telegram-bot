from aiogram.types import BufferedInputFile, FSInputFile, Message

from keyboards import keyboards
from logger import logger
from text import bot_answer
from utils import levenshtein, utils


class Command:
    def __init__(self, command, fn):
        self.levenshtein_distance = 0
        self.command = command
        self.fn = fn

    def __gt__(self, other):
        return self.levenshtein_distance > other.levenshtein_distance

    def comparison(self, recognize_command):
        self.levenshtein_distance = levenshtein.levenshtein(
            self.command, recognize_command
        )


class Commands:
    def __init__(self):
        self.commands = [
            Command("меню", self.menu),
            Command("последнее селфи", self.send_last_self_photo),
            Command("фото из старшей школы", self.send_school_self_photo),
            Command("мое увлечение", self.send_my_hobby),
            Command(
                "что такое джи пи ти для бабушки", self.send_what_is_gpt_for_grandma
            ),
            Command(
                "разница между эскюэль и нойскюэль", self.send_sql_or_nosql_differences
            ),
            Command("история первой любви", self.send_first_love),
            Command("ссылка на гитхаб", self.send_github_link),
            Command("ссылка на хабр", self.send_habr_link),
        ]

    def call_command(self, recognize_command: str):
        for command in self.commands:
            command.comparison(recognize_command)

        self.commands.sort()
        logger.info(
            f"recognize_command '{recognize_command}'. "
            f"Command '{self.commands[0].command}'. "
            f"Levenshtein_distance={self.commands[0].levenshtein_distance}"
        )
        return self.commands[0]

    @staticmethod
    async def menu(message: Message):
        logger.info("menu")
        await message.answer(bot_answer.menu, reply_markup=keyboards.menu)

    @staticmethod
    async def send_last_self_photo(message: Message):
        logger.info("send_last_self_photo")
        photo = FSInputFile("images/last_self_photo.jpg")
        await message.answer_photo(photo=photo)

    @staticmethod
    async def send_school_self_photo(message: Message):
        logger.info("send_school_self_photo")
        photo = FSInputFile("images/school_self_photo.png")
        await message.answer_photo(photo=photo)

    @staticmethod
    async def send_my_hobby(message: Message):
        logger.info("send_my_hobby")
        photo = FSInputFile("images/old_road.jpg")
        await message.answer_photo(
            photo=photo,
            caption=bot_answer.my_hobby,
        )
        voice = BufferedInputFile(
            file=utils.generate_voice(bot_answer.my_hobby), filename="voice.wav"
        )
        await message.answer_voice(voice=voice)

    @staticmethod
    async def send_what_is_gpt_for_grandma(message: Message):
        logger.info("send_what_is_gpt_for_grandma")
        voice = FSInputFile("voices/what_is_gpt_for_grandma.mp3")
        await message.answer_voice(voice=voice)

    @staticmethod
    async def send_sql_or_nosql_differences(message: Message):
        logger.info("send_sql_or_nosql_differences")
        voice = FSInputFile("voices/sql_or_nosql_differences.mp3")
        await message.answer_voice(voice=voice)

    @staticmethod
    async def send_first_love(message: Message):
        logger.info("send_first_love")
        voice = FSInputFile("voices/first_love.mp3")
        await message.answer_voice(voice=voice)

    @staticmethod
    async def send_github_link(message: Message):
        logger.info("send_github_link")
        await message.answer(text=bot_answer.github_link)

    @staticmethod
    async def send_habr_link(message: Message):
        logger.info("send_github_link")
        await message.answer(text=bot_answer.habr_link)


commands = Commands()
