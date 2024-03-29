import speedtest
from dotenv import load_dotenv
load_dotenv()
import os
import mysql.connector
from datetime import date, datetime, timedelta
import json

#mysql-pw is the .env variable
mysqlpw = os.environ.get("mysql-pw")

servers = []
# If you want to test against a specific server
# servers = [1234]

threads = None
# If you want to use a single threaded test
# threads = 1

#Which speedtests to run
s = speedtest.Speedtest()
s.download(threads=threads)
s.upload(threads=threads)
s.results.share()

#Store results in a dictionary
results_dict = s.results.dict()
r = results_dict

#MySQL Connection and Insert
cnx = mysql.connector.connect(user='speedtest', password=f"{mysqlpw}", host='127.0.0.1', database='speedtest')
cursor = cnx.cursor()

add_speedtest = ("INSERT INTO results "
	"(client, server, bytes_received, bytes_sent, download, upload, ping, share, timestamp)"
	"VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")

now = datetime.now()
formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')

client = r.get('client')
server = r.get('server')

data_speedtest = (json.dumps(client),json.dumps(server),r.get('bytes_received'),r.get('bytes_sent'),r.get('download'),
	r.get('upload'),r.get('ping'),r.get('share'),formatted_date)

cursor.execute(add_speedtest, data_speedtest)

cnx.commit()

cursor.close()
cnx.close()
