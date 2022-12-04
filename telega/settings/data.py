from settings.meta_engine import get_engine

engine = get_engine()
conn = engine.connect()


try:
    TOKEN = conn.execute("""SELECT token FROM data WHERE id=1""").fetchone()[0]
    user = conn.execute("""SELECT user_id FROM data WHERE id=1""").fetchone()[0]
except:
    raise SystemExit('нет данных')

path = "photo/screen.png"
#path_img = "imgs/nya.png"

