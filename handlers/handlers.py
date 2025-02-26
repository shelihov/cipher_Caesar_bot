from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from keyboards.keyboards import main_kb, language_kb
from lexicon.lexicon import LEXICON

router = Router()
user_data = {}

# Хендлер на команду /start
@router.message(Command("start"))
async def process_start_command(message: Message):
    user_id = message.from_user.id
    user_data[user_id] = {
        'cipher_mode': '',
        'language': '',
        'choice_digit': 0
    }
    await message.answer(LEXICON['start'], reply_markup=main_kb)

# Хендлер на команду /help
@router.message(Command("help"))
async def process_help_command(message: Message):
    await message.answer(LEXICON['help'])

# Хендлер на шифрование/дешифрование
@router.message(F.text.in_(['Шифрование', 'Дешифрование']))
async def process_cipher(message: Message):
    user_id = message.from_user.id
    choise_user = message.text
    user_data[user_id]['cipher_mode'] = choise_user
    await message.answer(f'Вы выбрали: {choise_user}\n\nВыберите язык:', reply_markup=language_kb)

# Хендлер на выбор языка
@router.message(F.text == "Русский")
async def process_russian_language(message: Message):
    await message.answer(LEXICON['russian_language'])

@router.message(F.text == "Английский")
async def process_english_language(message: Message):
    await message.answer(LEXICON['english_language'])

# Хендлер отправки сообщения с шагом сдвига
@router.message(F.text.regexp(r'^[1-9]\d*$'))
async def process_choise_digit(message: Message):
    await message.answer(LEXICON['choise_digit'])

# Хендлер на callback_query
@router.callback_query(F.data == "button1")
async def process_button1(callback: CallbackQuery):
    await callback.answer("Вы нажали кнопку 1!")

@router.callback_query(F.data == "button2")
async def process_button2(callback: CallbackQuery):
    await callback.answer("Вы нажали кнопку 2!") 