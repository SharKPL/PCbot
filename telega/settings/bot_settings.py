import logging
import os


# from pydub import AudioSegment
import cv2
#import speech_recognition as sr
from PIL import ImageGrab
from aiogram import executor, types
from aiogram.types import ContentType, Message

from settings.bot_create import dp, bot
from settings.data import user, path
from settings.keyboard import com_kb
from settings.data import keys, closkeys, coms, coms_list


logging.basicConfig(level=logging.INFO)


# вывод комманд
@dp.message_handler(commands=['start', 'help'])
async def start_message(message: types.message):
    user_id = message.from_user.id
    logging.info(f'{user_id}')
    # img = open(path_img, 'rb')
    await bot.send_message(chat_id=message.chat.id, reply_markup=com_kb, text='Вот комманды')
    await message.delete()


# выключение компьютера
@dp.message_handler(text='выключить')
async def off_message(message: types.message):
    user_id = message.from_user.id
    if user_id == user:
        await bot.send_message(user_id, "пк выключится через 5 минут")
        os.system("shutdown -s -t 300")


@dp.message_handler(text='список команд')
async def off_message(message: types.message):
    user_id = message.from_user.id
    if user_id == user:

        await bot.send_message(user_id, "\n".join(list(coms_list.keys())))
# окрытие
@dp.message_handler(text=keys)
async def off_message(message: types.message):
    user_id = message.from_user.id
    if user_id == user:
        for i in coms:
            if list(i.keys())[0] == message.text:
                os.startfile(f'{i[message.text]}')
                await bot.send_message(user_id, f"{i[message.text].split('/')[-1]} открывается")
                print(f"{i[message.text].split('/')[-1]} открывается")


# закрытие программ
@dp.message_handler(text=closkeys)
async def off_message(message: types.message):
    user_id = message.from_user.id
    if user_id == user:
        for i in closkeys:

            if i == message.text:
                for d in coms:
                    if list(d.keys())[0] == message.text.split(" ")[0]:
                        os.system(f'taskkill /f /im {d[list(d.keys())[0]].split("/")[-1]}')
                        await bot.send_message(user_id, f"{d[list(d.keys())[0]].split('/')[-1]} закрывается")
                        print(f"{d[list(d.keys())[0]].split('/')[-1]} закрывается")


# отмена выключения компьютера
@dp.message_handler(text='отмена')
async def off_message(message: types.message):
    user_id = message.from_user.id
    if user_id == user:
        os.system("shutdown -a")
        await bot.send_message(user_id, "отмена выключения")


# снимок экрана
@dp.message_handler(text='скрин')
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


# снимок с вебкамеры
@dp.message_handler(text='снимок вебки')
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


# выводит id пользователя в чат
@dp.message_handler(text='id')
async def screen_message(message: types.message):
    user_id = message.from_user.id
    await bot.send_message(user_id, f'{user_id}')


# async def handle_file(file: File, file_name: str, path: str):
#     Path(f"{path}").mkdir(parents=True, exist_ok=True)
# 
#     await bot.download_file(file_path=file.file_path, destination=f"{path}/{file_name}")


@dp.message_handler(content_types=[ContentType.VOICE])
async def voice_message_handler(message: Message):
    file_id = message.voice.file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    file_name = str(message.message_id)
    # aud = bot.(file_id)
    # print(aud)
    print(file_name)
    await bot.download_file(file_path, "voice/temp.mp3")
    # AudioSegment.converter = r"C:\\x\\build\\win\\64\\ffmpeg.exe"
    # AudioSegment.ffprobe = r"C:\\x\\build\\win\\64\\ffprobe.exe"
    f_path = os.path.abspath("voice/temp.mp3")
    print(f_path)
    # audio = AudioSegment.from_file(f_path)
    # audio.export("output.wav", format="wav")
    # wf = wave.open("voice/temp.wav", "rb")
    r = sr.Recognizer()

    # Загрузка аудиофайла
    with sr.AudioFile('voice/temp.ogg') as source:
        # Обработка шума в аудиофайле
        r.adjust_for_ambient_noise(source)
        # Преобразование аудио в текст
        audio_text = r.recognize_google(r.record(source), language='ru-RU')

    print(audio_text)

# @dp.message_handler(content_types=[ContentType.VOICE])
# async def voice_message_handler(message: Message):
#
#     file_id = message.voice.file_id
#     # Получение объекта Audio по file_id
#     voice_message = await bot.get_file(file_id)
#     file = await bot.get_file(file_id)
#     file_path = file.file_path
#
#     path = "voice"
#
#     # Загрузка голосового сообщения в папку с проектом
#     await voice_message.download(file_path, destination_dir="voice")
#
#     # Путь к сохраненному файлу
#     #file_path = os.path.abspath(path)
#
#     # Делаем что-то с сохраненным голосовым сообщением
#     # ...
#
#     # Удаляем файл после использования
#     #os.remove(file_path)


# прием любых файлов
@dp.message_handler(content_types=[ContentType.ANY])
async def unknown_message(message: types.Message):
    if document := message.document:
        await document.download(destination_file=f'files/{document.file_name}')


if __name__ == '__main__':
    executor.start_polling(dp)
