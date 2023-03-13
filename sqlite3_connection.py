import sqlite3
from resourcepath import resource_path

con = sqlite3.connect(resource_path("tasks.sqlite"))