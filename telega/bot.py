from settings.bot_settings import *


def bot_start():
    executor.start_polling(dp)


if __name__ == '__main__':
    bot_start()


