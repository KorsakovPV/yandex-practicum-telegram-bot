import io
import typing

from aiogram import Bot, F, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from config import bot, settings
from logger import logger
from utils import utils
from utils.commands import commands
from text import bot_answer


async def start_bot(bot: Bot):
    logger.info("start_bot")
    await bot.send_message(chat_id=settings.ADMIN_ID, text="Бот запущен! /start")


async def stop_bot(bot: Bot):
    logger.info("stop_bot")
    await bot.send_message(chat_id=settings.ADMIN_ID, text="Бот остановлен !")


router = Router()


@router.message(Command("start"))
async def start_handler(message: Message):
    logger.info("start_handler")
    await message.answer(bot_answer.greet.format(name=message.from_user.full_name))
    await commands.menu(message)


@router.message(F.text == "Меню")
@router.message(F.text == "Выйти в меню")
@router.message(F.text == "◀️ Выйти в меню")
async def menu(message: Message):
    await commands.menu(message)


@router.callback_query(F.data == "last_self_photo")
async def send_last_self_photo(clbck: CallbackQuery, state: FSMContext):
    await commands.send_last_self_photo(clbck.message)


@router.callback_query(F.data == "school_self_photo")
async def send_school_self_photo(clbck: CallbackQuery, state: FSMContext):
    await commands.send_school_self_photo(clbck.message)


@router.callback_query(F.data == "my_hobby")
async def send_my_hobby(clbck: CallbackQuery, state: FSMContext):
    await commands.send_my_hobby(clbck.message)


@router.callback_query(F.data == "what_is_gpt_for_grandma")
async def send_what_is_gpt_for_grandma(clbck: CallbackQuery, state: FSMContext):
    await commands.send_what_is_gpt_for_grandma(clbck.message)


@router.callback_query(F.data == "sql_or_nosql_differences")
async def send_sql_or_nosql_differences(clbck: CallbackQuery, state: FSMContext):
    await commands.send_sql_or_nosql_differences(clbck.message)


@router.callback_query(F.data == "first_love")
async def send_first_love(clbck: CallbackQuery, state: FSMContext):
    await commands.send_first_love(clbck.message)


@router.callback_query(F.data == "github_link")
async def send_github_link(clbck: CallbackQuery, state: FSMContext):
    await commands.send_github_link(clbck.message)


@router.callback_query(F.data == "habr_link")
async def send_habr_link(clbck: CallbackQuery, state: FSMContext):
    await commands.send_habr_link(clbck.message)


@router.message(F.content_type == "voice")
async def voice_message_handler(message: Message):
    if message.voice.duration > 5:
        await message.answer(text=bot_answer.long_command)
        return
    file_id = message.voice.file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path

    binary_stream = io.BytesIO()
    result_binary_stream: typing.BinaryIO = await bot.download_file(
        file_path, binary_stream
    )

    recognize_command = utils.recognize_command(result_binary_stream)

    command = commands.call_command(recognize_command)

    if command.levenshtein_distance > 3:
        logger.info("unrecognized_command")
        await message.answer(text=bot_answer.unrecognized_command)
        return

    await command.fn(message)
