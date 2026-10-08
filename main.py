import os
import asyncio

from aiogram import Bot, Dispatcher
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command


TOKEN = os.getenv("BOT_TOKEN")


bot = Bot(token=TOKEN)

dp = Dispatcher()



menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="⭐ Баланс"),
            KeyboardButton(text="👷 Работники")
        ],
        [
            KeyboardButton(text="🎁 Рулетка"),
            KeyboardButton(text="📦 Кейсы")
        ],
        [
            KeyboardButton(text="💱 Обмен"),
            KeyboardButton(text="🏆 Топы")
        ],
        [
            KeyboardButton(text="👤 Профиль"),
            KeyboardButton(text="👥 Пригласить")
        ]
    ],
    resize_keyboard=True
)



@dp.message(Command("start"))
async def start(message: Message):

    await message.answer(
        """
⭐ Добро пожаловать в АртRabs!

Игровая экономическая система.

Здесь ты можешь:
👷 развивать работников
✨ получать Multi Stars
🎁 участвовать в активностях
🏆 занимать места в топах
        """,
        reply_markup=menu
    )



@dp.message()
async def buttons(message: Message):

    text = message.text


    if text == "⭐ Баланс":

        await message.answer(
            """
⭐ Stars: 0

✨ Multi Stars: 0
            """
        )


    elif text == "👷 Работники":

        await message.answer(
            """
👷 Работники АртRabs

Количество:
0

Доход:
0 Multi Stars / неделю
            """
        )


    elif text == "🎁 Рулетка":

        await message.answer(
            """
🎁 Ежедневная рулетка

Награды:
0-5 ⭐

Крутить можно 1 раз в день.
            """
        )


    elif text == "📦 Кейсы":

        await message.answer(
            """
📦 Кейсы

Покупка за Multi Stars

Возможные награды:
+3500
+2000
+500
0
-1000
            """
        )


    elif text == "🏆 Топы":

        await message.answer(
            """
🏆 Топы

👷 Топ работников

💰 Топ балансов

📈 Топ заработка
            """
        )


    elif text == "👥 Пригласить":

        await message.answer(
            """
👥 Твои работники

Приглашай людей и получай Multi Stars.
            """
        )


    elif text == "👤 Профиль":

        await message.answer(
            """
👤 Профиль

Уровень:
1

Работников:
0

Баланс:
0
            """
        )



async def main():

    await dp.start_polling(bot)



if __name__ == "__main__":
    asyncio.run(main())
