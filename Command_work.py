from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from asyncio import sleep
from datetime import datetime
import requests, datetime
from random import choice

bot = Bot(token="")  # Токен вашего бота

dp = Dispatcher(bot=bot)

info_bot = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Цитаты🥸🤓'),
            KeyboardButton('Праздники🎉🎉')
        ],
        [
            KeyboardButton('Инфо обо мне🤖'),
            KeyboardButton('Что умеет бот?')
        ],
        [
            KeyboardButton('О разработчике🫡')
        ]
    ], resize_keyboard=True
)


@dp.message_handler(text="/start")
async def cms_start(message: types.Message):
    await message.answer(f"Привет {message.from_user.full_name}👋\n"
                         f"Добро пожаловать в бота🤖\n"
                         f"Информацию о боте можете получить ниже⏬", reply_markup=info_bot)


@dp.message_handler(text="Цитаты🥸🤓")
async def cmd_цит(message: types.Message):
    quote = requests.get('https://favqs.com/api/qotd').json()
    quote_ind = quote['quote']['body']
    quote_aut = quote['quote']['author']
    await message.answer(f"Цытата дня: {quote_ind}\n"
                         f"Автор: {quote_aut}")


@dp.message_handler(text="Праздники🎉🎉")
async def cmd_holi(message: types.Message):
    date = datetime.datetime.now()
    year = date.year
    month = date.month
    day = date.day
    api_key = '32e77b054f60a5ae55f3d61e2e806f4e39e81141'
    holi_apis = requests.get(
        f"https://calendarific.com/api/v2/holidays?api_key={api_key}&country=UZ&year={year}&month={month}&day={day}").json()
    holi_apis = holi_apis['response']['holidays']
    if holi_apis:
        await message.answer(f"в Узбекистане сегодня праздник{holi_apis}🥳")
    else:
        await message.answer("Извините сегодня нет праздников☹️")


@dp.message_handler(text="Инфо обо мне🤖")
async def cmd_bot_info(message: types.Message):
    words = ['Плохой', "Хороший", "Странный", "Просто мразь", "Пофигист", "Анимешник", "Репер", "Задрот", "Разраб",
             "Пидор", "Долбоёб", "🔷ЛОХ🔷", "Куряший унитаз", "Терпила", "Уролог", "Испорчанный ГОНДОН",
             "💯Шлюха бесплатная💯", "Обосанный", "Хитро жук", "Дро4ер", "Трпяка"]
    await message.answer("Что знает о вас этот бот ?\n"
                         f"🔷 Вы: {message.from_user.full_name}😉\n"
                         f"🔷 Ваш ID: {message.from_user.id}🆔\n"
                         f"🔷 Ваш пользовательская имя: {message.from_user.username}🤩\n"
                         f"🔷 А ещё вы {choice(words)}")


@dp.message_handler(text="Что умеет бот?")
async def cmd_bot_csn(message: types.Message):
    await message.answer("Я бот пока в БЕТА версии\n"
                         "Просто заходи туда сюда")


@dp.message_handler(text="О разработчике🫡")
async def cmd_info(message: types.Message):
    await message.answer("Создатель не особо любит личные обсуждение\n"
                         f"J_A_V_A никнейм разработчика\n"
                         f"в 20 лет ученик Максима Орлова, директора MRIT\n"
                         f"contact +998(97) 406-11-55")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
