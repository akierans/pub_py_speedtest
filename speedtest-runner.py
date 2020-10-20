import speedtest
from pymongo import MongoClient
from dotenv import load_dotenv
load_dotenv()
import os
import mysql.connector
from datetime import date, datetime, timedelta
import json

#mongo-pw is the .env variable
pw = os.environ.get("mongo-pw")
mysqlpw = os.environ.get("mysql-pw")
#import urllib.parse

servers = []
# If you want to test against a specific server
# servers = [1234]

threads = None
# If you want to use a single threaded test
# threads = 1

s = speedtest.Speedtest()

s.download(threads=threads)

s.upload(threads=threads)

s.results.share()

results_dict = s.results.dict()

r = results_dict

#MongoDB Connection
#username = urllib.parse.quote_plus('admin')
#password = urllib.parse.quote_plus('M1d568d00e!')
#conn = MongoClient('mongodb://%s%s@192.168.1.137' % (username, password))

uri = f"mongodb://admin:{pw}@localhost/admin"
client = MongoClient(uri)

mydb = client["db_speedtest"]
mycol = mydb["results"]

x = mycol.insert_one(results_dict)

#MySQL Connection and Insert
cnx = mysql.connector.connect(user='speedtest', password=f"{mysqlpw}", host='127.0.0.1', database='speedtest')
cursor = cnx.cursor()

add_speedtest = ("INSERT INTO results "
	"(client, server, bytes_received, bytes_sent, downoad, upload, ping, share, timestamp)"
	"VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")

now = datetime.datetime.now()
formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')

client = r.get('client')
server = r.get('server')

data_speedtest = (json.dumps(client),json.dumps(server),r.get('bytes_received'),r.get('bytes_sent'),r.get('downoad'),
	r.get('upload'),r.get('ping'),r.get('share'),formatted_date)

cursor.execute(add_speedtest, data_speedtest)

cnx.commit()

cursor.close()
cnx.close()