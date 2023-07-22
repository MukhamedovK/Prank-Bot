from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def start_btn():
    btn = InlineKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn.add(
        InlineKeyboardButton("🔥 Заказать пранки", callback_data="order"),
        InlineKeyboardButton("🔊 Мои пранки", callback_data="my_pranks"),
        InlineKeyboardButton("🏠 Личный кабинет", callback_data="cabinet"),
        InlineKeyboardButton("💎 Премиум подписка", callback_data="premium"),
        InlineKeyboardButton("⭐️ Лучшие пранки", url="https://t.me/borya_mba"),
    )

    return btn


async def order_prank_btn():
    btn = InlineKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn.add(
        InlineKeyboardButton("🤬 Наезды", callback_data="assaults"),
        InlineKeyboardButton("🤭 Приколы", callback_data="fun"),
        InlineKeyboardButton("🧔🏻‍♂️ Кавказцы", callback_data="caucasians"),
        InlineKeyboardButton("🔙 Назад", callback_data="back"),
    )

    return btn


async def my_pranks_btn():
    btn = InlineKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn.add( InlineKeyboardButton("🔙 Назад", callback_data="back") ) 

    return btn


async def cabinet_btn():
    btn = InlineKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn.add(
        InlineKeyboardButton("💸 Пополнить баланс", callback_data="balace"),
        InlineKeyboardButton("💳 Список платежей", callback_data="list"),
        InlineKeyboardButton("👥 Реферальная система", callback_data="referal"),
        InlineKeyboardButton("📙 Условия использования", callback_data="conditions"),
        InlineKeyboardButton("🧾 Ввести e-mail для чеков", callback_data="enter_e-mail"),
        InlineKeyboardButton("♻️ Сообщить о проблеме", callback_data="problem"),
        InlineKeyboardButton("🔙 Назад", callback_data="back")
        ) 

    return btn


async def premium_btn():
    btn = InlineKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn.add(
        InlineKeyboardButton("💸 Оформить премиум", callback_data="checkout"),
        InlineKeyboardButton("🔙 Назад", callback_data="back"),
    )

    return btn