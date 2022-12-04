import os
import logging

import cv2
from PIL import ImageGrab
from aiogram import executor, types

from settings.keyboard import com_kb

from settings.data import user, path
from settings.bot_create import dp, bot


logging.basicConfig(level=logging.INFO)


#вывод комманд
@dp.message_handler(commands=['start', 'help'])
async def start_message(message: types.message):
    user_id = message.from_user.id
    logging.info(f'{user_id}')
    #img = open(path_img, 'rb')
    await bot.send_message(chat_id=message.chat.id, reply_markup=com_kb, text='Вот комманды')
    await message.delete()


#выключение компьютера
@dp.message_handler(commands=['off'])
async def off_message(message: types.message):
    user_id = message.from_user.id
    if user_id == user:
        await bot.send_message(user_id, "пк выключится через 5 минут")
        os.system("shutdown -s -t 300")


#отмена выключения компьютера
@dp.message_handler(commands=['cancel'])
async def off_message(message: types.message):
    user_id = message.from_user.id
    if user_id == user:
        os.system("shutdown -a")
        await bot.send_message(user_id, "отмена выключения")


#снимок экрана
@dp.message_handler(commands=['screen'])
async def screen_message(message: types.message):
    user_id = message.from_user.id
    if user_id == user:
        if not os.path.isfile(path):
            pass
        else:
            os.remove("photo/screen.png")
        chat_id = message.chat.id
        pic = ImageGrab.grab()
        pic.save(path)
        screen = open(path, 'rb')
        await bot.send_photo(chat_id=chat_id, photo=screen)


#снимок с вебкамеры
@dp.message_handler(commands=['web'])
async def screen_message(message: types.message):
    user_id = message.from_user.id
    if user_id == user:
        try:
            chat_id = message.chat.id
            cap = cv2.VideoCapture(0)

            # "Прогреваем" камеру, чтобы снимок не был тёмным
            for i in range(5):
                cap.read()

            # Делаем снимок
            ret, frame = cap.read()

            # Записываем в файл
            cv2.imwrite('photo/cam.png', frame)

            # Отключаем камеру
            cap.release()
            photo = open('photo/cam.png', 'rb')
            await bot.send_photo(chat_id=chat_id, photo=photo)

        except:
            await bot.send_message(user_id, "у тебя нет вебки")


#выводит id пользователя в чат
@dp.message_handler(commands=['myId'])
async def screen_message(message: types.message):
    user_id = message.from_user.id
    await bot.send_message(user_id, f'{user_id}')


if __name__ == '__main__':
    executor.start_polling(dp)
