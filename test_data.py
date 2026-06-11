from pymongo import MongoClient
from pymongo.server_api import ServerApi
import certifi

uri = "mongodb+srv://akashdhsrnm_db_user:Akashdh%408@cluster0.jstclaj.mongodb.net/?appName=Cluster0"

client = MongoClient(
    uri,
    server_api=ServerApi('1'),
    tls=True,
    tlsCAFile=certifi.where()
)

try:
    client.admin.command('ping')
    print("Connected!")
except Exception as e:
    print(e)