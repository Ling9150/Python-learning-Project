import sqlite3
import json

def init_db():
    coon = sqlite3.connect("cache.db")
