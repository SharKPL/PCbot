from settings.meta_engine import get_engine

engine = get_engine()
conn = engine.connect()


def dialog():
    token_av = input("Тебе нужно добавить токен?: y/n \n")
    if token_av.lower() == 'n':
        pass
    elif token_av.lower() == 'y':
        token = str(input("введи токен \n"))
        exz = f"""UPDATE data set token='{token}' WHERE id=1"""
        conn.execute(exz)
    id_av = input("знаешь ли свой id?: y/n \n")
    if id_av.lower() == 'n':
        pass
    elif id_av.lower() == 'y':
        ids = str(input("введи id \n"))
        exz = f"""UPDATE data set user_id='{ids}' WHERE id=1"""
        conn.execute(exz)


if __name__ == '__main__':
    try:
        dialog()
    except:
        pass

