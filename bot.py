import logging
import os
from dotenv import load_dotevn
load_dotevn()

from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils import executor

from aiogram.types import InlineKeyboardMrkup, InlineKeyboardButton
from aiogram.dispatcher.filters import Text

API_TOKEN = os.getenv("secret_key")

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply(f"salom {message.from_user.first_name}")
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)







#     first_name = message.from_user.first_name
#     await message.reply(f"{first_name}")
#
# @dp.message_handler()
# async def echo(message: types.Message):
#     # old style:
#     # await bot.send_message(message.chat.id, message.text)
#
#     await message.answer(message.text)
#
#
# if __name__ == '__main__':
#     executor.start_polling(dp, skip_updates=True)
