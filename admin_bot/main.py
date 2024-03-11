from admin_bot.config import token
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.utils.chat_action import ChatActionSender
from additional_scripts import markup as m  # script to create inline keyboard
from aiogram.types import ReplyKeyboardRemove as remove_reply_markup
import asyncio

from db_script.interface import DatabaseInterface


logging.basicConfig(level=logging.INFO)

bot = Bot(token=token)
dp = Dispatcher()


tournaments = {
    "1 Tournament": ["Date", "Team", "Team quantity", "Price", "Close regestration date"],
    "2 Tur": ["sfd", "324", "Tm sf", "402332", "      date"]
}


@dp.message(Command("start"))
async def start(message: types.Message) -> None:
    """Function to handle start command"""
    markup = m.make_markup("Мои турниры", "Создать турнир", "Удалить турнир")
    await message.answer("Что вы хотите сделать?", reply_markup=markup)


@dp.message(lambda message: message.text == "Мои турниры")
async def my_tournaments(message: types.Message):
    """Handling button Мои Турниры"""
    markup = m.make_markup(*[f"Просмотреть турнир {tournament}" for tournament in tournaments.keys()], "Назад")

    await message.answer("Выберите турнир для просмотра", reply_markup=markup)


@dp.message(lambda message: message.text == "Создать турнир")
async def create_tournament(message: types.Message):
    """Handling button Создать турнир"""
    await message.answer("Создание турнира...")

@dp.message(lambda message: message.text == "Удалить турнир")
async def delete_tournament(message: types.Message):
    """Handling button Удалить турнир"""
    await message.answer("Удаление турнира...")


@dp.message(lambda message: "Просмотреть турнир" in message.text)
async def tournament_info(message: types.Message):
    """Get exact tournament info"""
    tournament_name = message.text.split("Просмотреть турнир")[1].strip()
    tournament_info = tournaments[tournament_name]

    markup = m.make_markup(f"Отредактировать турнир {tournament_name}", "В меню просмотра турниров")

    await message.answer(f"Название: {tournament_name}\nДата: {tournament_info[0]}\nКоманда: {tournament_info[1]}\nКол-во учатсников команды: {tournament_info[2]}\nЦена: {tournament_info[3]}\nДата закрытия регистрации: {tournament_info[4]}", reply_markup=markup)


# @dp.message(lambda message: message.text == "В меню просмотра турниров")
# async def back2tournament_info():
#     asyncio.run(tournament_info())


# Добавление обработчика для кнопки "Назад"
async def go_back(message: types.Message):
    await start(message)

# Регистрация обработчиков
def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start, Command("start"))
    dp.register_message_handler(my_tournaments, lambda message: message.text == "Мои турниры")
    dp.register_message_handler(go_back, lambda message: message.text == "Назад")


async def main():
    """Main function. Stands for bot running"""
    await dp.start_polling(bot)
