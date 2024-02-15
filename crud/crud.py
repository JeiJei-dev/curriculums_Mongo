from json import loads

def create(records):
    vals = []
    option = ""
    while option.upper() != "EXIT":
        option = input("Please type the new record ('Exit' for leave): ")
        if option.upper() != "EXIT":
            value = loads(option)
            vals.append(value)

def read(records):
    query = loads(input("Type your Query: "))
    res = records.find(query)
    
    for value in res:
        print(value)

def update(records):
    pass

def delete(records):
    pass

def upload_file(records):
    file_name = "curriculums.json" # input("Enter the file name: ")
    with open(file_name) as file:
        res = loads(file.read())
        res = records.insert_many(res)