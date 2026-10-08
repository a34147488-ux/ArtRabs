import os
import asyncio

from aiogram import Bot, Dispatcher
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command, CommandStart


TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("BOT_TOKEN не найден в Railway Variables")


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


@dp.message(CommandStart())
async def start(message: Message):

    args = message.text.split()

    if len(args) > 1:
        ref = args[1]

        await message.answer(
            f"""
⭐ Добро пожаловать в АртRabs!

Ты пришёл по приглашению пользователя:
{ref}

Твой аккаунт создан.
"""
        )

    else:
        await message.answer(
            """
⭐ Добро пожаловать в АртRabs!

Экономическая система работников.

Развивай команду,
получай Multi Stars,
участвуй в активностях.
"""
        )

    await message.answer(
        "Главное меню:",
        reply_markup=menu
    )


@dp.message()
async def buttons(message: Message):

    text = message.text


    if text == "⭐ Баланс":

        await message.answer(
            """
⭐ Твой баланс:

⭐ Stars: 0

✨ Multi Stars: 0
"""
        )


    elif text == "👷 Работники":

        await message.answer(
            """
👷 Работники АртRabs


Всего работников:
0


Доход:
0 ✨ Multi Stars / неделю
"""
        )


    elif text == "🎁 Рулетка":

        await message.answer(
            """
🎁 Ежедневная рулетка


Награды:

⭐ 0-5 Stars


Доступна 1 раз в сутки.
"""
        )


    elif text == "📦 Кейсы":

        await message.answer(
            """
📦 Кейсы АртRabs


Покупка за Multi Stars


Возможные результаты:

✨ +3500
✨ +2000
✨ +500
0
❌ -1000
"""
        )


    elif text == "💱 Обмен":

        await message.answer(
            """
💱 Обмен валюты


Курс:


1000 ✨ Multi Stars
=
0.25 ⭐ Stars


Минимальный обмен:
1000 Multi Stars
"""
        )


    elif text == "👥 Пригласить":

        info = await bot.get_me()

        link = (
            f"https://t.me/{info.username}"
            f"?start={message.from_user.id}"
        )


        await message.answer(
            f"""
👥 Работники АртRabs


Твоя ссылка:


{link}


За каждого приглашённого:
✨ +500 Multi Stars


Приглашай людей и развивай свою команду.
"""
        )


    elif text == "🏆 Топы":

        await message.answer(
            """
🏆 Топы АртRabs


👷 Топ работников

💰 Топ балансов

✨ Топ заработка
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

    print("ArtRabs запущен")

    await dp.start_polling(bot)



if __name__ == "__main__":
    asyncio.run(main())
