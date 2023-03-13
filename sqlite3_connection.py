import sqlite3
from resourcepath import get_config_path

con = sqlite3.connect(get_config_path("tasks.sqlite"))