from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

# Основная клавиатура
main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Шифрование🔐"), KeyboardButton(text="Дешифрование🔓")],
        #[KeyboardButton(text="Помощь")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

# Клавиатура языка
language_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Русский🇷🇺"), KeyboardButton(text="Английский🇺🇲")],
        #[KeyboardButton(text="Помощь")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)