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
@router.message(F.text.in_(['Шифрование🔐', 'Дешифрование🔓']))
async def process_cipher(message: Message):
    user_id = message.from_user.id
    choise_user = message.text
    user_data[user_id]['cipher_mode'] = choise_user
    await message.answer(f'Вы выбрали: {choise_user}\n\nВыберите язык:', reply_markup=language_kb)

# Хендлер на выбор языка
@router.message(F.text.in_(["Русский🇷🇺", "Английский🇺🇲"]))
async def process_russian_language(message: Message):
    user_id = message.from_user.id
    language_user = message.text
    user_data[user_id]['language'] = language_user
    await message.answer(f'Вы выбрали язык: {language_user}\n\nОтправьте шаг сдвига (вправо):')

# Хендлер отправки сообщения с шагом сдвига
@router.message(F.text.regexp(r'^[1-9]\d*$'))
async def process_choise_digit(message: Message):
    user_id = message.from_user.id
    choice_digit_user = message.text
    user_data[user_id]['choice_digit'] = choice_digit_user
    await message.answer(f'Вы выбрали шаг сдвига: {choice_digit_user}\n\nОтправьте сообщение для шифрования:')

eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

#Хендлер отправки текста
@router.message(F.text)
async def process_cipher(message: Message):
    user_id = message.from_user.id
    text_user = message.text
    result = ''

    for i in range(len(text_user)):

        if user_data[user_id]['language'] == 'Русский🇷🇺':
            alphas = 32
            low_alphabet = rus_lower_alphabet
            upp_alphabet = rus_upper_alphabet
        if user_data[user_id]['language'] == 'Английский🇺🇲':
            alphas = 26
            low_alphabet = eng_lower_alphabet
            upp_alphabet = eng_upper_alphabet
                
        if text_user[i].isalpha():
            if text_user[i] == text_user[i].lower():
                place = low_alphabet.index(text_user[i])
            if text_user[i] == text_user[i].upper():
                place = upp_alphabet.index(text_user[i])

            if user_data[user_id]['cipher_mode'] == 'Шифрование🔐':
                index = (place + int(user_data[user_id]['choice_digit'])) % alphas
                
            elif user_data[user_id]['cipher_mode'] == 'Дешифрование🔓':
                index = (place - int(user_data[user_id]['choice_digit'])) % alphas

            if text_user[i] == text_user[i].lower():
                result += low_alphabet[index]
            if text_user[i] == text_user[i].upper():
                result += upp_alphabet[index]    

        else:
            result += text_user[i]

    await message.answer(f'{result}\n\nОтправьте в чат сообщение для шифрования, либо настройте параметры заново: /start')






# Хендлер на callback_query
@router.callback_query(F.data == "button1")
async def process_button1(callback: CallbackQuery):
    await callback.answer("Вы нажали кнопку 1!")

@router.callback_query(F.data == "button2")
async def process_button2(callback: CallbackQuery):
    await callback.answer("Вы нажали кнопку 2!") 