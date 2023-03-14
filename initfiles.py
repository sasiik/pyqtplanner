import os
import sqlite3
from PyQt5.QtCore import QStandardPaths, qDebug
import csv


def create_db(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        cur = conn.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS tasks (
                                   title      STRING  NOT NULL,
                                   circ_count INTEGER NOT NULL,
                                   completed  BOOLEAN NOT NULL,
                                   id         INTEGER PRIMARY KEY AUTOINCREMENT
                                                      UNIQUE
                                                      NOT NULL
                   )
                   """)
        conn.commit()

    except Exception as e:
        print(e)

    return conn


def create_config(path):
    if not os.path.exists(path):
        with open(path, 'w', encoding='utf-8') as configfile:
                writer = csv.writer(configfile, delimiter=';', quotechar='"')
                writer.writerow([1500, 300, 900])


def init_files():
    appdata_path = QStandardPaths.writableLocation(QStandardPaths.AppLocalDataLocation)
    print(appdata_path)
    abs_dir_app = os.path.join(appdata_path, f".pyqtplanner")
    if not os.path.exists(abs_dir_app):
        os.mkdir(abs_dir_app)
    db_path = os.path.join(abs_dir_app, 'tasks.sqlite')
    con = create_db(db_path)
    config_path = os.path.join(abs_dir_app, 'config.csv')
    create_config(config_path)

    return con, config_path


con, config_path = init_files()
