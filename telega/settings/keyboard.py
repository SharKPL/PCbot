from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


off = KeyboardButton('/off')
screen = KeyboardButton('/screen')
cancel = KeyboardButton('/cancel')
web = KeyboardButton('/web')
myId = KeyboardButton('/myId')
com_kb = ReplyKeyboardMarkup()
com_kb.add(off).add(screen).add(cancel).add(web).add(myId)
