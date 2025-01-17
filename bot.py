import asyncio
import wikipedia
import logging 
from aiogram import Bot, Dispatcher, Router
from aiogram.filters import CommandStart
from aiogram.types import Message

API_TOKEN = '7910667304:AAGyvbYTmAh4pQjcIuA1u1fKu9mYnaim3ao'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()
router = Router()

wikipedia.set_lang('uz')

@router.message(CommandStart())
async def start(message: Message):

    await message.answer(f"Salom {message.from_user.full_name}\nWikipedia botiga xush kelibsiz\nBiror bir so'z yuboring")

@router.message(lambda message: message.text == "/help")
async def help(message: Message):

    await message.answer("Botdan foydalanish uchun botga biror bir so'z yuboring\nBot sizga siz kiritgan so'z haqida wikipediadan maqola beradi agar mavjud bo'lsa")

@router.message()
async def Wikibot(message: Message):

    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer("Bunday mavzu bo'yicha maqola topilmadi")

dp.include_router(router)

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())