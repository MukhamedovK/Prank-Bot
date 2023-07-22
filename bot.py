import logging
import datetime

from aiogram import Bot, Dispatcher, executor
from aiogram.types import *
from keyboard import start_btn, order_prank_btn, my_pranks_btn, cabinet_btn, premium_btn


logging.basicConfig(level=logging.INFO)

BOT_TOKEN = "6251779786:AAG3lZJXf7u2-r7rBOW29ZhSiCbEL7ZF3zw"


bot = Bot(token=BOT_TOKEN, parse_mode='html')
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def start_handler(message: Message):
    btn = await start_btn()
    await message.answer("<b>Добро пожаловать в Пранк-Бота 💥</b>\n\n"
                        "<b>Чтобы разыграть своего друга нажми на кнопку «<i>Заказать пранк</i></b>» 👇🏻",
                        reply_markup=btn)
    

@dp.callback_query_handler(text='order')
async def order_prank(call: CallbackQuery):
    btn = await order_prank_btn()
    await call.message.edit_text("Выбери категорию пранков 😏", reply_markup=btn)


@dp.callback_query_handler(text='my_pranks')
async def my_pranks(call: CallbackQuery):
    btn = await my_pranks_btn()
    await call.message.edit_text("🔊 Здесь вы можете прослушать аудиозаписи пранков.", reply_markup=btn)


@dp.callback_query_handler(text='cabinet')
async def cabinet(call: CallbackQuery):
    btn = await cabinet_btn()
    registration_date = datetime.datetime.now()
    await call.message.edit_text("🧑🏻‍💻 Кабинет\n\n"
                                f"🆔 Ваш ID: {call.message.from_user.id}\n"
                                f"📅 Дата регистрации: {registration_date}\n\n"
                                "💰 Ваш баланс: <i>0 RUB</i>\n"
                                "👥 Рефералов приглашено: <i>0</i>\n\n"
                                "💎 Премиум статус: <i>Неактивен</i>", reply_markup=btn)


@dp.callback_query_handler(text='premium')
async def premium(call: CallbackQuery):
    btn = await premium_btn()
    await call.message.edit_text("💎ПРЕМИУМ ПОДПИСКА:\n\n"
                                "- Заказывай <b>пранки со скидкой 30%</b>⚡️\n"
                                "- <b>Выбирай номер телефона</b> с которого доставляются пранки\n☎️\n"
                                "- Получай <b>за рефералов на 10% больше</b> 📈\n\n"
                                "Успей купить премиум со скидкой всего за <b>299 руб/мес.</b>❗️", reply_markup=btn)


@dp.callback_query_handler(text='back')
async def back(call: CallbackQuery):
    btn = await start_btn()
    await call.message.edit_text("<b>Добро пожаловать в Пранк-Бота 💥</b>\n\n"
                                 "<b>Чтобы разыграть своего друга нажми на кнопку «<i>Заказать пранк</i></b>» 👇🏻", reply_markup=btn)




if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
