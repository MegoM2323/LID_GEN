import Config
import asyncio
import logging
import data_handler
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

bot = Bot(token=Config.BotToken)
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: Message):
    if data_handler.add_user(telegram_id=str(message.from_user.id), name=message.from_user.username) == 1:
        await message.answer(Config.hello_text[0])
    else:
        await message.answer(Config.hello_text[1])


@dp.message(Command('help'))
async def get_help(message: Message):
    await message.answer(Config.help_message)


async def main():
    # dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    data_handler.create_database()
    if Config.TestMode:
        logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
