import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message
from datetime import datetime

# ВСТАВЬТЕ СЮДА ВАШ НОВЫЙ ТОКЕН (полученный через @BotFather)
BOT_TOKEN = "8895879371:AAENY4EgMeCRp9OF8q-6M4Sy-1EbltrqUQU"

# Включаем логирование, чтобы видеть ошибки
logging.basicConfig(level=logging.INFO)

# Создаём объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Обработчик команды /start
@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        "🤖 Привет! Я универсальный бот.\n\n"
        "📋 Мои команды:\n"
        "/start - показать это сообщение\n"
        "/help - список команд\n"
        "/time - текущее время\n"
        "/echo [текст] - повторить ваш текст\n"
        "Просто напиши любое сообщение - я отвечу!"
    )

# Обработчик команды /help
@dp.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer(
        "🔧 Доступные команды:\n"
        "/start - приветствие\n"
        "/time - показать текущее время и дату\n"
        "/echo текст - повторить то, что вы написали\n\n"
        "💬 Также я отвечаю на простые фразы:\n"
        "привет, как дела, спасибо, кто ты"
    )

# Команда /time - показывает текущее время
@dp.message(Command("time"))
async def cmd_time(message: Message):
    now = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    await message.answer(f"🕐 Текущее время: {now}")

# Команда /echo - повторяет текст пользователя
@dp.message(Command("echo"))
async def cmd_echo(message: Message):
    # Получаем текст после команды /echo
    text_to_repeat = message.text.replace("/echo", "", 1).strip()
    if text_to_repeat:
        await message.answer(f"🔊 Эхо: {text_to_repeat}")
    else:
        await message.answer("❌ Напишите что-нибудь после команды /echo, например:\n/echo Привет!")

# Обработчик обычных текстовых сообщений (без команд)
@dp.message()
async def answer_smart(message: Message):
    text = message.text.lower()
    
    if text in ["привет", "здравствуй", "ку", "hi", "hello"]:
        await message.answer("👋 И тебе привет! Как дела?")
    
    elif text in ["как дела", "как ты", "how are you"]:
        await message.answer("✅ Всё отлично, спасибо! Жду твоих команд 😊")
    
    elif text in ["спасибо", "благодарю", "thanks"]:
        await message.answer("🙏 Пожалуйста! Рад помочь.")
    
    elif text in ["кто ты", "что ты умеешь"]:
        await message.answer(
            "🤖 Я бот-помощник. Мои команды:\n"
            "/start, /help, /time, /echo [текст]\n\n"
            "Также я отвечаю на простые приветствия!"
        )
    
    else:
        await message.answer(
            f"📩 Ты написал: {message.text}\n\n"
            "Не знаю, что ответить 😅\n"
            "Используй /help для списка команд."
        )

# Запуск бота
async def main():
    print("🚀 Бот запущен и готов к работе!")
    print("Нажми Ctrl+C для остановки")
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n❌ Бот остановлен пользователем")
