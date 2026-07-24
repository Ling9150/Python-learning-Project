import sqlite3
import json
from datetime import datetime,timedelta

def init_db():
    conn = sqlite3.connect("cache.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS vuln_cache(
            package_name TEXT,
            version TEXT,
            response_json TEXT,
            cached_time TEXT,   
            PRIMARY KEY (package_name,version)
        )
    ''')
    conn.commit()
    conn.close()

def save_cache(package_name,version,response_json,cached_time):
    conn = sqlite3.connect("cache.db")
    cursor = conn.cursor()
    cursor.execute(
    """
        INSERT OR REPLACE INTO vuln_cache VALUES(?,?,?,?)
    """,
        (
        package_name,
        version,
        json.dumps(response_json),
        cached_time
        )
    )
    conn.commit()
    conn.close()

def get_cache(package_name,version):
    conn = sqlite3.connect("cache.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT response_json,cached_time From vuln_cache
        WHERE package_name = ? AND version = ?
        """,
        (
            package_name,
            version
        )
    )
    result = cursor.fetchone()
    conn.close()
    if not result:
        return None
    response_json = result[0]
    cached_time = result[1]
    cached_dt = datetime.fromisoformat(cached_time)
    now = datetime.now()
    if now - cached_dt > timedelta(days=7):
        return None
    return json.loads(response_json)

if __name__ == "__main__":
    init_db()
    save_cache(
        "d",
        "2.0",
        {"test":"hello"},
        str(datetime.now())
    )
    result = get_cache("d","2.0")
    print(result)