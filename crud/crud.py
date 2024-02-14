from json import loads

def create(records):
    pass

def read(records):
    pass

def update(records):
    pass

def delete(records):
    pass

def upload_file(records):
    file_name = "curriculums.json" # input("Enter the file name: ")
    with open(file_name) as file:
        res = loads(file.read())
        records.insert_many(res)