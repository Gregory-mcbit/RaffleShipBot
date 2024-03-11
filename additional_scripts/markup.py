from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def make_markup(*info):
    """Makes markup with transmitted info"""
    kb = []
    for elem in list(info):
        btn = KeyboardButton(text=elem)
        kb.append([btn])
    
    return ReplyKeyboardMarkup(resize_keyboard=True, keyboard=kb)
