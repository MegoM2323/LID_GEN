import Config

import asyncio
import logging

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

bot = Bot(token=Config.BotToken)
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(Config.hello_text)


@dp.message(Command('help'))
async def get_help(message: Message):
    await message.answer(Config.help_message)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    if Config.TestMode:
        logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
