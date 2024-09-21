import Config
import asyncio
import logging
import data_handler
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

bot = Bot(token=Config.BotToken)
dp = Dispatcher()
Version = '1.4'


@dp.message(CommandStart())
async def cmd_start(message: Message):
    if data_handler.add_user(telegram_id=str(message.from_user.id), name=message.from_user.username) == 1:
        await message.answer(Config.hello_text[0])
        print(f'+ {message.from_user.id} {message.from_user.username}')
        data_handler.send_telegram_message(f'+ {message.from_user.id} {message.from_user.username}')
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
        print(f"Version: {Version}")
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
