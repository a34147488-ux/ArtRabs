import os

print("DATABASE:", os.getenv("DATABASE_URL"))
import asyncpg
import os

DATABASE_URL = os.getenv("DATABASE_URL")

db = None

async def connect_db():
    global db
    db = await asyncpg.create_pool(DATABASE_URL)
import os
import random
import time
import asyncio

from aiogram import Bot, Dispatcher
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import CommandStart


TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()


users = {}


menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="👷 Работники"),
            KeyboardButton(text="🎁 Рулетка")
        ],
        [
            KeyboardButton(text="💱 Обмен"),
            KeyboardButton(text="📦 Кейсы")
        ],
        [
            KeyboardButton(text="🏆 Топы"),
            KeyboardButton(text="👤 Профиль")
        ],
        [
            KeyboardButton(text="👥 Пригласить")
        ]
    ],
    resize_keyboard=True
)


images = {

"workers":
"https://i.imgur.com/example_workers.jpg",

"exchange":
"https://i.imgur.com/example_exchange.jpg",

"roulette":
"https://i.imgur.com/example_roulette.jpg",

"cases":
"https://i.imgur.com/example_cases.jpg",

"profile":
"https://i.imgur.com/example_profile.jpg",

"tops":
"https://i.imgur.com/example_tops.jpg"

}



@dp.message(CommandStart())
async def start(message: Message):

    user_id = message.from_user.id


    if user_id not in users:

        users[user_id] = {

            "stars":0,
            "multi":0,
            "workers":0,
            "last_spin":0

        }


    await message.answer(
        """
⭐ Добро пожаловать в ArtRabs!


Развивай работников,
получай Multi Stars,
участвуй в событиях.
""",
        reply_markup=menu
    )



@dp.message()
async def handler(message: Message):

    user = users[message.from_user.id]


    if message.text == "👥 Пригласить":


        info = await bot.get_me()

        link = (
            f"https://t.me/{info.username}"
            f"?start={message.from_user.id}"
        )


        await message.answer(
            f"""
👷 Работники ArtRabs


Твоя ссылка:

{link}


За каждого приглашённого:

✨ +500 Multi Stars
"""
        )



    elif message.text == "🎁 Рулетка":


        now = time.time()


        if now - user["last_spin"] < 86400:

            await message.answer(
                "⏳ Рулетка доступна раз в сутки."
            )

            return



        prize = random.randint(0,5)

        user["stars"] += prize

        user["last_spin"] = now


        await message.answer(
            f"""
🎁 Ежедневная рулетка


Выпало:

⭐ {prize} Stars


Баланс:
⭐ {user["stars"]}
"""
        )



    elif message.text == "💱 Обмен":


        amount = user["multi"]


        if amount < 1000:

            await message.answer(
                """
💱 Обмен


Минимум:
1000 Multi Stars


Твой баланс:

✨ {amount}
"""
            )

        else:

            stars = amount // 4000

            user["stars"] += stars

            user["multi"] = 0


            await message.answer(
                f"""
✅ Обмен выполнен


Получено:

⭐ {stars} Stars
"""
            )



    elif message.text == "👷 Работники":


        await message.answer(
            f"""
👷 Работники ArtRabs


Количество:

{user["workers"]}


Доход:

0 Multi Stars / неделю
"""
        )



    elif message.text == "👤 Профиль":


        await message.answer(
            f"""
👤 Профиль


⭐ Stars:
{user["stars"]}


✨ Multi Stars:
{user["multi"]}


👷 Работники:
{user["workers"]}
"""
        )



    elif message.text == "📦 Кейсы":


        win = random.choice(
            [
                3500,
                2000,
                500,
                0,
                -1000
            ]
        )


        user["multi"] += win


        await message.answer(
            f"""
📦 Кейс открыт


Результат:

✨ {win} Multi Stars
"""
        )



    elif message.text == "🏆 Топы":

        await message.answer(
            """
🏆 Топы ArtRabs


👷 Лучшие работники

💰 Лучшие балансы

✨ Лучшие заработки
"""
        )



async def main():

    print("ArtRabs запущен")

    await dp.start_polling(bot)



if __name__ == "__main__":

    asyncio.run(main())
async def create_tables():
    async with db.acquire() as conn:
        await conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id BIGINT PRIMARY KEY,
            username TEXT,
            stars INTEGER DEFAULT 0,
            multistars INTEGER DEFAULT 0,
            referrals INTEGER DEFAULT 0,
            ref_income INTEGER DEFAULT 0
        );
        """)
        async def on_startup():
    await connect_db()
    await create_tables()
