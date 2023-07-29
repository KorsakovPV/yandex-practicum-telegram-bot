from aiogram import Bot, F, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, FSInputFile, Message

import text
from config.config import settings
from config.logger import logger
from keyboards import keyboards


async def start_bot(bot: Bot):
    logger.info("start_bot")
    await bot.send_message(chat_id=settings.ADMIN_ID, text="Бот запущен! /start")


async def stop_bot(bot: Bot):
    logger.info("stop_bot")
    await bot.send_message(chat_id=settings.ADMIN_ID, text="Бот остановлен !")


router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    logger.info("start_handler")
    await msg.answer(
        text.greet.format(name=msg.from_user.full_name), reply_markup=keyboards.menu
    )


@router.message(F.text == "Меню")
async def menu(msg: Message):
    logger.info("menu")
    await msg.answer(text.menu, reply_markup=keyboards.menu)


@router.callback_query(F.data == "last_self_photo")
async def send_last_self_photo(clbck: CallbackQuery, state: FSMContext):
    logger.info("send_last_self_photo")
    photo = FSInputFile("images/last_self_photo.jpg")
    await clbck.message.answer_photo(photo=photo)


@router.callback_query(F.data == "school_self_photo")
async def send_school_self_photo(clbck: CallbackQuery, state: FSMContext):
    logger.info("send_school_self_photo")
    photo = FSInputFile("images/school_self_photo.png")
    await clbck.message.answer_photo(photo=photo)


@router.callback_query(F.data == "my_hobby")
async def send_my_hobby(clbck: CallbackQuery, state: FSMContext):
    logger.info("send_my_hobby")
    photo = FSInputFile("images/old_road.jpg")
    await clbck.message.answer_photo(
        photo=photo,
        caption=text.my_hobby,
    )


@router.callback_query(F.data == "what_is_gpt_for_grandma")
async def send_what_is_gpt_for_grandma(clbck: CallbackQuery, state: FSMContext):
    logger.info("send_what_is_gpt_for_grandma")
    voice = FSInputFile("voices/what_is_gpt_for_grandma.mp3")
    await clbck.message.answer_voice(voice=voice)


@router.callback_query(F.data == "sql_or_nosql_differences")
async def send_sql_or_nosql_differences(clbck: CallbackQuery, state: FSMContext):
    logger.info("send_sql_or_nosql_differences")
    voice = FSInputFile("voices/sql_or_nosql_differences.mp3")
    await clbck.message.answer_voice(voice=voice)


@router.callback_query(F.data == "first_love")
async def send_first_love(clbck: CallbackQuery, state: FSMContext):
    logger.info("send_first_love")
    voice = FSInputFile("voices/first_love.mp3")
    await clbck.message.answer_voice(voice=voice)


@router.callback_query(F.data == "github_link")
async def send_github_link(clbck: CallbackQuery, state: FSMContext):
    logger.info("send_github_link")
    await clbck.message.answer(text=text.github_link)


@router.callback_query(F.data == "habr_link")
async def send_habr_link(clbck: CallbackQuery, state: FSMContext):
    logger.info("send_github_link")
    await clbck.message.answer(text=text.habr_link)
