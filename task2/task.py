from aiogram import Bot, Dispatcher
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command
import asyncio
import logging
from aiogram.types import FSInputFile
from pathlib import Path


# Включаем логирование
logging.basicConfig(level=logging.INFO)

# Укажите токен бота
API_TOKEN = "7754673241:AAGhe1h9muCl1W8B5aFreT0ihpLQxbu0u_Q"

# Создаем бота и диспетчер
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Создаем клавиатуру

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📚 Курсы")],
        [KeyboardButton(text="📅 Расписание")],
        [KeyboardButton(text="📞 Контакты")],
        [KeyboardButton(text="❓ Задать вопрос")],
    ],
    resize_keyboard=True
)

courses_names = {"Картина маслом за 3 часа",
                 "Курс живописи маслом",
                 "Интерьерная картина",
                 "Fashion-иллюстрация",
                 "Акварель",
                  "Рисование на планшете"
                 }

courses_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="1", callback_data="course_1")],
        [InlineKeyboardButton(text="2", callback_data="course_2")],
        [InlineKeyboardButton(text="3", callback_data="course_3")],
        [InlineKeyboardButton(text="4", callback_data="course_4")],
        [InlineKeyboardButton(text="5", callback_data="course_5")],
        [InlineKeyboardButton(text="6", callback_data="course_6")],
        [InlineKeyboardButton(text="Назад", callback_data="back")]
    ]
)

# Обработчик команды /start
@dp.message(Command("start"))
async def send_welcome(message: Message):
    await message.answer(
        "Привет! Я бот школы рисования \"Пикассо\". Чем могу помочь?",
        reply_markup=main_menu
    )

# # Обработчик кнопки "📚 Курсы"
# @dp.message(lambda message: message.text == "📚 Курсы")
# async def courses(message: Message):
#     response = (
#         f"🎨 Наши курсы:\n"
#         "1. {courses_names[0]}\n"
#         "2. {courses_names[1]}\n"
#         "3. {courses_names[2]}\n"
#         "4. {courses_names[3]}\n"
#         "5. {courses_names[4]}\n"
#         "6. {courses_names[5]}\n\n"
#         "Напишите номер курса, чтобы узнать подробности."
#     )
#     await message.answer(response, reply_markup=courses_menu)

# @dp.callback_query(lambda c: c.data.startswith("course_"))
# async def course_details(callback_query):
#     course_number = int(callback_query.data.split("_")[1])  # Извлекаем номер курса из callback_data
    
#     # Формируем запрос для генерации описания курса
#     prompt = f"Напиши описание курса под названием {courses_names[course_number - 1]} в школе рисования."
    
#     # Генерация ответа от модели
#     description = generate_response(prompt)  # Генерация описания курса с использованием модели
    
#     # Отправляем описание курса пользователю
#     await callback_query.message.answer(description, reply_markup=courses_menu)
#     await callback_query.answer()  # Подтверждаем обработку callback

# Обработчик кнопки "Назад"
@dp.callback_query(lambda c: c.data == "back")
async def back_to_courses(callback_query):
    await callback_query.message.answer(
        "Выберите курс, чтобы узнать подробности:",
        reply_markup=courses_menu
    )
    await callback_query.answer()  # Подтверждаем обработку callback

# Обработчик кнопки "📅 Расписание"
@dp.message(lambda message: message.text == "📅 Расписание")
async def schedule(message: Message):
    response_text = (
        "🕒 Наше расписание:\n"
    )
    images_dir = Path(__file__).resolve().parent / "images"
    image_path = images_dir / "schedule.jpg"

    # Отправка изображения
    image = FSInputFile(image_path)  # Загружаем файл
    await message.answer_photo(photo=image, caption=response_text)

# Обработчик кнопки "📞 Контакты"
@dp.message(lambda message: message.text == "📞 Контакты")
async def contacts(message: Message):
    response = (
        "📞 Контакты:\n"
        "Телефон: +7 (123) 456-78-90\n"
        "Email: info@picasso-school.com\n"
        "Адрес: ул. Импрессионистов, д. 10, г. Москва"
    )
    await message.answer(response)

# Обработчик кнопки "❓ Задать вопрос"
@dp.message(lambda message: message.text == "❓ Задать вопрос")
async def ask_question(message: Message):
    await message.answer(
        "📩 Напишите ваш вопрос, и мы постараемся ответить как можно скорее!"
    )

# Обработчик текстовых сообщений для вопросов
@dp.message()
async def handle_questions(message: Message):
    user_question = message.text
    await message.answer(
        "Ваш вопрос принят! Мы ответим вам в ближайшее время."
    )
    # Можно добавить функционал отправки вопроса администратору
    admin_id = 123456789  # Укажите ID администратора
    await bot.send_message(admin_id, f"Вопрос от {message.from_user.full_name}: {user_question}")

async def remove_webhook():
    await bot.delete_webhook()

async def main():
    # Удаляем вебхук перед началом работы
    await remove_webhook()
    # Запуск бота
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
