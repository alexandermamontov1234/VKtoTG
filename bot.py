import os
import asyncio

from aiogram import Bot, Dispatcher, executor, types
from main import get_data
from dotenv import load_dotenv


load_dotenv()
TG_TOKEN = str(os.getenv('TG_TOKEN'))
chat_id = str(os.getenv('chat_id'))

bot = Bot(TG_TOKEN)
dp = Dispatcher(bot)


async def on_startup(_):
    print('Бот успешно запущен')


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(text="Бот начал работу")


async def post():
    while True:
        await asyncio.sleep(10)
        for key, value in get_data().items():
            if value:
                await bot.send_photo(chat_id=chat_id,
                                     photo=value,
                                     caption=key)
            else:
                await bot.send_message(chat_id=chat_id,
                                       text=key)


if __name__ == '__main__':
    asyncio.run(post())
    executor.start_polling(dp,
                           on_startup=on_startup,
                           skip_updates=True)
