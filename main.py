from pymongo import MongoClient
from crud import create, read, update, delete, upload_file

MONGO_URI = "mongodb://localhost"
CLIENT  = MongoClient(MONGO_URI)
DB = CLIENT["DBProject"]
CURRICULUMS = DB["curriculum"]

OPTIONS = {
    "CREATE": create,
    "READ": read,
    "UPDATE": update,
    "DELETE": delete,
    "FILE": upload_file,
}

option = ""

while option.upper() != "EXIT":
    print("""
        Hey, choose your option:
            CREATE
            READ
            UPDATE
            DELETE
            FILE
            EXIT
    """)
    option = input("Your option: ").upper()

    if option in OPTIONS.keys():
        OPTIONS[option](CURRICULUMS)