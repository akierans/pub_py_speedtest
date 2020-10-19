import speedtest
import pymongo

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

conn = pymongo.MongoClient("mongodb://192.168.1.134:27017/")
mydb = conn["db_speedtest"]
mycol = mydb["results"]

x = mycol.insert_one(results_dict)