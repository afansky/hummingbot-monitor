import sqlite3
import sys
import requests

if len(sys.argv) < 4:
    exit(1)

db_filename = sys.argv[1]
url = sys.argv[2]
name = sys.argv[3]

con = sqlite3.connect(db_filename)
cur = con.cursor()
cur.execute("select count(*) from TradeFill")

trades = cur.fetchone()[0]

requests.post(url, json=
{
    "name": name,
    "trades": trades
})
